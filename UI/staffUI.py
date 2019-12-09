from UI.quitUI import QuitUI
from LL.mainLL import MainLL
from Models.inputHandler import InputHandler

class StaffUI:
    def __init__(self):
        self.mainObject = MainLL()
        self.inputObject = InputHandler()

        self.MAINMENU = """
############################################################
#                           _|_	               quit(q)     #
#                   --@--@--(_)--@--@--                    #
#__________________________________________________________#
#                                                          #
#                        Employees                         #
#                                                          #
#                 1. List employees                        #
#                 2. Register employees                    #
#                 3. Add staff to voyage                   #
#                 4. Work Schedule                         #
#                                                          #
#                                                          #
#                                                          #
#                                                          #
#                                                          #
#  0.Back                                                  #
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
#                   3. Flight attendants                   #
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
#               1. Available staff                         #
#               2. Unavailable staff                       #
#               3. Work scedule for single employee        #
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
            mainCommand_dict = {'1': self.listStaff, '2': self.addNewStaffUI, '3': self.workScheduleUI, 'q': QuitUI}
            print(self.MAINMENU)
            user_input = input("Input a command: ")
            if user_input != '0':
                if user_input in mainCommand_dict:
                    for key in mainCommand_dict:
                        if user_input == key:
                            mainCommand_dict[key]()
                else:
                    print('Invalid command!')
            else:
                return

    def listStaff(self):

        while True: 
            subCommand_dict = {'1': self.getAllStaffUI, '2': self.getAllPilotsUI, '3': self.getAllCabinCrewUI,
                                 '4': self.getStaffByIdUI, 'q': QuitUI}
            print(self.SUBMENU1)
            user_input = input("Input a command: ")
            if user_input != '0':
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
            if user_input != '0':
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
        for staffMember in staffObject_list:
            print('Name: {}, Role: {}'.format(staffMember.getName(), staffMember.getRole()))

    def getAllPilotsUI(self):
        pilotObject_list = self.mainObject.getAllPilotsLL()
        for staffMember in pilotObject_list:
            print('Name: {}, Role: {}'.format(staffMember.getName(), staffMember.getRole()))

    def getAllCabinCrewUI(self):
        cabinCrewObject_list = self.mainObject.getAllCabinCrewLL()
        for staffMember in cabinCrewObject_list:
            print('Name: {}, Role: {}'.format(staffMember.getName(), staffMember.getRole()))

    def addNewStaffUI(self):

        newEmployee = self.inputObject.addNewStaffIH()
        self.mainObject.addNewStaffLL(newEmployee)

    def getStaffByIdUI(self):
        staffObject_list = self.mainObject.getAllStaffLL()
        for staffMember in staffObject_list:
            print('Name: {}, SSN: {}'.format(staffMember.getName(), staffMember.getSSN()))
        input_ssn = input("Enter social security number: ")
        staffMember = self.mainObject.getStaffByIDLL(input_ssn)
        print(staffMember)

    def availableStaffUI(self):
        pass

    def unavailableStaffUI(self):
        pass

    def singleStaffUI(self):
        pass