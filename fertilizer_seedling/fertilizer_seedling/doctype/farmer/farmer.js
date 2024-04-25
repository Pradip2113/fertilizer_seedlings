// Copyright (c) 2023, tejal and contributors
// For license information, please see license.txt

frappe.ui.form.on('Farmer', {
	// refresh: function(frm) {

	// }
});


frappe.ui.form.on('Farmer', {
	setup: function(frm) {
		frm.set_query("district", function(doc) {
			if (frm.doc.state) {
			return {
				filters: [
				    ['District', 'state', '=', frm.doc.state],
				]
			};
		}else{
			return {};
		}
		});
	},
})



frappe.ui.form.on('Farmer', {
	setup: function(frm) {
		frm.set_query("taluka", function(doc) {
			if (frm.doc.district) {
			return {
				filters: [
				    ['Taluka', 'district', '=', frm.doc.district],
				]
			};
		}else{
			return {};
		}
		});
	},
})


frappe.ui.form.on('Farmer', {
	setup: function(frm) {
		frm.set_query("village", function(doc) {
			if (frm.doc.taluka) {
			return {
				filters: [
				    ['Village', 'taluka', '=', frm.doc.taluka],
				]
			};
		}else{
			return {};
		}
		});
	},
})