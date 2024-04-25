# Copyright (c) 2024, tejal and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class MoistureTest(Document):


	@frappe.whitelist()
	def fixed_child_entries(self):
		if not self.get("oven_child_table"):
			self.add_fixed_entries_to_child_table()
			

	def add_fixed_entries_to_child_table(self):
		fixed_entries = [
			{"test_name": "Number of Container"},
			{"test_name": "Wt of Con+Cover(M1)"},
			{"test_name":"WtCon+Cover+Seed BfDrying(M2)"},
			{"test_name":"WtCon+Cover+Seed AfDrying(M3)"},
			{"test_name": "Wt of Seed(M2-M1)"},
			{"test_name": "Loss of Weight(M2-M3)"},
			{"test_name":"Moisture Content"},
		]
		for entry in fixed_entries:
			self.append("oven_child_table", entry)



	@frappe.whitelist()
	def fixed_child(self):
		if not self.get("electronic_moisture_method"):
			self.add_fixed_entrie()
			

	def add_fixed_entrie(self):
		fixed_entries = [
			{"sample_no": "1"},
			{"sample_no": "2"},
			{"sample_no":"3"},
		]
		for entry in fixed_entries:
			self.append("electronic_moisture_method", entry)



			


	@frappe.whitelist()
	def get_valid_seed_quality_inspections(self):
		seed_quality_inspections = frappe.db.sql("""
			SELECT parent 
			FROM `tabSeed Quality Test Child Table` 
			WHERE test = 'Moisture Test';
		""", as_dict=True)

		parent_id_list = []

		for i in seed_quality_inspections:
			parent_id_list.append(i.parent)

		return parent_id_list

	@frappe.whitelist()
	def changes_status(self):
		name = frappe.get_value("Seed Quality Test Child Table", 
							filters={"parent": self.seed_q_i_no,"test":self.test_name},
							fieldname=["name"]) 

		# temp = frappe.get_doc('Seed Quality Test Child Table',name)
		# temp.status='Completed'
		# temp.result = self.result
		# temp.save()
		frappe.db.set_value('Seed Quality Test Child Table', name, 'status', 'Completed')
		frappe.db.set_value('Seed Quality Test Child Table', name, 'result', self.result)
		