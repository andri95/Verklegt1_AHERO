

class staffData():
    def __init__(self, SSN, name, role, rank, license="N/A"):
        self.SSN = SSN
        self.name = name
        self.role = role
        self.rank = rank
        self.license = license

    def __str__(self):
        return "ssn: {}\nname: {}\nrole: {}\nrank: {}\nlicence: {}".format(self.SSN, self.name, self.role, self.rank, self.license)


staff1 = staffData("1611983239", "Rúnar", "Pilot", "Captain")
print(staff1)
