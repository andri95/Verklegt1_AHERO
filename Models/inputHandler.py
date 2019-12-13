from Models.airplaneData import AirplaneData
from Models.destinationData import DestinationData
from Models.staffData import StaffData
from Models.voyageData import VoyageData
from Models.errorHandler import ErrorHandler
import datetime

class InputHandler:
    '''The reason for the InputHandler class is to take the load of from the UI classes. The methods that are called
     in multiple different methods. When the user inputs the information then we call the error handler to validate the information.
     When the information has been validated then we return the information as a instance of the correct model'''
    def __init__(self):
        self.errorObject = ErrorHandler()

    def addNewAirplaneIH(self):
        planeID = input("\nEnter airplane ID: ")
        types = input("Enter Airplane type: ")
        model = input("Enter Model name: ")
        capacity = input("Enter Airplane Capacity: ")
        newAirplane = AirplaneData(planeID, types, model, capacity)
        errorChecked = self.errorObject.addNewAirplaneEH(newAirplane)
        return errorChecked

    def addNewDestinationIH(self):
        country = input('Enter country: ')
        flighttime = input('Enter flight duration (hrs): ')
        contact = input('Enter contact: ')
        emergencynum = input('Enter emergency number: ')
        destinationId = ''
        newDestination = DestinationData(country, flighttime, contact, emergencynum, destinationId)
        errorChecked = self.errorObject.addNewDestinationEH(newDestination)
        return errorChecked

    def addNewFlightIH(self):
        arrivingAt = ""
        flightNumber = ""
        departingFrom = ""
        date = input("When will you be flying (YYYY-MM-DD): ").lower()
        time = input("At what hour (HH:MM): ") +":00"
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
        role = input('Enter role: ').lower()
        rank = input('Enter rank: ').lower()
        license_str = ""
        newEmployee = StaffData(ssn, name, address, cellPhone, phoneNumber, email, role, rank, license_str)
        errorChecked = self.errorObject.addNewStaffEH(newEmployee)
        return errorChecked

    def updateDestinationIH(self, destinationObject_dict):
        user_input = input('Choose destination: ')
        destToChange = self.errorObject.availebleDestinationsEH(user_input, destinationObject_dict)
        newContact = input('New contact name: ')
        newEmergencyNumber = input('New emergency number: ')
        errorCheckedContact, errorCheckedEmergency = self.errorObject.errorCheckDestinationEH(newContact, newEmergencyNumber)
        dataList = [destToChange.getCountry(), errorCheckedContact, errorCheckedEmergency]
        return dataList
        
    def updateVoyageIH(self, staff_list, pilotObject_list, cabinCrewObject_list, staffObject_list):
        errorChecked = self.errorObject.addStaffToVoyageEH(staff_list, pilotObject_list, cabinCrewObject_list, staffObject_list)
        return errorChecked

    def addLicenseIH(self, pilotObject_dict):
        flag = True
        while flag:
            user_input = input('Choose a pilot: ')
            if user_input in pilotObject_dict:
                newLicense = input('Enter new airplane type: ')
                dataList = [pilotObject_dict[user_input].getSSN(), newLicense]
                flag = False
            else:
                print('Invalid input!')
                continue
        return dataList

    def workWeekIH(self):
        flag = True
        while flag:
            input_date = input("Enter desired date 'YYYY-MM-DD': ")
            if self.errorObject.errorCheckDateEH(input_date):
                flag = False
            else:
                continue
        dateSplit = input_date.split('-')
        dateObject = datetime.datetime(int(dateSplit[0]), int(dateSplit[1]), int(dateSplit[2]))
        return dateObject


