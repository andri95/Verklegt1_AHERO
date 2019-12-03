class DestinationData:
    def __init__(self, country, flightTime, contact, emergencyNumber):
        self.country = country
        self.flightTime = flightTime
        self.contact = contact
        self.emergencyNumber = emergencyNumber

    def getCountry(self):
        return self.country
        
    def getFlightTime(self):
        return self.flightTime

    def getContact(self):
        return self.contact

    def getEmergencyNumber(self):
        return self.emergencyNumber

    def setContact(self, newContact):
        self.contact = newContact

    def setEmergencyNumber(self, newNumber):
        self.emergencyNumber = newNumber
