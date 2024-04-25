// Copyright (c) 2024, tejal and contributors
// For license information, please see license.txt

frappe.ui.form.on('Physical Purity Test', {
	// refresh: function(frm) {

	// }
});


frappe.ui.form.on('Physical Purity Test', {
	pure_seed_gm: function(frm) {
		if(frm.doc.total_gm_test1  != null && frm.doc.pure_seed_gm != null){
		frm.clear_table("pure_seed_percen");
		frm.refresh_field('pure_seed_percen');
		frm.call({
			method:'get_pure_seed_percen',
			doc:frm.doc
		})
}
else{
	return{}
	// frappe.throw('Please Enter Initial Working Sample wt. First !')
}
},

	inert_matter_gm: function(frm) {
		if(frm.doc.total_gm_test1  != null && frm.doc.inert_matter_gm != null){
		frm.clear_table("inert_matter_percen");
		frm.refresh_field('inert_matter_percen');
		frm.call({
			method:'get_inert_matter_percen',
			doc:frm.doc
		})
	}
	else{
		return{}
	// frappe.throw('Please Enter Initial Working Sample wt. First !')
	}
	},

	other_seed_gm: function(frm) {
		if(frm.doc.total_gm_test1  != null && frm.doc.other_seed_gm != null){
		frm.clear_table("other_seed_percen");
		frm.refresh_field('other_seed_percen');
		frm.call({
			method:'get_other_seed_percen',
			doc:frm.doc
		})
	}
	else{
		return{}
	// frappe.throw('Please Enter Initial Working Sample wt. First !')
	}
	},
	pure_seed_2_gm: function(frm) {
		if(frm.doc.total_gm_test2  != null && frm.doc.pure_seed_2_gm != null){
		frm.clear_table("pure_seed_2_percen");
		frm.refresh_field('pure_seed_2_percen');
		frm.call({
			method:'get_pure_seed_2_percen',
			doc:frm.doc
		})
		// frm.call({
		// 	method:'total_pure_seed_gm_result',
		// 	doc:frm.doc
		// });
	}
	else{
		return{}
	// frappe.throw('Please Enter Initial Working Sample wt. First !')
	}
	},
	inert_matter_2: function(frm) {
		if(frm.doc.total_gm_test2  != null && frm.doc.inert_matter_2 != null){
		frm.clear_table("inert_matter_2_percen");
		frm.refresh_field('inert_matter_2_percen');
		frm.call({
			method:'get_inert_matter_2_percen',
			doc:frm.doc
		})
	}
	else{
		return{}
	// frappe.throw('Please Enter Initial Working Sample wt. First !')
	}
	},
	other_seed_2: function(frm) {
		if(frm.doc.total_gm_test2  != null && frm.doc.other_seed_2 != null){
		frm.clear_table("other_seed_2_percen");
		frm.refresh_field('other_seed_2_percen');
		frm.call({
			method:'get_other_seed_2_percen',
			doc:frm.doc
		})
	}
	else{
		return{}
	// frappe.throw('Please Enter Initial Working Sample wt. First !')
	}
	},

});



frappe.ui.form.on('Physical Purity Test', {
    setup: function(frm) {
        // Call the Python method during setup
        frappe.call({
            method: 'get_valid_seed_quality_inspections',
			doc:frm.doc,
            callback: function(r) {
                if (r.message) {
                    // Assuming your Python method returns an array of parent IDs
					frm.set_query("seed_ins_no",function(doc, cdt, cdn) {	    
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




frappe.ui.form.on('Physical Purity Test', {
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
