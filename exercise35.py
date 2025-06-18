from datetime import date, datetime

today = date.today()
new_year = date(today.year + 1, 1, 1)
days_left = (new_year - today).days

print("Today's date:", today)
print("Day of the week:", today.strftime("%A"))
print("Days until New Year:", days_left)
