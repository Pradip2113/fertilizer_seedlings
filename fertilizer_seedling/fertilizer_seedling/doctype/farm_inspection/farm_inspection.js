// Copyright (c) 2023, tejal and contributors
// For license information, please see license.txt

frappe.ui.form.on('Farm Inspection', {
	// refresh: function(frm) {

	// }
});



frappe.ui.form.on('Farm Inspection', {
	crop_seed_allocation_id: function(frm) {
		frm.clear_table("fertilizer");
		frm.refresh_field('fertilizer');
        frm.clear_table("pesticide");
		frm.refresh_field('pesticide');
        frm.clear_table("operation");
		frm.refresh_field('operation');
		frm.call({
			method:'get_fertilizer_data',
			doc:frm.doc
		})
	}
});




frappe.ui.form.on('Farm Inspection', {
    after_save: function (frm) {
        // Triggered after the document is saved
        frm.fields_dict['crop_seed_allocation_id'].df.read_only = 1;
    }
});