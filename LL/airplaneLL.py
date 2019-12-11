from IO.mainIO import MainIO

class AirplaneLL:
    def __init__(self):
        self.mainObject = MainIO()

    def validateAirPlaneData(self, new_airplane):
        print(type(new_airplane))
        flag = True
        if flag == True:
            #self.AirplaneIO.addNewAirplane(new_airplane)
            return True

    def addAirplane(self, newAirplane):
        return self.mainObject.addNewAirplaneIO(newAirplane)

    def getAirplanes(self):
        return self.mainObject.getAirplanesIO()

    def getAirplaneStatus(self):
        pass

    def getAirplaneByID(self, ID):
        license_dict = self.getLicenseDict()
        return_dict = {}
        for pilotLicense in license_dict:
            if pilotLicense == ID:
                return_dict[pilotLicense] = license_dict[pilotLicense]
        return return_dict

    def addLicense(self, dataList):
        return self.mainObject.addLicenseIO(dataList)

    def getAllPilots(self):
        staffObject_list = self.mainObject.getStaffIO()
        pilotObject_list = []
        for staffMember in staffObject_list:
            if staffMember.getRole() == 'Pilot':
                pilotObject_list.append(staffMember)
        return pilotObject_list

    def getLicenseDict(self):
        staffObject_list = self.mainObject.getStaffIO()
        pilotObject_list = []
        for staffMember in staffObject_list:
            if staffMember.getRole() == 'Pilot':
                pilotObject_list.append(staffMember)
        license_Dict = {}
        for staffMember in pilotObject_list:
            if staffMember.getLicense() not in license_Dict:
                license_Dict[staffMember.getLicense()] = [staffMember.getName()]
            else:
                license_Dict[staffMember.getLicense()].append(staffMember.getName())
        return license_Dict



