from Models.airplaneData import AirplaneData
from Models.destinationData import DestinationData
from Models.staffData import StaffData
from Models.voyageData import VoyageData
from Models.errorHandler import ErrorHandler
import datetime

class InputHandler:
    def __init__(self):
        self.errorObject = ErrorHandler()

    def __init__(self):
        self.errorObject = ErrorHandler()

    def addNewAirplaneIH(self):
        planeID = input("\nEnter airplane ID: ")
        types = input("Enter Airplane type: ")
        model = input("Enter Model name: ")
        capacity = input("Enter Airplane Capacity")
        newAirplane = AirplaneData(planeID, types, model, capacity)
        errorChecked = self.errorObject.addNewAirplaneEH(newAirplane)  # Hér byrjar error handler
        return errorChecked

    def addNewDestinationIH(self):
        country = input('Enter country: ')
        flighttime = input('Enter flight duration (hrs): ')
        contact = input('Enter contact: ')
        emergencynum = input('Enter emergency number: ')
        destinationId = ''
        newDestination = DestinationData(country, flighttime, contact, emergencynum, destinationId)
        errorChecked = self.errorObject.addNewDestinationEH(newDestination)  # Hér byrjar error handler
        return errorChecked

    def addNewFlightIH(self):
        arrivingAt = input("Where will you be arriving at: ").lower()
        flightNumber = ""
        departingFrom = ""
        date = input("When will you be flying: YYYY-MM-DD : ").lower()
        print("Note, NanAir only flies only by the hour (13:00, 02:00)")
        time = input("At what hour: HH:MM ") +":00"
        departureTime = date + "T" + time
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
        errorChecked = self.errorObject.addNewStaffEH(newEmployee)
        print('New staff member registered!')
        return errorChecked

    def updateDestinationIH(self):
        destToChange = input('Enter country you want to change: ')
        newContact = input('New contact name: ')
        newEmergencyNumber = input('New emergency number: ')
        dataList = [destToChange, newContact, newEmergencyNumber]
        return dataList
        
    def updateVoyageIH(self, staff_list, pilotObject_list, cabinCrewObject_list, staffObject_list):
        errorChecked = self.errorObject.addStaffToVoyageEH(staff_list, pilotObject_list, cabinCrewObject_list, staffObject_list)
        return errorChecked

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