# Copyright (c) 2024, tejal and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class InvoiceProcessing(Document):

	@frappe.whitelist()
	def get_all_supplier(self):
		if self.from_date and self.to_date:
			org_dict = set()
			org = frappe.get_all("Seed Procurement",
								filters={"date": ["between", [self.from_date, self.to_date]]},
								fields=["organizer_name"],)
			if org:
				for o in org:
					if o.organizer_name not in org_dict:
						self.append('select_organizer', {
							"organizer_name": o.organizer_name
						})
						org_dict.add(o.organizer_name)


	@frappe.whitelist()
	def selectall(self):
		children = self.get('select_organizer')
		if not children:
			return
		all_selected = all([child.check for child in children])  
		value = 0 if all_selected else 1 
		for child in children:
			child.check = value
			
	
	@frappe.whitelist()
	def get_lot_and_farmer_details(self):
			for i in self.get('select_organizer'):
					if i.check==True:
							doc = frappe.get_all("Seed Procurement", 
											filters={"date": ["between", [self.from_date, self.to_date]],"organizer_name":i.organizer_name,"crop_variety":self.crop_name,"lot_status":"Lot Approved"},
											fields=["name","organizer_name","farmer_id","farmer_name","date","crop_variety","lot_weight","contact","unitwt","target_warehouse"],)
							# frappe.throw(str(doc))
							if(doc):
								for d in doc:
									self.append('invoice', {
														"lot_id":d.name,
														"farmer_id":d.farmer_id,
														"farmer_name":d.farmer_name,
														"crop_variety":d.crop_variety,
														"lot_weight":d.lot_weight,
														"organizer_name":d.organizer_name,
														"rate":self.rate,
														"contact":d.contact,
														"source_warehouse":d.target_warehouse,
														"unit":d.unitwt,
														"date":d.date })



	@frappe.whitelist()
	def checkall(self):
		children = self.get('invoice')
		if not children:
			return
		all_selected = all([child.check for child in children])  
		value = 0 if all_selected else 1 
		for child in children:
			child.check = value

	def on_submit(self):
		self.purchase_invoice_entry()
		self.stock_repack_entry()
		self.changes_status()
		
	@frappe.whitelist()
	def purchase_invoice_entry(self):
		for j in self.get("select_organizer"):
			if j.check ==True:
				purchase_entry_naming_series="ACC-PINV-.YYYY.-"
				doc = frappe.new_doc("Purchase Invoice")
				doc.supplier =j.organizer_name
				doc.naming_series=purchase_entry_naming_series
				for i in self.get("invoice"):
					if i.check:
						if i.organizer_name==j.organizer_name:
							doc.append("items",{
										"item_name": i.crop_variety,
										"qty":i.lot_weight,
										"expense_account":"Cash - E",
										"rate":i.rate,
										"lot_number":i.lot_id,
										"farmer_id":i.farmer_id,
										"farmer_name":i.farmer_name,
										"supplier":i.organizer_name,
										"contact":i.contact,
										"uom":i.unit
							})
					
				doc.invoice_processing=self.name
				doc.insert()
				doc.save()
				doc.submit()

	@frappe.whitelist()
	def changes_status(self):
		# frappe.msgprint('hiiiiiiiiii')
		for i in self.invoice:
			if i.check == True:
				frappe.db.set_value('Seed Procurement',i.lot_id, 'lot_status', 'Billed')

		frappe.msgprint("Status updated successfully.")


	@frappe.whitelist()
	def stock_repack_entry(self):
		for j in self.get("select_organizer"):
			if j.check == True:
				stock_entry_naming_series = "MAT-STE-.YYYY.-"
				doc = frappe.new_doc("Stock Entry")
				doc.stock_entry_type = "Rate Valuation"
				doc.naming_series = stock_entry_naming_series
				status=False
				total=0
				for i in self.get("invoice"):
					if i.check and i.organizer_name == j.organizer_name:	
						status=True
						doc.append("items",{
											"item_code": self.crop_name,
											"qty":i.lot_weight,
											"s_warehouse":i.source_warehouse,
											"batch_no":i.lot_id,
								})
						doc.append("items",{
										"item_code": self.crop_name,
										"qty":i.lot_weight,
										"basic_rate":self.rate,
										"batch_no":i.lot_id,
										"t_warehouse":self.target_warehouse,
										"is_finished_item":True,
										"set_basic_rate_manually":True,
										# "additional_cost":self.additional_cost,
										"basic_amount":i.lot_weight*self.rate,
										"amount":i.lot_weight*self.rate,
						})
						total=total+(i.lot_weight*self.rate)
				if status:
					doc.blending=self.name
					# doc.total_outgoing_value =total
					doc.insert()
					doc.save()
					doc.submit()


