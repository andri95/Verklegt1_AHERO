'''Model class used solely as data transfer object when passing
   information between layers. Class only contains getters and setters'''
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

    def setSSN(self, newSSN):
        self.SSN = newSSN

    def setName(self, newName):
        self.name = newName

    def setRole(self, newRole):
        self.role = newRole

    def setRank(self, newRank):
        self.rank = newRank

    def setLicense(self, newLicense):
        self.pilot_license = newLicense

    def setAddress(self, newAddress):
        self.address = newAddress

    def setCellPhone(self, newCellPhone):
        self.cellPhone = newCellPhone

    def setPhoneNumber(self, newPhoneNumber):
        self.phoneNumber = newPhoneNumber

    def setEmail(self, newEmail):
        self.email = newEmail
