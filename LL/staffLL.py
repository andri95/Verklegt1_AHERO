import datetime
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
            if staffMember.getRole() == 'pilot':
                pilotObject_list.append(staffMember)
        return pilotObject_list

    def getAllCabinCrew(self):
        staffObject_list = self.mainObject.getStaffIO()
        pilotObject_list = []
        for staffMember in staffObject_list:
            if staffMember.getRole() == 'cabincrew':
                pilotObject_list.append(staffMember)
        return pilotObject_list

    def getStaffData(self, dataList):
        staffObject_list = self.mainObject.getStaffIO()
        for staffMember in staffObject_list:
            if staffMember.getSSN() == dataList[0]:
                return staffMember

    def addNewStaff(self, newEmployee):
        return self.mainObject.addNewStaffIO(newEmployee)

    def getWorkSchedule(self, workDay):
        workSchedule_list = []
        staffData = []
        voyageThisdayDict = {}
        voyage_list = self.mainObject.getVoyagesIO()
        for voyage in voyage_list:
            voyageDate = voyage.getDepartureTime().split("T")
            if workDay == voyageDate[0]:
                workSchedule_list.append(voyage)

        for voyage in workSchedule_list:
            if voyage.getCaptain() != "":
                staffData.append(self.getStaffByID(voyage.getCaptain()))
                staffData.append(self.getStaffByID(voyage.getCoPilot()))
                staffData.append(self.getStaffByID(voyage.getFa1()))
                staffData.append(self.getStaffByID(voyage.getFa2()))
            else:
                staffData = voyage.getStaff()
            if voyage not in voyageThisdayDict:
                voyageThisdayDict[voyage] = staffData
                staffData = []
            else:
                staffData = []
        return voyageThisdayDict

    def getWorkSchedlueAvailable(self, workDay):
        availableStaff = []
        unavailableStaff = []
        voyageThisdayDict = self.getWorkSchedule(workDay)
        staffObject_list = self.getAllStaff()
        for voyage in voyageThisdayDict:
            for workingStaff in voyageThisdayDict[voyage]:
                unavailableStaff.append(workingStaff)
        for staffMember in staffObject_list:
            if staffMember.getSSN() not in unavailableStaff:
                availableStaff.append(staffMember)

        return availableStaff

