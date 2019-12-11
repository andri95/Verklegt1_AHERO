from Models.airplaneData import AirplaneData
from Models.destinationData import DestinationData
from Models.staffData import StaffData
from Models.voyageData import VoyageData
import datetime

class InputHandler:

    def addNewAirplaneIH(self):
        planeID = input("Enter airplane ID: ")
        types = input("Enter Airplane type: ")
        model = input("Enter Model name: ")
        capacity = input("Enter Airplane Capacity")
        newAirplane = AirplaneData(planeID, types, model, capacity)
        return newAirplane

    def addNewDestinationIH(self):
        country = input('Enter country: ')
        flighttime = input('Enter flight time: ')
        contact = input('Enter contact: ')
        emergencynum = input('Enter emergency number: ')
        newDestination = DestinationData(country, flighttime, contact, emergencynum)
        return newDestination

    def addNewFlightIH(self):
        arrivingAt = input("Where will you be arriving at: ").lower()
        flightNumber = ""
        departingFrom = input("Where will you be flying from: ").lower()
        date = input("When will you be flying: YYYY-MM-DD : ").lower()
        time = input("At what hour: HH:MM ") +":00"
        departureTime = date + " " + time
        arrivalTime = ""
        aircraftId = ""
        newFlight = VoyageData(flightNumber, departingFrom, arrivingAt , departureTime, arrivalTime , aircraftId)
        return newFlight

    def addNewStaffIH(self):
        ssn = input('Enter social security number: ')
        name = input('Enter name: ')
        address = input('Enter address: ')
        cellPhone = input('Enter cell phone: ')
        phoneNumber = input('Enter phone number: ')
        email = input('Enter email: ')
        role = input('Enter role: ')
        rank = input('Enter rank: ')
        license_str = input('Enter license: ')
        newEmployee = StaffData(ssn, name, address, cellPhone, phoneNumber, email, role, rank, license_str)
        return newEmployee

    def updateDestinationIH(self):
        destToChange = input('Enter country you want to change: ')
        newContact = input('New contact name: ')
        newEmergencyNumber = input('New emergency number: ')
        dataList = [destToChange, newContact, newEmergencyNumber]
        return dataList
        
    def updateVoyageIH(self):
        staff_list = []
        staff_list.append(input("Enter a Captain"))
        staff_list.append(input("Enter a Co-Pilot"))
        staff_list.append(input("Enter a flight attendant: "))
        staff_list.append(input("Enter a flight attendant: "))
        return staff_list

    def addLicenseIH(self):
        ssn = input('Enter social security number: ')
        newLicense = input('Enter new airplane type: ')
        dataList = [ssn, newLicense]
        return dataList

    def workWeekIH(self):
        date = input("Enter desired date 'YYYY-MM-DD: ")
        dateSplit = date.split('-')
        dateObject = datetime.datetime(int(dateSplit[0]), int(dateSplit[1]), int(dateSplit[2]))
        return dateObject