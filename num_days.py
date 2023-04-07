#!/usr/bin/python
from PyQt5.QtCore import QDate, Qt

today = QDate.currentDate()

lease_date = QDate(2020, 10, 3)
lease_return = Qdate(2023,10,3)

dayspassed = lease_date.daysTo(now)

print(f"\nStart of Car Lease for BMW SCN 96U: {lease_date}")
print(f"\nDays since Car pick up: {dayspassed}")
print(f"\nDays left until Car return: {now.daysTo(lease_return)}")

