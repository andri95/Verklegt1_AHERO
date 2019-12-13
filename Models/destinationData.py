class DestinationData:
    def __init__(self, country, flightTime, contact, emergencyNumber, destId=''):
        self.country = country
        self.flightTime = flightTime
        self.contact = contact
        self.emergencyNumber = emergencyNumber
        self.destId = destId

    def getCountry(self):
        return self.country
        
    def getFlightTime(self):
        return self.flightTime

    def getContact(self):
        return self.contact

    def getEmergencyNumber(self):
        return self.emergencyNumber

    def getDestId(self):
        return self.destId

    def setCountry(self, newCountry):
        self.country = newCountry

    def setFlightTime(self, newFlightTime):
        self.flightTime = newFlightTime

    def setContact(self, newContact):
        self.contact = newContact

    def setEmergencyNumber(self, newNumber):
        self.emergencyNumber = newNumber

    def setDestinationId(self, destinationId):
        self.destId = destinationId

        