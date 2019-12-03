class DestinationData:
    def __init__(self, destName, flightTime, Distance, phoneNumber, contacts):
        self.destName = destName
        self.flightTime = flightTime
        self.distance = Distance
        self.phoneNumber = phoneNumber
        self.contact = contacts
        
    def getDestName(self):
        return self.destName

    def getFlightTime(self):
        return self.flightTime

    def getDistance(self):
        return self.distance

    def getPhoneNumber(self):
        return self.phoneNumber

    def getContact(self):
        return self.contact
