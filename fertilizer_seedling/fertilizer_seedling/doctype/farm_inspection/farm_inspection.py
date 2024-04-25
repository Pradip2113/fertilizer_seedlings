# Copyright (c) 2023, tejal and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class FarmInspection(Document):
	@frappe.whitelist()
	def get_fertilizer_data(self):
		if self.crop_seed_allocation_id:
			doc = frappe.get_all("Fertilizer Child Table", 
							filters={"parent": self.crop_seed_allocation_id},
							fields=["fertilizer_name","quantity","days_after_plantation"],)
			
			Pesticide = frappe.get_all("Pesticide Child Table", 
							filters={"parent": self.crop_seed_allocation_id},
							fields=["pesticide_name","quantity","days_after_plantation"],)
			
			Internal = frappe.get_all("Internal Operation Child Table", 
							filters={"parent": self.crop_seed_allocation_id},
							fields=["operation_name","time"],)
			
			# frappe.msgprint('hiiii')	

			if(doc):
				for d in doc:
					self.append('fertilizer', {
												"fertilizer_name":d.fertilizer_name,
												"quantity":d.quantity,
												"days_after_plantation":d.days_after_plantation })
					
			if(Pesticide):
				for d in Pesticide:
					self.append('pesticide', {
												"pesticide_name":d.pesticide_name,
												"quantity":d.quantity,
												"days_after_plantation":d.days_after_plantation })
					
			if(Internal):
				for d in Internal:
					self.append('operation', {
												"operation_name":d.operation_name,
												"time":d.time })

			# doc.farm_inspection_id=self.name