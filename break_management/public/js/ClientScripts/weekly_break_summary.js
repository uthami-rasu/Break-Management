frappe.ui.form.on('BreakRecords', {
    date: function (frm, cdt, cdn) {
        let row = locals[cdt][cdn];
        let selected_date = row.date;
        let today = frappe.datetime.get_today();

        if (!selected_date) return;

        // 1. Must be today
        if (selected_date !== today) {
            frappe.msgprint("Date must be today's date.");
            frappe.model.set_value(cdt, cdn, "date", "");
            return;
        }

        // 2. Must be within parent start and end of week
        let week_start = frm.doc.week_start_date;
        let week_end = frm.doc.week_end_date;

        if (!week_start || !week_end) {
            frappe.msgprint("Please ensure both Week Start Date and Week End Date are set in the parent form.");
            frappe.model.set_value(cdt, cdn, "date", "");
            return;
        }

        if (
            selected_date < week_start ||
            selected_date > week_end
        ) {
            frappe.msgprint(`Date must be within the week (${week_start} to ${week_end}).`);
            frappe.model.set_value(cdt, cdn, "date", "");
        }


        console.log("log")
    }
});


