// Copyright (c) 2024, tejal and contributors
// For license information, please see license.txt

frappe.ui.form.on('Seed Health Test', {
	// refresh: function(frm) {

	// }

	n1: function(frm) {
		if(frm.doc.n1  != null && frm.doc.no1 != null){
		frm.call({
			method:'get_n1_percen',
			doc:frm.doc
		})
		
		}	
},
n2: function(frm) {
	if(frm.doc.n2  != null && frm.doc.no2 != null){
	frm.call({
		method:'get_n2_percen',
		doc:frm.doc
	})
	
	}	
},
n3: function(frm) {
	if(frm.doc.n3  != null && frm.doc.no3 != null){
	frm.call({
		method:'get_n3_percen',
		doc:frm.doc
	})
	
	}	
},
n4: function(frm) {
	if(frm.doc.n4  != null && frm.doc.no4 != null){
	frm.call({
		method:'get_n4_percen',
		doc:frm.doc
	})
	
	}	
},
n5: function(frm) {
	if(frm.doc.n5  != null && frm.doc.no5 != null){
	frm.call({
		method:'get_n5_percen',
		doc:frm.doc
	})
	
	}	
}
});



frappe.ui.form.on('Seed Health Test', {
	non1: function(frm) {
		if(frm.doc.non1  != null && frm.doc.no1 != null){
		frm.call({
			method:'get_pn1_percen',
			doc:frm.doc
		})
		
		}	
}
	
});

frappe.ui.form.on('Seed Health Test', {
	non2: function(frm) {
		if(frm.doc.non2  != null && frm.doc.no2 != null){
		frm.call({
			method:'get_pn2_percen',
			doc:frm.doc
		})
		
		}	
}
	
});

frappe.ui.form.on('Seed Health Test', {
	non3: function(frm) {
		if(frm.doc.non3  != null && frm.doc.no3 != null){
		frm.call({
			method:'get_pn3_percen',
			doc:frm.doc
		})
		
		}	
}
	
});

frappe.ui.form.on('Seed Health Test', {
	non4: function(frm) {
		if(frm.doc.non4  != null && frm.doc.no4 != null){
		frm.call({
			method:'get_pn4_percen',
			doc:frm.doc
		})
		
		}	
}
	
});

frappe.ui.form.on('Seed Health Test', {
	non5: function(frm) {
		if(frm.doc.non5  != null && frm.doc.no5 != null){
		frm.call({
			method:'get_pn5_percen',
			doc:frm.doc
		})
		
		}	
}
	
});



frappe.ui.form.on('Seed Health Test', {
    setup: function(frm) {
        // Call the Python method during setup
        frappe.call({
            method: 'get_valid_seed_quality_inspections',
			doc:frm.doc,
            callback: function(r) {
                if (r.message) {
                    // Assuming your Python method returns an array of parent IDs
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




frappe.ui.form.on('Seed Health Test', {
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
