from staffData import StaffData
import staffData
#from staffLL import StaffLL

import csv

class StaffIO:

    def __init__(self):
        self.path = 'Crew.csv'

    def getAllStaffIO(self):

        file = open(self.path, 'r')
        reader = csv.DictReader(file)
        staffList = []
        for row in reader:
            staffList.append(StaffData(row['ssn'], row['name'], row['role'], row['rank'], row['licence']))

        for employee in staffList:
            print('Ssn: {}, Name: {}, Role: {}, Rank: {}, Licence: {}'.format(employee.SSN, employee.name, employee.role, employee.rank, employee.license))

