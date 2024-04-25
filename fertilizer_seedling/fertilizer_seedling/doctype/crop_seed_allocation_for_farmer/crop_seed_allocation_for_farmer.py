# Copyright (c) 2023, tejal and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class CropSeedAllocationForFarmer(Document):
	
	@frappe.whitelist()
	def get_fertilizer_data(self):
		if self.batch_id:
			doc = frappe.get_all("Fertilizer Child Table", 
							filters={"parent": self.batch_id},
							fields=["fertilizer_name","quantity","days_after_plantation"],)

			
			
			Pesticide = frappe.get_all("Pesticide Child Table", 
							filters={"parent": self.batch_id},
							fields=["pesticide_name","quantity","days_after_plantation"],)
			
			Internal = frappe.get_all("Internal Operation Child Table", 
							filters={"parent": self.batch_id},
							fields=["operation_name","time"],)
			
			if(doc):
				for d in doc:
					self.append('fertilizers', {
												"fertilizer_name":d.fertilizer_name,
												"quantity":d.quantity,
												"days_after_plantation":d.days_after_plantation })
					
			if(Pesticide):
				for d in Pesticide:
					self.append('pesticides', {
												"pesticide_name":d.pesticide_name,
												"quantity":d.quantity,
												"days_after_plantation":d.days_after_plantation })
					
			if(Internal):
				for d in Internal:
					self.append('internal_operations', {
												"operation_name":d.operation_name,
												"time":d.time })

			# doc.crop_seed_allocation_id=self.name

	@frappe.whitelist()
	def get_Allocated_Seed_Price(self):
		self.allocated_seed_cost_price = self.allocated_seed * self.cost_price_kg
		return self.allocated_seed_cost_price