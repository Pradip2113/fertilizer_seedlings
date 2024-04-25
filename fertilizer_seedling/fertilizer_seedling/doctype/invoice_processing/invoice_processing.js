// Copyright (c) 2024, tejal and contributors
// For license information, please see license.txt

frappe.ui.form.on('Invoice Processing', {
	// refresh: function(frm) {

	// }
});

frappe.ui.form.on('Invoice Processing', {
	to_date: function(frm) {
		frm.clear_table("select_organizer");
		// frm.refresh_field('select_organizer');
		frm.call({
			method:'get_all_supplier',
			doc:frm.doc
		})
	}
});


frappe.ui.form.on('Invoice Processing', {
	get_lot_details: function(frm) {
		frm.clear_table("invoice");
		frm.refresh_field('invoice');
		frm.call({
			method:'get_lot_and_farmer_details',
			doc:frm.doc
		})
	}
});

frappe.ui.form.on('Invoice Processing', {
	select_all: function(frm) {
		frm.call({
			method:'checkall',
			doc:frm.doc
		})
	}
});

frappe.ui.form.on('Invoice Processing', {
	check_all: function(frm) {
		frm.call({
			method:'selectall',
			doc:frm.doc
		})
	}
});

