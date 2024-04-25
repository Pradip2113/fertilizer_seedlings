# Copyright (c) 2024, tejal and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class VirusTest(Document):
	
	@frappe.whitelist()
	def get_valid_seed_quality_inspections(self):
		seed_quality_inspections = frappe.db.sql("""
			SELECT parent 
			FROM `tabSeed Quality Test Child Table` 
			WHERE test = 'Virus Test';
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
		frappe.db.set_value('Seed Quality Test Child Table', name, 'status', 'Completed')
		frappe.db.set_value('Seed Quality Test Child Table', name, 'result', self.result)
