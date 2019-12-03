
class StaffData():
    def __init__(self, SSN, name, role, rank, license="N/A"):
        self.SSN = SSN
        self.name = name
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

    def __str__(self):
        return "ssn: {}\nname: {}\nrole: {}\nrank: {}\nlicence: {}".format(self.SSN, self.name, self.role, self.rank, self.license)


