from datetime import datetime, timedelta

start_date = datetime(2023, 1, 1)

end_date = datetime(2023, 12, 31)

free_entry_dates = []

current_date = start_date
while current_date <= end_date:
    current_month = current_date.month
    while current_date.month == current_month:
        if current_date.weekday() == 3 and 15 <= current_date.day <= 21:
            free_entry_dates.append(current_date)
        current_date += timedelta(days=1)

for date in free_entry_dates:
    print(date.strftime('%d.%m.%Y'))
