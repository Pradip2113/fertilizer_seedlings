# Copyright (c) 2024, tejal and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Blending(Document):
	

	def on_update(self):
		self.material_receipt_stock_entry()

	@frappe.whitelist()
	def material_receipt_stock_entry(self):

		stock_entry_naming_series="MAT-STE-.YYYY.-"
		doc = frappe.new_doc("Stock Entry")
		doc.stock_entry_type ="Repack"
		doc.naming_series=stock_entry_naming_series
		for i in self.get("blending_child_table"):
			doc.append("items",{
							"item_code": self.crop_variety,
							"qty":i.lot_weight,
							"s_warehouse":i.source_warehouse,
			})
		else:
			doc.append("items",{
							"item_code": self.crop_variety,
							"qty":self.total_weight,
							"t_warehouse":self.target_warehouse,
							"is_finished_item":True,
			})
		
		doc.blending=self.name
		doc.insert()
		doc.save()
		doc.submit()

	@frappe.whitelist()
	def get_lot_info(self):
		# if self.get_available_lot_no:
			
			lot_weight

			if(doc):
				for d in doc:
					if not d.check:
						self.append('blending_child_table',{
							"lot_number":d.lot_number,
							"lot_weight":d.lot_wt,
							"unit":d.unitl,
							"source_warehouse":d.target_warehouse,
							# 'procurement_date': frappe.get_value("Seed Procurement",{'name':self.lot_number,'crop':self.crop_name,'crop_variety':self.crop_variety,},'date')
						})

			self.calculate_child_table()	



	@frappe.whitelist()
	def changes_status(self):
		# frappe.msgprint('hiii') 
		name = frappe.get_all("Seed Quality Inspection", 
							filters={"crop":self.crop_name,"crop_variety":self.crop_variety},
							fields=["name"])
		# frappe.msgprint(str(name)) 
		if(name):
			for n in name:
				frappe.db.set_value('Seed Quality Inspection', n, 'check', '1')


	def on_trash(self):
		self.uncheck_field()
	def uncheck_field(self):
		# if self.get_available_lot_no:
			name_list = frappe.get_all("Seed Quality Inspection", 
								filters={"crop":self.crop_name,"crop_variety":self.crop_variety},
								fields=["name", "check"])
			
			if(name_list):
				for item in name_list:
					if item.check:
						frappe.db.set_value('Seed Quality Inspection', item, 'check', '0')


	@frappe.whitelist()
	def calculate_child_table(self):		
		table = self.get('blending_child_table')
		total = 0
		
		for i in table:
			total += i.lot_weight
			# frappe.msgprint(str(total))
		self.total_weight = total
		# self.get_procurement_date()
		

	


