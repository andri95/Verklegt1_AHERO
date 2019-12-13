from UI.quitUI import QuitUI
from LL.mainLL import MainLL
from Models.inputHandler import InputHandler
from Models.outputHandler import OutputHandler
from Models.errorHandler import ErrorHandler
import datetime

class StaffUI:
    def __init__(self):
        self.mainObject = MainLL()
        self.inputObject = InputHandler()
        self.outputObject = OutputHandler()
        self.errorObject = ErrorHandler()
        

        self.MAINMENU = """
############################################################
#                           _|_	               quit(q)     #
#                   --@--@--(_)--@--@--                    #
#__________________________________________________________#
#                                                          #
#                        Employees                         #
#                                                          #
#                  1. List employees                       #
#                  2. Register employees                   #
#                  3. Work Schedule                        #
#                                                          #
#                                                          #
#                                                          #
#                                                          #
#                                                          #
#                                                          #
#  back(b)                                                 #
############################################################
"""
        self.SUBMENU1 ="""
############################################################
#                           _|_	               quit(q)     #
#                   --@--@--(_)--@--@--                    #
#__________________________________________________________#
#                                                          #
#                                                          #
#                        Employees                         #
#                                                          # 
#                   1. All employees                       #
#                   2. Pilots                              #
#                   3. Cabin Crew                          #
#                   4. Find employee                       #
#                                                          #
#                                                          #
#                                                          #
#                                                          #
#  back(b)                                                 #
############################################################"""

        self.SUBMENU2 ="""
############################################################
#                           _|_	               quit(q)     #
#                   --@--@--(_)--@--@--                    #
#__________________________________________________________#
#                                                          #
#                                                          #
#                      Work schedule                       #
#                                                          # 
#               1. Find available staff                    #
#               2. Work schedule by date                   #
#               3. Work schedule for single employee       #
#                                                          #
#                                                          #
#                                                          #
#                                                          #
#                                                          #
#                                                          #
#  back(b)                                                 #
############################################################"""
        self.start()

    def start(self):
        while True:
            mainCommand_dict = {'1': self.listStaffUI, '2': self.addNewStaffUI, '3': self.workScheduleUI, 'q': QuitUI}
            print(self.MAINMENU)
            user_input = input("Input a command: ")
            if user_input != 'b':
                if user_input in mainCommand_dict:
                    for key in mainCommand_dict:
                        if user_input == key:
                            mainCommand_dict[key]()
                else:
                    print('Invalid command!')
            else:
                return

    def listStaffUI(self):

        while True: 
            subCommand_dict = {'1': self.getAllStaffUI, '2': self.getAllPilotsUI, '3': self.getAllCabinCrewUI, 
                                 '4': self.getStaffByIdUI, 'q': QuitUI}
            print(self.SUBMENU1)
            user_input = input("Input a command: ")
            if user_input != 'b':
                if user_input in subCommand_dict:
                    for key in subCommand_dict:
                        if user_input == key:
                            subCommand_dict[key]()
                else:
                    print('Invalid command!')
            else:
                return

    def workScheduleUI(self):

        while True:
            subCommand_dict = {'1': self.availableStaffUI, '2': self.unavailableStaffUI, '3': self.singleStaffUI, 'q': QuitUI}
            print(self.SUBMENU2)
            user_input = input('Input a command: ')
            if user_input != 'b':
                if user_input in subCommand_dict:
                    for key in subCommand_dict:
                        if user_input == key:
                            subCommand_dict[key]()
                else:
                    print('Invalid command!')
            else:
                return

    def getAllStaffUI(self):
        staffObject_list = self.mainObject.getAllStaffLL()
        return self.outputObject.allStaffOH(staffObject_list)
        

    def getAllPilotsUI(self):
        pilotObject_list = self.mainObject.getAllPilotsLL()
        #sorted(pilotObject_list, key=methodcaller('StaffData.getLicense')
        return self.outputObject.allPilotsOH(pilotObject_list)


    def getAllCabinCrewUI(self):
        cabinCrewObject_list = self.mainObject.getAllCabinCrewLL()
        self.outputObject.allCabinCrewOH(cabinCrewObject_list)

    def addNewStaffUI(self):
        newEmployee = self.inputObject.addNewStaffIH()
        self.mainObject.addNewStaffLL(newEmployee)

    def getStaffByIdUI(self):
        staffObject_dict = {}
        staffObject_list = self.mainObject.getAllStaffLL()
        for counter, staffMember in enumerate(staffObject_list, 1):
            staffObject_dict[str(counter)] = staffMember
        self.outputObject.singleStaffListOH(staffObject_dict)
        user_input = input("Choose an employee: ")
        errorChecked = self.errorObject.getStaffByIdEH(user_input, staffObject_dict)
        staffMember = self.mainObject.getStaffByIDLL(errorChecked.getSSN())
        self.outputObject.singleStaffHeaderOH()
        self.outputObject.singleStaffOH(staffMember)

    def availableStaffUI(self):
        flag = True
        while flag:
            input_date = input("Enter a date 'YYYY-MM-DD' : ")
            if self.errorObject.errorCheckDateEH(input_date):
                flag = False
            else:
                continue
        availableStaff = self.mainObject.workScheduleAvailableLL(input_date)
        self.outputObject.workScheduleAvailableOH(availableStaff)

    def unavailableStaffUI(self):
        availableDates_dict = {}
        availableDates_list = self.mainObject.availableDatesLL()
        for counter, date in enumerate(availableDates_list, 1):
            availableDates_dict[str(counter)] = date
        self.outputObject.availableDatesOH(availableDates_dict)

        user_input = input("Choose date: ")
        errorChecked = self.errorObject.availableDatesEH(user_input, availableDates_dict)
        workSchedule_dict = self.mainObject.workScheduleLL(errorChecked)
        self.outputObject.allVoyagesOH(workSchedule_dict)

    def singleStaffUI(self):
        print('Start of work week')
        dateStart = self.inputObject.workWeekIH()
        print('End of work week')
        dateEnd = self.inputObject.workWeekIH()
        compareDay = dateStart.day + 7
        compareDate = dateStart.replace(day = compareDay)
        if dateEnd != compareDate:
            print('That is not a work week!')
        else:
            staffObject_dict = {}
            staffObject_list = self.mainObject.getAllStaffLL()
            for counter, staffMember in enumerate(staffObject_list, 1):
                staffObject_dict[str(counter)] = staffMember
            self.outputObject.singleStaffListOH(staffObject_dict)
            user_input = input("Choose an employee: ")
            errorChecked = self.errorObject.getStaffByIdEH(user_input, staffObject_dict)
            dataList = [dateStart, dateEnd, errorChecked.getSSN()]
            workWeekObject_list = self.mainObject.workWeekLL(dataList)
            self.outputObject.workWeekOH(workWeekObject_list)