# Copyright (c) 2023, tejal and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document

class FoundationSeed(Document):
	pass
	
	# @frappe.whitelist()
	# def get_fertilizer_data(self):
	# 		doc = frappe.get_value("Item", 
	# 						filters={"item_name": self.crop,"item_group":"Seed Category","crop_variety":self.crop_variety},
	# 						fields=["stock_uom"],)
		
			
	# 			# for d in doc:
	# 			# 	self.append('Foundation Seed', {
	# 			# 								"uom":d.stock_uom,})
					
	# 			self.