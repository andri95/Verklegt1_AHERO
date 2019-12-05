

class StaffData():
    def __init__(self, SSN, name, address, cellPhone, phoneNumber, email, role, rank, license="N/A"):
        self.SSN = SSN
        self.name = name
        self.address = address
        self.cellPhone = cellPhone
        self.phoneNumber = phoneNumber
        self.email = email
        self.role = role
        self.rank = rank
        self.license = license

    def getSSN(self):
        return self.SSN

    def getName(self):
        return self.name

    def getRole(self):
        return self.role

    def getRank(self):
        return self.rank

    def getLicence(self):
        return self.license

    def getAddress(self):
        return self.address

    def getCellPhone(self):
        return self.cellPhone

    def getPhoneNumber(self):
        return self.phoneNumber

    def getEmail(self):
        return self.email

    def setLicense(self, newLicense):
        self.license += ('/' + newLicense)



    def __str__(self):
        return "ssn: {}\nname: {}\nrole: {}\nrank: {}\nlicence: {}".format(self.SSN, self.name, self.role, self.rank, self.license)
