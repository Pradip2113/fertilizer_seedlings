// Copyright (c) 2024, tejal and contributors
// For license information, please see license.txt

frappe.ui.form.on('Germination Test', {
	// refresh: function(frm) {

	// }
});


frappe.ui.form.on('Germination Test', {
	refresh: function(frm) {
		frm.call({
			method:'fixed_child_entries',
			doc:frm.doc
		})
	}
});

frappe.ui.form.on('Germination Test', {
	refresh: function(frm) {
		frm.call({
			method:'fixed_child',
			doc:frm.doc
		})
	}
});

frappe.ui.form.on('Germination Test', {
	refresh: function(frm) {
		frm.call({
			method:'fixed_child_entri',
			doc:frm.doc
		})
	}
});

frappe.ui.form.on('Germination Test', {
	refresh: function(frm) {
		frm.call({
			method:'fixed',
			doc:frm.doc
		})
	}
});


frappe.ui.form.on('Germination Test', {
    setup: function(frm) {
        frappe.call({
            method: 'get_valid_seed_quality_inspections',
			doc:frm.doc,
            callback: function(r) {
                if (r.message) {
					frm.set_query("seed_q_i_no",function(doc, cdt, cdn) {	    
						let d = locals[cdt][cdn];
						return {
							filters: [
								['Seed Quality Inspection', 'name','in', r.message],     
							]
						};
					});
                }
            }
        });
    }
});


frappe.ui.form.on('Germination Test', {
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
