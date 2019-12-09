
from IO.mainIO import MainIO

class StaffLL:

    def __init__(self):
        self.mainObject = MainIO()       

    def getAllStaff(self):
        return self.mainObject.getStaffIO()

    def getStaffByID(self, ssn):
        staffObject_list = self.mainObject.getStaffIO()
        for staffMember in staffObject_list:
            if staffMember.getSSN() == ssn:
                return staffMember

    def getAllPilots(self):
        staffObject_list = self.mainObject.getStaffIO()
        pilotObject_list = []
        for staffMember in staffObject_list:
            if staffMember.getRole() == 'Pilot':
                pilotObject_list.append(staffMember)
        return pilotObject_list

    def getAllCabinCrew(self):
        staffObject_list = self.mainObject.getStaffIO()
        cabinCrewObject_list = []
        for staffMember in staffObject_list:
            if staffMember.getRole() == 'Cabincrew':
                cabinCrewObject_list.append(staffMember)
        return cabinCrewObject_list

    def getStaffData(self, dataList):
        staffObject_list = self.mainObject.getStaffIO()
        for staffMember in staffObject_list:
            if staffMember.getSSN() == dataList[0]:
                return staffMember

    def addNewStaff(self, newEmployee):
        return self.mainObject.addNewStaffIO(newEmployee)

    def getWorkSchedule(self, workDay):
        voyage_list = self.mainObject.getVoyagesIO()
        for voyage in voyage_list:
            voyageDate = voyage.getDepartureTime().split("T")
            if workDay == voyageDate[0]:
                return voyage
                #print("::::", voyage.getDepartureTime())
        #print("all voyages times: ", temp)
        #print("we are looking for:", workDay)






    

