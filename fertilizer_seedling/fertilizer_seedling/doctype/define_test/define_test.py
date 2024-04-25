# Copyright (c) 2024, tejal and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class DefineTest(Document):

	@frappe.whitelist()
	def fixed_child_entries(self):
		if not self.get("test_information"):
			self.add_fixed_entries_to_child_table()		

	def add_fixed_entries_to_child_table(self):
		fixed_entries = [
			{"test": "Physical Purity Test"},
			{"test": "Virus Test"},
			{"test":"Grow Out Test"},
			{"test":"Seed Health Test"},
			{"test":"Moisture Test"},
			{"test":"Germination Test"},
		]
		for entry in fixed_entries:
			self.append("test_information", entry)


	@frappe.whitelist()
	def checkall(self):
		children = self.get('test_information')
		if not children:
			return
		all_selected = all([child.check for child in children])  
		value = 0 if all_selected else 1 
		for child in children:
			child.check = value




	@frappe.whitelist()
	def get_sowing_date(self):
		date = frappe.get_value("Inspection Internal Operation Child Table", 
								filters={"parent": self.farm_inspection_id, "operation_name": "sowing of seeds"},
								fieldname="date")  
		frappe.msgprint(str(date))
		self.date_of_sowing = date


		# doc.define_test_id=self.name

	@frappe.whitelist()
	def changes_status(self):
		
		name = frappe.get_value("Seed Procurement", 
							filters={"name": self.seed_procurement_id},
							fieldname=["name"]) 
		frappe.db.set_value('Seed Procurement', name, 'lot_status', "Inspection In-Process")
		



























	# @frappe.whitelist()
	# def get_current_user_name(self):
	# 	if not self.supervisor_name and not self.supervisor_id:
	# 		user_name = frappe.session.user
	# 		doc = frappe.get_all("Employee", 
	# 							filters={"user_id":user_name},
	# 							fields=["name","employee_name"],)
	# 		if doc:
	# 			for d in doc :
	# 				self.supervisor_id = d.name
	# 				self.supervisor_name = d.employee_name