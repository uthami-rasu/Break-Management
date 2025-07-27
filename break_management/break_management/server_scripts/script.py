from datetime import datetime, timedelta
import frappe 



def find_prev_monday(date):

    # date.weekday(): Monday = 0, Sunday = 6

    days_to_monday = date.weekday()
    prev_monday = date - timedelta(days=days_to_monday)

    return prev_monday.date()




def before_insert(doc,method):
    
    week_start = find_prev_monday(datetime.now())

    week_end = week_start + timedelta(days=6)


    doc.week_start_date = week_start
    doc.week_end_date = week_end




def seconds_to_hhmmss(seconds):
    hours, remainder = divmod(int(seconds), 3600)
    minutes, seconds = divmod(remainder, 60)
    return f"{hours:02}:{minutes:02}:{seconds:02}"

def on_update(doc, method):
    total_break = 0  # in seconds

    for rec in doc.break_timing_records:
        if rec.entry_time and rec.exit_time:
            start = datetime.strptime(rec.entry_time, "%H:%M:%S")
            end = datetime.strptime(rec.exit_time, "%H:%M:%S")

            time_taken = (end - start).total_seconds()
            rec.time_taken_in_minutes = seconds_to_hhmmss(time_taken)

            total_break += time_taken

    doc.total_break_time = seconds_to_hhmmss(total_break)
