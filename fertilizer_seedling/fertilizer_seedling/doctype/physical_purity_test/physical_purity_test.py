# Copyright (c) 2024, tejal and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
import statistics
class PhysicalPurityTest(Document):

	# @frappe.whitelist()
	# def get_Allocated_Seed_Price(self):
	# 	self.allocated_seed_cost_price = self.allocated_seed * self.cost_price_kg
	# 	return self.allocated_seed_cost_price

	@frappe.whitelist()
	def get_pure_seed_percen(self):
		self.pure_seed_percen= (self.pure_seed_gm /self.total_gm_test1)*100
		self.total_pure_seed_gm_result() 
		self.total_wt_of_components()
		self.total_wt_of_components_result()
		self.total_pure_seed_mean()
		self.final_result()
			
	@frappe.whitelist()
	def get_inert_matter_percen(self):
		self.inert_matter_percen= (self.inert_matter_gm /self.total_gm_test1)*100 
		self.total_inert_matter_result()
		self.total_wt_of_components()
		self.total_wt_of_components_result()
		self.total_inert_matter_mean()
		self.final_result()
	
	@frappe.whitelist()
	def get_other_seed_percen(self):
		self.other_seed_percen= (self.other_seed_gm /self.total_gm_test1)*100
		self.total_other_seed_result()
		self.total_wt_of_components()
		self.total_wt_of_components_result()
		self.total_other_seed_mean()
		self.final_result()
	
	
	@frappe.whitelist()
	def get_pure_seed_2_percen(self):
		self.pure_seed_2_percen= (self.pure_seed_2_gm / self.total_gm_test2)*100
		self.total_pure_seed_gm_result() 
		self.total_wt_of_components_test2()
		self.total_wt_of_components_result()
		self.total_pure_seed_mean()
		self.final_result()

	@frappe.whitelist()
	def get_inert_matter_2_percen(self):
		self.inert_matter_2_percen= (self.inert_matter_2 / self.total_gm_test2)*100
		self.total_inert_matter_result()
		self.total_wt_of_components_test2()
		self.total_wt_of_components_result()
		self.total_inert_matter_mean()
		self.final_result()
	
		
	@frappe.whitelist()
	def get_other_seed_2_percen(self):
		self.other_seed_2_percen= (self.other_seed_2 / self.total_gm_test2)*100
		self.total_other_seed_result()
		self.total_wt_of_components_test2()
		self.total_wt_of_components_result()
		self.total_other_seed_mean()
		self.final_result()
		
	@frappe.whitelist()
	def total_pure_seed_gm_result(self):
		self.total_pure_seed_gm = self._calculate_total(self.pure_seed_gm, self.pure_seed_2_gm)		

	@frappe.whitelist()
	def total_inert_matter_result(self):
		self.total_inert_matter_gm = self._calculate_total(self.inert_matter_gm, self.inert_matter_2)
		
	@frappe.whitelist()
	def total_other_seed_result(self):
		self.total_other_seed_gm = self._calculate_total(self.other_seed_gm, self.other_seed_2)

	@frappe.whitelist()
	def total_wt_of_components_result(self):
		self.total_comp_gm = self._calculate_total(self.total_wt_comp_gm, self.total_wt_comp_2)
	
	@frappe.whitelist()
	def total_wt_of_components(self):
		self.total_wt_comp_gm = self._calculate_total(self.pure_seed_gm, self.inert_matter_gm, self.other_seed_gm)
	
	@frappe.whitelist()
	def total_wt_of_components_test2(self):
		self.total_wt_comp_2 = self._calculate_total(self.pure_seed_2_gm, self.inert_matter_2, self.other_seed_2)
	
	def _calculate_total(self, *values):
		return sum(value for value in values if value is not None)
	

	@frappe.whitelist()
	def total_pure_seed_mean(self):
		self.pure_seed_mean = self._calculate_total_mean(self.pure_seed_percen, self.pure_seed_2_percen)		

	@frappe.whitelist()
	def total_inert_matter_mean(self):
		self.inert_matter_mean = self._calculate_total_mean(self.inert_matter_percen, self.inert_matter_2_percen)
		
	@frappe.whitelist()
	def total_other_seed_mean(self):
		self.other_seed_mean = self._calculate_total_mean(self.other_seed_percen, self.other_seed_2_percen)

	def _calculate_total_mean(self, *values):
		return statistics.mean(value for value in values if value is not None)
	
	@frappe.whitelist()
	def final_result(self):
		self.pure_seed_final=self.pure_seed_mean
		self.inert_matter_final= self.inert_matter_mean
		self.other_seed_final = self.other_seed_mean


	@frappe.whitelist()
	def get_valid_seed_quality_inspections(self):
		seed_quality_inspections = frappe.db.sql("""
			SELECT parent 
			FROM `tabSeed Quality Test Child Table` 
			WHERE test = 'Physical Purity Test';
		""", as_dict=True)

		parent_id_list = []

		for i in seed_quality_inspections:
			parent_id_list.append(i.parent)

		return parent_id_list

	@frappe.whitelist()
	def changes_status(self):
		name = frappe.get_value("Seed Quality Test Child Table", 
							filters={"parent": self.seed_ins_no,"test":self.test_name},
							fieldname=["name"]) 
		frappe.db.set_value('Seed Quality Test Child Table', name, 'status', 'Completed')
		frappe.db.set_value('Seed Quality Test Child Table', name, 'result', self.result)
	
		