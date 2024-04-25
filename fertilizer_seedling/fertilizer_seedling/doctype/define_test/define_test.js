// Copyright (c) 2024, tejal and contributors
// For license information, please see license.txt

frappe.ui.form.on('Define Test', {
	// refresh: function(frm) {

	// }
});



frappe.ui.form.on('Define Test', {
	refresh: function(frm) {
		frm.call({
			method:'fixed_child_entries',
			doc:frm.doc
		})
	}
});



frappe.ui.form.on('Define Test', {
	select_all: function(frm) {
		frm.call({
			method:'checkall',
			doc:frm.doc
		})
	}
});


frappe.ui.form.on('Define Test', {
    seed_procurement_id: function(frm) {
        var selectedSeedProcurementId = frm.doc.seed_procurement_id;
        frm.set_value('lot_number', selectedSeedProcurementId);
    }
});



frappe.ui.form.on('Define Test', {
    after_save: function(frm) {
        // Call server-side method after saving
        frappe.call({
            method: 'changes_status',
            doc: frm.doc,
            callback: function(response) {
                // Handle the response here
                if (response.message) {
                    console.log(response.message);
                }
            }
        });
    }
	
});
