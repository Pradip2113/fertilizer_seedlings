// Copyright (c) 2024, tejal and contributors
// For license information, please see license.txt

frappe.ui.form.on('Seed Procurement', {
	// refresh: function(frm) {

	// }
});


// frappe.ui.form.on('Seed Procurement', {
//     empty_weight: function(frm) {
//         var selectedSeedProcurementId = frm.doc.name;
//         frm.set_value('batch', selectedSeedProcurementId);
//     }
// });


// frappe.ui.form.on('Seed Procurement', {
// 	empty_weight: function(frm) {
// 		if(frm.doc.loaded_weight != null && frm.doc.empty_weight != null){
// 		frm.call({
// 			method:'calculate_lot_weight',
// 			doc:frm.doc
// 		})
// }
// else{
// 	frappe.throw('Please Enter Loaded Weight First !')
// }
// }
// });

frappe.ui.form.on('Seed Procurement', {
	empty_weight: function(frm) {
		
		frm.call({
			method:'calculate_lot_weight',
			doc:frm.doc
		})
}
});


// frappe.ui.form.on('Seed Procurement', {
//     after_save: function(frm) {
//         frappe.call({
//             method: 'set_batch_id',
//             doc: frm.doc,
          
//         });
//     }
	
// });




