from Models.airplaneData import AirplaneData
from Models.destinationData import DestinationData
from Models.voyageData import VoyageData
from Models.staffData import StaffData
import datetime

'''The ErrorHandler class is solely used for error handling the various user inputs in the software'''
class ErrorHandler:

    def addNewAirplaneEH(self, other):
        planeID = other.getPlaneId()
        planeIDValid = ErrorHandler().isOnlyNumbersOrLetters(planeID)
        if planeIDValid == False:
            print("\nInvalid plane ID, please try again.")
            flag = True
            while flag:
                planeID = input('Enter new plane ID: ')
                planeIDValid = ErrorHandler().isOnlyNumbersOrLetters(planeID)
                if planeIDValid:
                    other.setSSN(planeID)
                    flag = False

        type = other.getType()
        if type.isalpha() == False:
            print("\nInvalid airplane type, please try again.")
            flag = True
            while flag:
                type = input('Enter new airlpane type: ')
                if type.isalpha():
                    other.setType(type)
                    flag = False

        model = other.getModel()
        if model.isalnum() == False:
            print("\nInvalid model, please try again.")
            flag = True
            while flag:
                model = input('Enter new model name: ')
                if model.isalnum():
                    other.setModel(model)
                    flag = False

        capacity = other.getCapacity()
        if capacity.isdigit() == False:
            print("\nInvalid capacity, please try again.")
            flag = True
            while flag:
                capacity = input('Enter new capacity: ')
                if capacity.isdigit():
                    other.setCapacity(capacity)
                    flag = False
        return other


    def addNewDestinationEH(self, other):
        country = other.getCountry()
        if country.isalpha() == False:
            print("\nInvalid country, please try again.")
            flag = True
            while flag:
                country = input('Enter new country: ')
                if country.isalpha():
                    other.setCountry(country)
                    flag = False

        flightTime = other.getFlightTime()
        if flightTime.isdigit() == False:
            print("\nInvalid flight time, please try again.")
            flag = True
            while flag:
                flightTime = input('Enter new flight time: ')
                if flightTime.isdigit():
                    other.setFlightTime(flightTime)
                    flag = False

        contact = other.getContact()
        contactValid = ErrorHandler().isNameValid(contact)
        if contactValid == False:
            print("\nInvalid contact, please try again.")
            flag = True
            while flag:
                contact = input('Enter new contact: ')
                contactValid = ErrorHandler().isNameValid(contact)
                if contactValid:
                    other.setContact(contact)
                    flag = False

        emergencynum = other.getEmergencyNumber()
        if emergencynum.isdigit() == False or len(emergencynum) != 7:
            print("\nInvalid emergency number, please try again.")
            flag = True
            while flag:
                emergencynum = input('Enter new emergency number: ')
                if emergencynum.isdigit() and len(emergencynum) == 7:
                    other.setEmergencyNumber(emergencynum)
                    flag = False
        return other

    def addNewStaffEH(self, other):
        SSN = other.getSSN()
        if SSN.isdigit() == False or len(SSN) != 10:
            flag = True
            while flag:
                print("\nInvalid social security number, must be 10 digits.")
                newSSN = input('Enter new SSN: ')
                if newSSN.isdigit() and len(newSSN) == 10:
                    other.setSSN(newSSN)
                    flag = False
                else:
                    continue

        name = other.getName()
        nameValid = self.isNameValid(name)
        if nameValid == False:
            flag = True
            while flag:
                print("\nInvalid name, can not include non alphabetical letters.")
                newName = input('Enter new name: ')
                nameValid = self.isNameValid(newName)
                if nameValid:
                    other.setName(newName)
                    flag = False
                else:
                    continue

        address = other.getAddress()
        addressValid = self.isAddressValid(address)
        if addressValid == False:
            flag = True
            while flag:
                print("\nInvalid address, example address: 'Marylane 85.'")
                newAddress = input('Enter new address: ')
                addressValid = self.isAddressValid(newAddress)
                if addressValid:
                    other.setAddress(newAddress)
                    flag = False
                else:
                    continue

        cellPhone = other.getCellPhone()
        if cellPhone.isdigit() == False or len(cellPhone) != 7:
            flag = True
            while flag:
                print("\nInvalid cellphone, must be 7 digits.")
                newCellPhone = input('Enter new cellphone number: ')
                if newCellPhone.isdigit() and len(newCellPhone) == 7:
                    other.setCellPhone(newCellPhone)
                    flag = False
                else:
                    continue
        phoneNumber = other.getPhoneNumber()
        if phoneNumber.isdigit() == False or len(cellPhone) != 7:
            flag = True
            while flag:
                print("\nInvalid phone number, must be 7 digits.")
                newPhone = input('Enter new phone number: ')
                if newPhone.isdigit() and len(newPhone) == 7:
                    other.setPhoneNumber(newPhone)
                    flag = False
                else:
                    continue
        email = other.getEmail()
        emailValid = ErrorHandler().isEmailValid(email)
        if emailValid == False:
            flag = True
            while flag:
                print("\nInvalid email, must end with: '@nanair.com'.")
                newEmail = input('Enter new email: ')
                emailValid = ErrorHandler().isEmailValid(newEmail)
                if emailValid:
                    other.setEmail(newEmail)
                    flag = False
                else:
                    continue
        role = other.getRole().lower()
        if role not in ["pilot", "cabincrew"]:
            flag = True
            while flag:
                print("\nInvalid role, role can be 'pilot' or 'cabincrew'.")
                newRole = input('Enter new role: ').lower()
                if newRole in ["pilot", "cabincrew"]:
                    other.setRole(newRole)
                    flag = False
                else:
                    continue

        rank = other.getRank().lower()
        if rank not in ["captain", "copilot", "flight service manager", "flight attendant"]:
            flag = True
            while flag:
                print("\nInvalid rank, rank can be 'captain', 'copilot', 'flight service manager' or 'flight attendant'.")
                newRank = input('Enter new rank: ').lower()
                if newRank in ["captain", "copilot", "flight service manager", "flight attendant"]:
                    other.setRank(newRank)
                    flag = False
                else:
                    continue
        return other

    def addStaffToVoyageEH(self, staff_list, pilotObject_list, cabinCrewObject_list, staffObject_list):
        captain_list = []
        copilot_list = []
        fsm_list = []
        fa_list = []
        updatedStaffSSN = []
        for pilot in pilotObject_list:
            if pilot.getRank() == 'captain':
                captain_list.append(pilot.getName())
            elif pilot.getRank() == 'copilot':
                copilot_list.append(pilot.getName())
        for flightAttendant in cabinCrewObject_list:
            if flightAttendant.getRank() == 'flight service manager':
                fsm_list.append(flightAttendant.getName())
            elif flightAttendant.getRank() == 'flight attendant':
                fa_list.append(flightAttendant.getName())

        if staff_list[0] not in captain_list:
            flag = True
            while flag:
                print(staff_list[0] + ' is not a captain!')
                newCaptain = input('Enter new captain: ')
                if newCaptain in captain_list:
                    staff_list[0] = newCaptain
                    flag = False
                else:
                    continue

        if staff_list[1] not in copilot_list:
            flag = True
            while flag:
                print(staff_list[1] + ' is not a copilot!')
                newCopilot = input('Enter new copilot: ')
                if newCopilot in copilot_list:
                    staff_list[1] = newCopilot
                    flag = False
                else:
                    continue

        if staff_list[2] not in fsm_list:
            flag = True
            while flag:
                print(staff_list[2] + ' is not a flight service manager!')
                newFsm = input('Enter new flight service manager: ')
                if newFsm in fsm_list:
                    staff_list[3] = newFsm
                    flag = False
                else:
                    continue

        if staff_list[3] not in fa_list:
            flag = True
            while flag:
                print(staff_list[3] + ' is not a flight attendant!')
                newFa = input('Enter new flight attendant: ')
                if newFa in fa_list:
                    staff_list[3] = newFa
                    flag = False
                else:
                    continue

        for staffMember in staffObject_list:
            if staffMember.getName() in staff_list:
                updatedStaffSSN.append(staffMember.getSSN())
        return updatedStaffSSN

    def getStaffByIdEH(self, user_input, staffObject_dict):
        if user_input in staffObject_dict:
            flag = False
            return staffObject_dict[user_input]
        else:
            flag = True
            while flag:
                print('Invalid input!')
                newUser_input = input('Choose an employee: ')
                if newUser_input in staffObject_dict:
                    flag = False
                    return staffObject_dict[newUser_input]
                else:
                    continue

    def availableDatesEH(self, user_input, availableDates_dict):
        if user_input in availableDates_dict:
            flag = False
            return availableDates_dict[user_input]
        else:
            flag = True
            while flag:
                print('Invalid input!')
                newUser_input = input('Choose date: ')
                if newUser_input in availableDates_dict:
                    flag = False
                    return availableDates_dict[newUser_input]
                else:
                    continue

    def availebleDestinationsEH(self, user_input, destinationObject_dict):
        if user_input in destinationObject_dict:
            flag = False
            return destinationObject_dict[user_input]
        else:
            flag = True
            while flag:
                print('Invalid input!')
                newUser_input = input('Choose date: ')
                if newUser_input in destinationObject_dict:
                    flag = False
                    return destinationObject_dict[newUser_input]
                else:
                    continue

    def errorCheckDestinationEH(self, contact, emergencynum):
        contactValid = self.isNameValid(contact)
        if contactValid == False:
            print("\nInvalid contact, please try again.")
            flag = True
            while flag:
                contact = input('Enter new contact: ')
                contactValid = self.isNameValid(contact)
                if contactValid:
                    flag = False

        if emergencynum.isdigit() == False or len(emergencynum) != 7:
            print("\nInvalid emergency number, please try again.")
            flag = True
            while flag:
                emergencynum = input('Enter new emergency number: ')
                if emergencynum.isdigit() and len(emergencynum) == 7:
                    flag = False

        return contact, emergencynum

    def errorCheckDateEH(self, date):
        errorMessageDate = "Date was not entered correctly (YYYY-MM-DD), please try again "
        try:
            year, month, day = date.split("-")
            temp = datetime.date(int(year), int(month), int(day))
            if len(year) != 4:
                print(errorMessageDate)
                return False
        except ValueError:
            print(errorMessageDate)
            return False
        try:
            temp = datetime.date(int(year), int(month), int(day))
        except TypeError:
            print(errorMessageDate)
            return False
        return True


    def errorCheckTimeEH(self, time):
        errorMessageTime = "Time was not entered correctly (HH:MM), please try again"
        try:
            hour, minute = time.split(":")
            temp = datetime.time(int(hour), int(minute))
        except ValueError:
            print(errorMessageTime)
            return False
        try:
            temp = datetime.time(int(hour), int(minute))
        except TypeError:
            print(errorMessageTime)
            return False
        return True

    def isOnlyNumbersOrLetters(self, other):
        """ Returns False if the string contains only letters or only numbers."""
        #print("in isOnlyNumberOrLetters")
        if other.isdigit():
            return False
        elif other.isalpha():
            return False
        else:
            return True

    def isNameValid(self, other):
        """ Returns false if any letter in the name is not from the alphabet. """
        for word in other.split():
            if word.isalpha() == False:
                return False
        return True

    def isAddressValid(self, other):
        address = other.split()
        if len(address) == 2:
            if address[0].isalpha() == False or address[1].isdigit() == False:
                return False
        return True

    def isEmailValid(self, other):
        if other[-11:] == "@nanair.com":
            return True
        else:
            return False

