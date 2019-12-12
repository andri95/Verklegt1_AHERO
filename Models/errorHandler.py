from Models.airplaneData import AirplaneData
from Models.destinationData import DestinationData
from Models.voyageData import VoyageData
from Models.staffData import StaffData


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
        return True

    def addNewStaffEH(self, other):
        SSN = other.getSSN()
        if SSN.isdigit() == False or len(SSN) != 10:
            flag = True
            while flag:
                print("\nInvalid social security number, please try again.")
                newSSN = input('Enter new SSN: ')
                if SSN.isdigit() and len(SSN) == 10:
                    other.setSSN(newSSN)
                    flag = False
                else:
                    continue

        name = other.getName()
        nameValid = self.isNameValid(name)
        if nameValid == False:
            flag = True
            while flag:
                print("\nInvalid name, please try again.")
                newName = input('Enter new name: ')
                nameValid = self.isNameValid(name)
                if nameValid:
                    other.setName(newName)
                    flag = False
                else:
                    continue

        address = other.getAddress()
        if address.isalnum() == False:
            flag = True
            while flag:
                print("\nInvalid address, please try again.")
                newAddress = input('Enter new address: ')
                if address.isalnum():
                    other.setAddress(newAddress)
                    flag = False
                else:
                    continue
        cellPhone = other.getCellPhone()
        if cellPhone.isdigit() == False or len(cellPhone) != 7:
            flag = True
            while flag:
                print("\nInvalid cellphone, please try again.")
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
                print("\nInvalid phone number, please try again.")
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
                print("\nInvalid email, please try again.")
                newEmail = input('Enter new email: ')
                emailValid = ErrorHandler().isEmailValid(newEmail)
                if emailValid:
                    other.setEmail(newEmail)
                    flag = False
                else:
                    continue
        role = other.getRole()
        if role not in ["Pilot", "Cabincrew"]:
            flag = True
            while flag:
                print("\nInvalid role, please try again.")
                newRole = input('Enter new role: ')
                if role in ["Pilot", "Cabincrew"]:
                    other.setRole(newRole)
                    flag = False
                else:
                    continue
        rank = other.getRank()
        if rank not in ["Captain", "Copilot", "Flight Service Manager", "Flight Attendant"]:
            flag = True
            while flag:
                print("\nInvalid rank, please try again.")
                newRank = ('Enter new rank: ')
                if rank in ["Captain", "Copilot", "Flight Service Manager", "Flight Attendant"]:
                    other.setRank(newRank)
                    flag = False
                else:
                    continue

        staff_license = other.getLicense()
        if staff_license.isalnum() == False:
            flag = True
            while flag:
                print("\nInvalid license, please try again.")
                newLicense = input('Enter new plane ID: ')
                if staff_license.isalnum():
                    other.setLicense(newLicense)
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
            if pilot.getRank() == 'Captain':
                captain_list.append(pilot.getName())
            elif pilot.getRank() == 'Copilot':
                copilot_list.append(pilot.getName())
        for flightAttendant in cabinCrewObject_list:
            if flightAttendant.getRank() == 'Flight Service Manager':
                fsm_list.append(flightAttendant.getName())
            elif flightAttendant.getRank() == 'Flight Attendant':
                fa_list.append(flightAttendant.getName())

        if staff_list[0] not in captain_list:
            flag = True
            while flag:
                print(staff_list[0] + ' is not a captain!')
                newCaptain = input('Enter new captain: ')
                if newCaptain in captain_list:
                    staff_list[0] = newCaptain
                else:
                    continue

        if staff_list[1] not in copilot_list:
            print(copilot_list)
            flag = True
            while flag:
                print(staff_list[1] + ' is not a copilot!')
                newCopilot = input('Enter new copilot: ')
                if newCopilot in copilot_list:
                    staff_list[1] = newCopilot
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

    def isEmailValid(self, other):
        if other[-11:] == "@nanair.com":
            return True
        else:
            return False

