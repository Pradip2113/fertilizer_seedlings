# Copyright (c) 2023, tejal and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
import re
class Farmer(Document):
	
	def before_save(self):

		mobile = self.contact
		mobile_pattern = re.compile(r'^[6789]\d{9}$')

		if not mobile_pattern.match(mobile):
			frappe.throw('Please enter a valid Indian mobile number.')

		# aadhar = self.farmer_aadhar_number
		# aadhar_pattern = re.compile(r'^[2-9]{1}[0-9]{3}\\s[0-9]{4}\\s[0-9]{4}$')            

		# if not aadhar_pattern.match(aadhar):
		# 	frappe.throw('Please enter a valid Aadhar number.')