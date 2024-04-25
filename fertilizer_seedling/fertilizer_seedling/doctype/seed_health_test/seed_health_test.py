# Copyright (c) 2024, tejal and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class SeedHealthTest(Document):
	
	@frappe.whitelist()
	def get_pn1_percen(self):
		self.pn1= (self.non1 / self.no1)*100

	@frappe.whitelist()
	def get_pn2_percen(self):
		self.pn2=(self.non2 / self.no2)*100

	@frappe.whitelist()
	def get_pn3_percen(self):
		self.pn3= (self.non3 / self.no3)*100

	@frappe.whitelist()
	def get_pn4_percen(self):
		self.pn4=(self.non4 / self.no4)*100

	@frappe.whitelist()
	def get_pn5_percen(self):
		self.pn5=(self.non5 / self.no5)*100
		
	
	@frappe.whitelist()
	def get_n1_percen(self):
		self.pnon1= (self.n1 / self.no1)*100
		
	@frappe.whitelist()
	def get_n2_percen(self):
		self.pnon2=(self.n2 / self.no2)*100

	@frappe.whitelist()
	def get_n3_percen(self):
		self.pnon3= (self.n3 / self.no3)*100

	@frappe.whitelist()
	def get_n4_percen(self):
		self.pnon4=(self.n4 / self.no4)*100

	@frappe.whitelist()
	def get_n5_percen(self):
		self.pnon5=(self.n5 / self.no5)*100
		

	@frappe.whitelist()
	def get_valid_seed_quality_inspections(self):
		seed_quality_inspections = frappe.db.sql("""
			SELECT parent 
			FROM `tabSeed Quality Test Child Table` 
			WHERE test = 'Seed Health test';
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