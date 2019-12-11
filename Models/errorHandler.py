from Models.airplaneData import AirplaneData
from Models.destinationData import DestinationData
from Models.voyageData import VoyageData
from Models.staffData import StaffData


class ErrorHandler:

    def addNewAirplaneEH(self, other):
        planeID = other.getPlaneId()
        planeIDValid = ErrorHandler().isOnlyNumbersOrLetters(planeID)
        if planeIDValid:
            print("planeID valid")
            type = other.getType()
            #typesValid = ErrorHandler().isOnlyLetters(type)
            if type.isalpha():
                print("type valid")
                model = other.getModel()
                #modelValid = ErrorHandler().isOnlyAscii(model)
                if model.isalnum():
                    print("model valid")
                    capacity = other.getCapacity()
                    #capacityValid = ErrorHandler().isOnlyNumbers(capacity)
                    if capacity.isdigit():
                        print("capacity valid")
                        return True
                    else:
                        print("capacity invalid")
                        return False
                else:
                    print("model invalid")
                    return False
            else:
                print("type invalid")
                return False
        else:
            print("planeID invalid")
            return False

    def addNewDestinationEH(self, other):
        # Pæling hvernig á að error check-a "flightTime"??
        country = other.getCountry()
        if country.isalpha():
            print("country valid")
            flighttime = other.getFlightTime()
            if flighttime.isdigit():
                print("flighttime valid")
                contact = other.getContact()
                contactValid = ErrorHandler().isNameValid(contact)
                if contactValid:
                    print("contact valid")
                    emergencynum = other.getEmergencyNumber()
                    if emergencynum.isdigit():
                        print("emergencynum valid")
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
        # Pæling hvernig á að error check-a "flightTime"??
        # Og líka pæling hvernig er best að error check-a "aircraftID".
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
        if SSN.isdigit():
            name = other.getName()
            nameValid = ErrorHandler().isNameValid(name)
            if nameValid:
                address = other.getAddress()
                if address.isalnum():
                    cellPhone = other.getCellPhone()
                    if cellPhone.isdigit():
                        phoneNumber = other.getPhoneNumber()
                        if phoneNumber.isdigit():
                            email = other.getEmail()
                            emailValid = ErrorHandler().isEmailValid(email)
                            if emailValid:
                                role = other.getRole()
                                if role.isalpha():
                                    rank = other.getRank()
                                    if rank.isalpha():
                                        license = other.getLicence()
                                        if license.isalnum():
                                            return True
                                        else:
                                            print("Invalid license, please try again.")
                                            return False
                                    else:
                                        print("Invalid rank, please try again.")
                                        return False
                                else:
                                    print("Invalid role, please try again.")
                                    return False
                            else:
                                print("Invalid email, please try again.")
                                return False
                        else:
                            print("Invalid phone number, please try again.")
                            return False
                    else:
                        print("Invalid cellphone, please try again.")
                        return False
                else:
                    print("Invalid address, please try again.")
                    return False
            else:
                print("Invalid name, please try again.")
                return False
        else:
            print("Invalid SSN, please try again.")
            return False

    def isOnlyNumbersOrLetters(self, other):
        """ Returns False if the string contains only letters or only numbers."""
        #print("in isOnlyNumberOrLetters")
        if other.isdigit():
            return False
        elif other.isalpha():
            return False
        else:
            return True

    def isOnlyLetters(self, other):
        """ Returns false if the string does not only contain letters. """
        #print("in isOnlyLetters")
        if other.isalpha():
            return True
        else:
            return False

    def isOnlyNumbers(self, other):
        """ Returns false if the string does not only contain numbers. """
        # print("in isOnlyNumbers")
        if other.isdigit():
            return True
        else:
            return False

    def isOnlyAscii(self, other):
        if other.isalnum():
            return True
        else:
            return False

    def isNameValid(self, other):
        """ Returns false if any letter in the name is not from the alphabet. """
        for word in other.split():
            if word.isalpha() == False:
                return False
        return True

    def isEmailValid(self, other):
        if other[:-10] == "@nanair.com":
            return True
        else:
            return False
