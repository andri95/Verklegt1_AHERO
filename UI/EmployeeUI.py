
from UI.quitUI import Goodbye
from LL.mainLL import MainLL
from Models.staffData import StaffData

class EmployeeMenu():
    def __init__(self):
        self.mainObject = MainLL()

        self.MAINMENU = """
############################################################
#                           _|_	               quit(q)     #
#                   --@--@--(_)--@--@--                    #
#__________________________________________________________#
#                                                          #
#                      Employees                           #
#                                                          #
#           1. List employees                              #
#           2. Register employees                          #
#           3. Change employees                            #
#           4. Add staff to voyage                         #
#           5. Work schedule                               #
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
#                  Employees                               #
#                                                          # 
#              1. All employees                            #
#              2. Pilots                                   #
#              3. Flight attendants                        #
#                                                          #
#                                                          #
#                                                          #
#                                                          #
#                                                          #
#  back(b)                                                 #
############################################################"""
        self.start()

    def start(self):
        print(self.MAINMENU)
        while True:
            user_input = input("Input a command:")
            if user_input == "0":
                return

            elif user_input == "1":
                self.listStaff()

            elif user_input == "2":
                self.registerStaff()

            elif user_input == "q":
                Goodbye()

            else:
                print("Invalid command!")


    def listStaff(self):

        while True:

            print(self.SUBMENU1)
            user_input = input("Input a command: ")

            if user_input == "1":
                staffObject_list = self.mainObject.getAllStaffLL()
                for staffMember in staffObject_list:
                    print('Name: {}, Role: {}'.format(staffMember.getName(), staffMember.getRole()))

            elif user_input == "2":
                pilotObject_list = self.mainObject.getAllPilotsLL()
                for staffMember in pilotObject_list:
                    print('Name: {}, Role: {}'.format(staffMember.getName(), staffMember.getRole()))

            elif user_input == "3":
                cabinCrewObject_list = self.mainObject.getAllCabinCrewLL()
                for staffMember in cabinCrewObject_list:
                    print('Name: {}, Role: {}'.format(staffMember.getName(), staffMember.getRole()))

            elif user_input == "q":
                Goodbye()

            elif user_input == "0":
                self.start()

            else:
                print("Invalid command")

    def registerStaff(self):

        ssn = input('Enter social security number: ')
        name = input('Enter name: ')
        address = input('Enter address: ')
        cellPhone = input('Enter cell phone: ')
        phoneNumber = input('Enter phone number: ')
        email = input('Enter email: ')
        role = input('Enter role: ')
        rank = input('Enter rank: ')
        license_str = input('Enter license: ')
        newEmployee = StaffData(ssn, name, address, cellPhone, phoneNumber, email, role, rank, license_str)
        self.mainObject.addNewStaffLL(newEmployee)


