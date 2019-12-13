import datetime
from IO.mainIO import MainIO


class StaffLL:

    def __init__(self):
        self.mainObject = MainIO()
             
    '''Returns MainIO function call'''
    def getAllStaff(self):
        return self.mainObject.getStaffIO()

    '''Takes in ssn, gets list of all staff objects. Iterates through list,
       compares ssn to staffMember ssn, returns desired staffmember object'''
    def getStaffByID(self, ssn):
        staffObject_list = self.mainObject.getStaffIO()
        for staffMember in staffObject_list:
            if staffMember.getSSN() == ssn:
                return staffMember

    '''Gets list of all staff objects, finds all staff with role pilot and returns pilot object list'''
    def getAllPilots(self):
        staffObject_list = self.mainObject.getStaffIO()
        pilotObject_list = []
        for staffMember in staffObject_list:
            if staffMember.getRole() == 'pilot':
                pilotObject_list.append(staffMember)
        return pilotObject_list

    '''Gets list of all staff objects, finds all staff with role cabincrew and returns cabincrew object list'''
    def getAllCabinCrew(self):
        staffObject_list = self.mainObject.getStaffIO()
        pilotObject_list = []
        for staffMember in staffObject_list:
            if staffMember.getRole() == 'cabincrew':
                pilotObject_list.append(staffMember)
        return pilotObject_list

    '''Takes in ssn, gets list of all staff objects. Iterates through list,
       compares ssn to staffMember ssn, returns desired staffmember object'''
    def getStaffData(self, dataList):
        staffObject_list = self.mainObject.getStaffIO()
        for staffMember in staffObject_list:
            if staffMember.getSSN() == dataList[0]:
                return staffMember

    '''Recieves staff object, returns addNewStaffIO with object as parameter'''
    def addNewStaff(self, newEmployee):
        return self.mainObject.addNewStaffIO(newEmployee)

    '''Recieves workDay, finds all voyages happening on workday. Returns dictionary with voyage
       object as key and all staff objects on voyage as values'''
    def getWorkSchedule(self, workDay):
        workSchedule_list = []
        staffData = []
        voyageThisdayDict = {}
        voyage_list = self.mainObject.getVoyagesIO()

        # Iterates through all voyages, finds voyage happening on given date
        for voyage in voyage_list:
            voyageDate = voyage.getDepartureTime().split("T")
            if workDay == voyageDate[0]:
                workSchedule_list.append(voyage)

        # iterates through all voyages happening on given date, puts all staff on voyage in list
        for voyage in workSchedule_list:
            if voyage.getCaptain() != "":
                staffData.append(self.getStaffByID(voyage.getCaptain()))
                staffData.append(self.getStaffByID(voyage.getCoPilot()))
                staffData.append(self.getStaffByID(voyage.getFa1()))
                staffData.append(self.getStaffByID(voyage.getFa2()))
            else:
                staffData = voyage.getStaff()
            
            # sets voyage object as key and all staff list as value
            if voyage not in voyageThisdayDict:
                voyageThisdayDict[voyage] = staffData
                staffData = []
            else:
                staffData = []
        return voyageThisdayDict

    '''Recieves workday, iterates through voyages happening on given day, finds all staff that are
       not working in given voyages and puts in list'''
    def getWorkSchedlueAvailable(self, workDay):
        availableStaff = []
        unavailableStaff = []
        voyageThisdayDict = self.getWorkSchedule(workDay)
        staffObject_list = self.getAllStaff()

        # Iterates through voyages happening on given date
        for voyage in voyageThisdayDict:

            # Iterates through staffmembers working on given voyage and appends to unavailablestaff
            for workingStaff in voyageThisdayDict[voyage]:
                unavailableStaff.append(workingStaff)
        
        # iterates through all staff, if staff object is not in unavailable staff, staffmember is available
        for staffMember in staffObject_list:
            if staffMember.getSSN() not in unavailableStaff:
                availableStaff.append(staffMember)

        return availableStaff

