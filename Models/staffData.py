

class StaffData():
    def __init__(self, SSN, name, address, cellPhone, phoneNumber, email, role, rank, pilot_license="N/A"):
        self.SSN = SSN
        self.name = name
        self.address = address
        self.cellPhone = cellPhone
        self.phoneNumber = phoneNumber
        self.email = email
        self.role = role
        self.rank = rank
        self.pilot_license = pilot_license

    def getSSN(self):
        return self.SSN

    def getName(self):
        return self.name

    def getRole(self):
        return self.role

    def getRank(self):
        return self.rank

    def getLicense(self):
        return self.pilot_license

    def getAddress(self):
        return self.address

    def getCellPhone(self):
        return self.cellPhone

    def getPhoneNumber(self):
        return self.phoneNumber

    def getEmail(self):
        return self.email

    def setLicense(self, newLicense):
        self.pilot_license = newLicense
