# Copyright (c) 2024, tejal and contributors
# For license information, please see license.txt
import frappe
from frappe.model.document import Document

class SeedProcurement(Document):


	def on_submit(self):
		self.material_receipt_stock_entry()

	@frappe.whitelist()
	def material_receipt_stock_entry(self):
		doc1=frappe.new_doc("Batch")
		doc1.batch_id=self.name
		doc1.item=self.crop_variety
		doc1.manufacturing_date=self.date
		doc1.save()

		stock_entry_naming_series="MAT-STE-.YYYY.-"
		doc = frappe.new_doc("Stock Entry")
		doc.stock_entry_type ="Material Receipt"
		doc.naming_series=stock_entry_naming_series
		doc.append("items",{
					"item_code": self.crop_variety,
					"qty":self.lot_weight,
					# "s_warehouse":self.source_warehouse,
					"t_warehouse":self.target_warehouse,
					"allow_zero_valuation_rate":True,	
					"batch_no":self.name,
		})

		doc.seed_procurement=self.name
		doc.insert()
		doc.submit()

   
	def on_trash(self):
		self.delete_material_receipt_stock_entry()
	
	def delete_material_receipt_stock_entry(self):
		frappe.delete_doc("Stock Entry",self.name,force=True)

	@frappe.whitelist()
	def calculate_lot_weight(self):
		self.lot_weight= (self.loaded_weight or 0)- (self.empty_weight or 0)
		return self.lot_weight
		

