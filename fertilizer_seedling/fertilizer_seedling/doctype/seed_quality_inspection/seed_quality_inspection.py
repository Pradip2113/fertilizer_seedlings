# Copyright (c) 2023, tejal and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class SeedQualityInspection(Document):

	# @frappe.whitelist()
	# def get_Result(self):
	# 	for minmax in self.get("quality"):
	# 		if(minmax.minimum  and  minmax.present and minmax.maximum ):
	# 			if (minmax.minimum <= minmax.present) and (minmax.present <= minmax.maximum ):
	# 				minmax.result = 'Pass'

	# 			else :
	# 				minmax.result = 'Fail'

		# frappe.msgprint('hiiiii')
    

	@frappe.whitelist()
	def get_checked_test(self):	
		entry = frappe.get_all("Test Information Child Table", 
							filters={"parent": self.define_test},
							fields=["test","check"])  
		for e in entry:
			if e.check:	
				self.append('test_information',{	
										"test":e.test,	
										"status":"On-Processing"						
					})			

	@frappe.whitelist()
	def changes_status(self):
		name = frappe.get_value("Seed Procurement", 
							filters={"name": self.lot_number},
							fieldname=["name"]) 
		frappe.db.set_value('Seed Procurement', name, 'lot_status', self.select_status_of_lot)
		
		

	