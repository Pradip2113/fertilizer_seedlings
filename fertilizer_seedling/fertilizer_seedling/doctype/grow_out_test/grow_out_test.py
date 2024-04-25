# Copyright (c) 2024, tejal and contributors
# For license information, please see license.txt

import datetime
import frappe
from frappe.model.document import Document

class GrowOutTest(Document):
	
	# @frappe.whitelist()
	# def get_sowing_date(self):
	# 		doc = frappe.get_all("Inspection Internal Operation Child Table", 
	# 						filters={"parent": self.seed_quality_inspection_number,"operation_name": "sowing of seeds"},
	# 						fields=["date"],)
			
	# 		# frappe.msgprint('doc')
	# 		for d in doc:
	# 			self.date_of_sowing = d.date
			
	
	
	@frappe.whitelist()
	def get_valid_seed_quality_inspections(self):
		seed_quality_inspections = frappe.db.sql("""
			SELECT parent 
			FROM `tabSeed Quality Test Child Table` 
			WHERE test = 'Grow Out Test';
		""", as_dict=True)

		parent_id_list = []

		for i in seed_quality_inspections:
			parent_id_list.append(i.parent)

		return parent_id_list


	@frappe.whitelist()
	def changes_status(self):
		name = frappe.get_value("Seed Quality Test Child Table", 
							filters={"parent": self.seed_quality_inspection_number,"test":self.test_name},
							fieldname=["name"]) 
		frappe.db.set_value('Seed Quality Test Child Table', name, 'status', 'Completed')
		frappe.db.set_value('Seed Quality Test Child Table',name,'result',self.result)