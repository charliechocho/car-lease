#!/usr/bin/python

from PyQt5.QtCore import 

now = QDateTime.currentDateTime()

print("Local Date and Time: ", now.toString(Qt.ISODate))
print("UTC Date and Time: ", now.toUTC().toString(Qt.ISODate))


print(f"\nThe offset between Local and UTC is: {now.offsetFromUtc()} seconds")

