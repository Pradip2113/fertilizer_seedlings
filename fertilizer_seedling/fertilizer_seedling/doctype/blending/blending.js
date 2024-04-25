// Copyright (c) 2024, tejal and contributors
// For license information, please see license.txt

frappe.ui.form.on('Blending', {
	// refresh: function(frm) {

	// }
});



frappe.ui.form.on('Blending', {
	get_available_lot_no: function(frm) {
		frm.clear_table("blending_child_table");
		frm.refresh_field('blending_child_table');
		frm.call({
			method:'get_lot_info',
			doc:frm.doc
		})
	}
});





frappe.ui.form.on('Blending', {
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




// frappe.ui.form.on('Blending', {
//     setup: function(frm) {
//         frm.set_query("crop_name", function(doc) {
//                 return {
//                     filters: [
//                         ['Item Group', 'parent_item_group', '=', "Seed Category"],
//                     ]
//                 };
//         });
//     },
// });



frappe.ui.form.on('Blending', {
    setup: function(frm) {
        frm.set_query("crop_variety", function(doc) {
            if (frm.doc.crop_name) {
                return {
                    filters: [
                        ['Item', 'crop', '=', frm.doc.crop_name],
                    ]
                };
            } else {
                // If no crop_type selected, show all crop_name
                return {};
            }
        });
    },
});

