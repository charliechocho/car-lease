#!/usr/bin/python
from PyQt5.QtCore import QDate, Qt


km_to_date = input("Vad är mätarställningen nu? ")
today = QDate.currentDate()
c = {'blue':'\033[34m', 'green':'\033[32m', 'cyan':'\033[36m',
'yellow':'\033[93m', 'pink':'\033[95m', 'red':'\033[31m'}

lease_date = QDate(2020, 10, 3)
lease_return = QDate(2023,10,3)
total_days = lease_date.daysTo(lease_return)
dayspassed = lease_date.daysTo(today)
allowed_daily_mileage = (60000/int(total_days))
allowed_total_mileage = '{0:.0f}'.format(float(allowed_daily_mileage) * int(dayspassed))
balance = int(km_to_date) - float(allowed_total_mileage)

print(c['green'], f"\nStart of Car Lease for BMW SCN 96U: {c['pink']}2020-10-03")
print(c['green'], f"\nTotal allowed daily mileage (km): {c['pink']}{'{0:.2f}'.format(allowed_daily_mileage)}\n")
print(c['green'], f"\nTotal lease days in contract: {c['pink']}{total_days}")
print(c['green'], f"\nDays since Car pick up: {c['pink']}{dayspassed}")
print(c['green'], f"\nAllowed mileage up until now (km): {c['pink']}{allowed_total_mileage}")
print(c['green'], f"\nDays left until Car return: {c['pink']}{today.daysTo(lease_return)}")

if int(balance) < 0:
    print(c['green'], f"\nYou're OK on the mileage: {c['pink']}{balance}")
else:
    print(c['green'], f"\nYou're over the allowed mileage: {c['red']}{balance}")

