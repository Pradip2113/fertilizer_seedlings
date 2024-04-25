// Copyright (c) 2023, tejal and contributors
// For license information, please see license.txt

frappe.ui.form.on('Seed Quality Inspection', {
	// refresh: function(frm) {

	// }
});

frappe.ui.form.on('Seed Quality Inspection', {
	farmer_id: function(frm) {
            frm.clear_table("test_information");
            frm.refresh_field('test_information');
			frm.doc.define_test=null
			frm.refresh_field('define_test');
	}
});


frappe.ui.form.on('Seed Quality Inspection', {
    setup: function(frm) {
        frm.set_query("define_test", function(doc) {
            if (frm.doc.farmer_name && frm.doc.plot_number) {
                return {
                    filters: [
                        ['Define Test', 'farmer_name', '=', frm.doc.farmer_name],
						['Define Test', 'plot_number', '=', frm.doc.plot_number],
                        ['Define Test', 'lot_number', '=', frm.doc.lot_number],
                        
                    ]
                };
            } else {
                return {};
            }
        });
    },
});


frappe.ui.form.on('Seed Quality Inspection', {
	define_test: function(frm) {
		frm.clear_table("test_information");
		frm.refresh_field('test_information');
		frm.call({
			method:'get_checked_test',
			doc:frm.doc
		})
	}
});


frappe.ui.form.on('Seed Quality Test Child Table', {
    go_to_test: function(frm, cdt, cdn) {
        var child = locals[cdt][cdn];

        var testFormMapping = {
            "Grow Out Test": "Grow Out Test",
            "Physical Purity Test": "Physical Purity Test",
            "Seed Health Test": "Seed Health Test",
            "Virus Test": "Virus Test",
            "Moisture Test":"Moisture Test",
            "Germination Test":"Germination Test",
        };

        var selectedTest = child.test;

        if (testFormMapping[selectedTest]) {
            frappe.set_route("Form", testFormMapping[selectedTest]);
        }
    }
});


// frappe.ui.form.on("Seed Quality Test Child Table", "go_to_test", function(frm) {
//     frappe.set_route("Form", self.test);
//   });
  

// frappe.ui.form.on('Seed Quality Inspection', {
//     refresh: function(frm) {
//         frm.fields_dict['YourChildTableFieldname'].grid.get_field('test').$input.on('click', function(event) {
//             var selectedTest = $(this).text();
//             var associatedDoctype = frm.doc.YourChildTableFieldname[$(this).closest('tr').attr('data-idx')].YourTargetDoctypeFieldname;

//             // Redirect to the associated doctype
//             frappe.set_route("Form", associatedDoctype, { "test": selectedTest });
//         });
//     }
// });

// frappe.ui.form.on('Seed Quality Inspection', {
//     after_save: function (frm) {
//         // Triggered after the document is saved
//         frm.fields_dict['define_test_id'].df.read_only = 1;
//     }
// });


// frappe.ui.form.on('Seed Quality Inspection', {
//     after_save: function (frm) {
//         // Triggered after the document is saved
//         frm.fields_dict['define_test_id'].df.read_only = 1;
//     }
// });

frappe.ui.form.on('Seed Quality Inspection', {
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