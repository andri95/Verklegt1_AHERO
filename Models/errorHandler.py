from Models.airplaneData import AirplaneData
from Models.destinationData import DestinationData
from Models.voyageData import VoyageData
from Models.staffData import StaffData


class ErrorHandler:

    def addNewAirplaneEH(self, other):
        planeID = other.getPlaneId()
        planeIDValid = ErrorHandler().isOnlyNumbersOrLetters(planeID)
        if planeIDValid:
            type = other.getType()
            if type.isalpha():
                model = other.getModel()
                if model.isalnum():
                    capacity = other.getCapacity()
                    if capacity.isdigit():
                        return True
                    else:
                        print("Invalid capacity, please try again.")
                        return False
                else:
                    print("Invalid model, please try again.")
                    return False
            else:
                print("Invalid type, please try again.")
                return False
        else:
            print("Invalid planeID, please try again.")
            return False

    def addNewDestinationEH(self, other):
        country = other.getCountry()
        if country.isalpha():
            flighttime = other.getFlightTime()
            if flighttime.isdigit():
                contact = other.getContact()
                contactValid = ErrorHandler().isNameValid(contact)
                if contactValid:
                    emergencynum = other.getEmergencyNumber()
                    if emergencynum.isdigit():
                        return True
                    else:
                        print("Invalid emergency number, please try again.")
                        return False
                else:
                    print("Invalid contact, please try again.")
                    return False
            else:
                print("Invalid contact, please try again.")
                return False
        else:
            print("emergencynum valid")
            return False

    def addNewFlightEH(self, other):
        print(type(other))
        flightNumber = other.getFlightNumber()
        flightNumberValid = ErrorHandler().isOnlyAscii(flightNumber)
        if flightNumberValid:
            print("flightNumber valid")
            departingFrom = other.getDepartingFrom()
            departingFromValid = ErrorHandler().isOnlyLetters(departingFrom)
            if departingFromValid:
                print("departingFrom valid")
                arrivingAt = other.getArrivingAt()
                arrivingAtValid = ErrorHandler().isOnlyLetters(arrivingAt)
                if arrivingAtValid:
                    print("arrivingAt valid")
                    departureTime = other.getDepartureTime()
                    departureTimeValid = ErrorHandler().isOnlyNumbers(departureTime)
                    if departureTimeValid:
                        print("departureTime valid")
                        arrivalTime = other.getArrivalTime()
                        arrivalTimeValid = ErrorHandler().isOnlyNumbers(arrivalTime)
                        if arrivalTimeValid:
                            print("arrivalTime valid")
                            aircraftId = other.getAircraftId()
                            aircraftIdValid = ErrorHandler().isOnlyNumbersOrLetters(aircraftId)
                            if aircraftIdValid:
                                print("aircraftId valid")
                                return True
                            else:
                                return False
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False

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

    def addStaffToVoyageEH(self, staff_list, pilotObject_list, cabinCrewObject_list):
        
        captain_list = []
        copilot_list = []
        fsm_list = []
        fa_list = []
        for pilot in pilotObject_list:
            if pilot.getRank() == 'Captain':
                captain_list.append(pilot.getSSN())
            elif pilot.getName == 'Copilot':
                copilot_list.append(pilot.getSSN())
        for flightAttendant in cabinCrewObject_list:
            if flightAttendant.getRank() == 'Flight Service Manager':
                fsm_list.append(flightAttendant.getSSN())
            elif flightAttendant.getName() == 'Flight Attendant':
                fa_list.append(flightAttendant.getSSN())

        if staff_list[0] not in captain_list:
            flag = True
            while flag:
                print(staff_list[0] + ' is not a captain!')
                newCaptain = input('Enter new captain ssn: ')
                if newCaptain in captain_list:
                    staff_list[0] = newCaptain
                else:
                    continue

        if staff_list[1] not in copilot_list:
            flag = True
            while flag:
                print(staff_list[1] + ' is not a copilot!')
                newCopilot = input('Enter new copilot ssn: ')
                if newCopilot in copilot_list:
                    staff_list[1] = newCopilot
                else:
                    continue

        if staff_list[2] not in fsm_list:
            flag = True
            while flag:
                print(staff_list[2] + ' is not a flight service manager!')
                newFsm = input()




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

