from UI.quitUI import QuitUI
from LL.mainLL import MainLL
from Models.inputHandler import InputHandler
from Models.outputHandler import OutputHandler
from Models.errorHandler import ErrorHandler
import datetime

class StaffUI:

    '''Instances of appropriate classes created in constructor so the class 
       has access to their functions. MainLL connects the class to the logic layer
       and the other classes handle inputs, outputs and errors'''
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

        '''Start function called in constructor so that as soon as the class is
           initiated start function runs'''
        self.start()

    def start(self):
        while True:
            # dictionary with class functions as values and available user inputs as keys
            mainCommand_dict = {'1': self.listStaffUI, '2': self.addNewStaffUI, '3': self.workScheduleUI, 'q': QuitUI}
            print(self.MAINMENU)
            user_input = input("Input a command: ")
            
            # Handles user input, calls appropriate function if user input is key in dict
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

    '''Calls MainLL function into variable, passes variable into outputHandler function where
       information is printed'''
    def getAllStaffUI(self):
        staffObject_list = self.mainObject.getAllStaffLL()
        return self.outputObject.allStaffOH(staffObject_list)
        
    '''Calls MainLL function into variable, passes variable into outputHandler function where
       information is printed'''
    def getAllPilotsUI(self):
        pilotObject_list = self.mainObject.getAllPilotsLL()
        return self.outputObject.allPilotsOH(pilotObject_list)

    '''Calls MainLL function into variable, passes variable into outputHandler function where
       information is printed'''
    def getAllCabinCrewUI(self):
        cabinCrewObject_list = self.mainObject.getAllCabinCrewLL()
        self.outputObject.allCabinCrewOH(cabinCrewObject_list)

    '''Calls input object where user inputs appropriate information and staffObject
       is created. New staff object then passed down into LL through MainLL'''
    def addNewStaffUI(self):
        # newEmployee object created in addNewStaffIH
        newEmployee = self.inputObject.addNewStaffIH()
        
        # Role of employee checked, if not pilot then license should be N/A
        role = newEmployee.getRole()
        if role == "cabincrew":
            newEmployee.setLicense("N/A")
            self.mainObject.addNewStaffLL(newEmployee)
            print('New staff member registered!')

        # If employee is pilot then airplane license should be added
        else:
            airplaneList = self.mainObject.airplaneObject.getAirplanes()
            airplaneIdList = []
            for airplane in airplaneList:
                airplaneIdList.append(airplane.getPlaneId())
            print("What license does", newEmployee.getName(), "have: ")
            print("{}\n".format(" ".join(i for i in airplaneIdList)))
            staff_license = input("Enter license: ")
            while staff_license not in airplaneIdList:
                print("\nInvalid license, can only include alphanumerical characters.")
                staff_license = input("Enter license: ")
            newEmployee.setLicense(staff_license)

            # New staff object passed down into LL through MainLL
            self.mainObject.addNewStaffLL(newEmployee)
            print('New staff member registered!')

    '''Dictionary created containing all employees as values, numbers as keys. User picks
       employee and chosen employee ssn is passed into getStaffByIdLL which returns desired staff object,
       staff object then passed into outputObject funtion'''
    def getStaffByIdUI(self):
        # Dictionary with number as key and staff object as value created
        staffObject_dict = {}
        staffObject_list = self.mainObject.getAllStaffLL()
        for counter, staffMember in enumerate(staffObject_list, 1):
            staffObject_dict[str(counter)] = staffMember
        
        # All staff listed and user chooses desired employee
        self.outputObject.singleStaffListOH(staffObject_dict)
        user_input = input("Choose an employee: ")
        errorChecked = self.errorObject.getStaffByIdEH(user_input, staffObject_dict)

        # Chosen employee ssn passed into getStaffByID
        staffMember = self.mainObject.getStaffByIDLL(errorChecked.getSSN())

        # staff object passed into outputHandler function
        self.outputObject.singleStaffHeaderOH()
        self.outputObject.singleStaffOH(staffMember)

    '''User picks date, date is passed into workScheduleAvailableLL which returns list of staff
       objects that are not working on given day.'''
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

    '''Shows user available dates, user picks desired date. date then passed into workScheduleLL
       that returns dictionary with all voyages as keys and staff working the voyages as keys'''
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

    '''Prompts user for startdate and enddate. User then picks employee he wants to see work schedule for.
       user input and desired dates are passed into workWeekLL which returns object list containing voyage objects'''
    def singleStaffUI(self):
        print('Start of work week')
        dateStart = self.inputObject.workWeekIH()
        print('End of work week')
        dateEnd = self.inputObject.workWeekIH()
        compareDay = dateStart.day + 7
        compareDate = dateStart.replace(day = compareDay)
        
        # check if input dates are a week
        if dateEnd != compareDate:
            print('That is not a work week!')
        else:
            # dictionary created with numbers as keys and values are staff objects
            staffObject_dict = {}
            staffObject_list = self.mainObject.getAllStaffLL()
            for counter, staffMember in enumerate(staffObject_list, 1):
                staffObject_dict[str(counter)] = staffMember
            self.outputObject.singleStaffListOH(staffObject_dict)

            # user chooses employee, dataList with dates and employee ssn passed into LL
            user_input = input("Choose an employee: ")
            errorChecked = self.errorObject.getStaffByIdEH(user_input, staffObject_dict)
            dataList = [dateStart, dateEnd, errorChecked.getSSN()]
            workWeekObject_list = self.mainObject.workWeekLL(dataList)
            self.outputObject.workWeekOH(workWeekObject_list)