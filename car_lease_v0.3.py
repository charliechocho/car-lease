#!/usr/local/bin/python3
from PyQt5.QtCore import QDate, Qt
from os.path import exists
from datetime import datetime


file_date = datetime.date(datetime.now())
today = QDate.currentDate()
lease_date = QDate(2023, 7, 31)
lease_return = QDate(2028, 7, 31)
dayspassed = lease_date.daysTo(today)
total_days = lease_date.daysTo(lease_return)
allowed_daily_mileage = (125000/int(total_days))
allowed_total_mileage = '{0:.0f}'.format(float(allowed_daily_mileage) * int(dayspassed))



c = {'blue':'\033[34m', 'green':'\033[32m', 'cyan':'\033[36m',
'yellow':'\033[93m', 'pink':'\033[95m', 'red':'\033[31m'}


def check_file():
    if exists('mileage.db'):
        with open('mileage.db', 'r') as f:
            result = f.readline()
            return result
    else:
        print('creating file!')
        with open('mileage.db', 'w') as f:
            f.seek(0)
            f.write('-No Mileage-')
            return '-No Mileage-'

def get_balance(km, allowed):
    try:
        bal = int(km) - float(allowed)
        return bal
    except ValueError:
        print('Did you enter any mileage?')
        quit()

def chk_balance(c, balance):
    if int(balance) < 0:
        print(c['green'], f"\nYou're OK on the mileage: {c['pink']}{balance}")
    else:
        print(c['green'], f"\nYou're over the allowed mileage: {c['red']}{balance}")

def write_km(kilometers, today, balance):
    with open('mileage.db', 'w') as f:
        f.write(f'{kilometers} - {today} (Bal: {balance}')

mileage = check_file()

km_to_date = input(f"What's on the odometer?(Last Entry: {mileage}): ")

balance = get_balance(km_to_date, allowed_total_mileage)

chk_balance(c, balance)

write_km(km_to_date, file_date, balance)


print(c['green'], f"\nStart of Car Lease for BMW FDE 08Z: {c['pink']}2023-07-31")
print(c['green'], f"\nTotal allowed daily mileage (km): {c['pink']}{'{0:.2f}'.format(allowed_daily_mileage)}\n")
print(c['green'], f"\nTotal lease days in contract: {c['pink']}{total_days}")
print(c['green'], f"\nDays since Car pick up: {c['pink']}{dayspassed}")
print(c['green'], f"\nAllowed mileage up until now (km): {c['pink']}{allowed_total_mileage}")
print(c['green'], f"\nDays left until Car return: {c['pink']}{today.daysTo(lease_return)}")

