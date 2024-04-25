# Copyright (c) 2024, tejal and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class GerminationTest(Document):
	
	@frappe.whitelist()
	def fixed_child_entries(self):
		if not self.get("replication1_child_table"):
			self.add_fixed_entries_to_child_table()
			

	def add_fixed_entries_to_child_table(self):
		fixed_entries = [
			{"idx1": ""},
			{"idx2": ""},
			{"idx3":""},
			
		]
		for entry in fixed_entries:
			self.append("replication1_child_table", entry)

	@frappe.whitelist()
	def fixed_child(self):
		if not self.get("replication2_child_table"):
			self.add_fixed_entries_to_child()
			

	def add_fixed_entries_to_child(self):
		fixed_entries = [
			{"idx1": ""},
			{"idx2": ""},
			{"idx3":""},
			
		]
		for entry in fixed_entries:
			self.append("replication2_child_table", entry)

	@frappe.whitelist()
	def fixed_child_entri(self):
		if not self.get("replication3_child_table"):
			self.add_fixed_entries_to()
			

	def add_fixed_entries_to(self):
		fixed_entries = [
			{"idx1": ""},
			{"idx2": ""},
			{"idx3":""},
			
		]
		for entry in fixed_entries:
			self.append("replication3_child_table", entry)


	@frappe.whitelist()
	def fixed(self):
		if not self.get("replication4_child_table"):
			self.add_fixed()
			

	def add_fixed(self):
		fixed_entries = [
			{"idx1": ""},
			{"idx2": ""},
			{"idx3":""},
			
		]
		for entry in fixed_entries:
			self.append("replication4_child_table", entry)

	@frappe.whitelist()
	def get_valid_seed_quality_inspections(self):
		seed_quality_inspections = frappe.db.sql("""
			SELECT parent 
			FROM `tabSeed Quality Test Child Table` 
			WHERE test = 'Germination Test';
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
		frappe.db.set_value('Seed Quality Test Child Table',name,'result',self.result)