
from UI.quitUI import Goodbye
from LL.mainLL import MainLL

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
#              4. Airplane managers                        #
#              5. Human resources managers                 #
#              6. Trip managers                            #
#                                                          #
#                                                          #
#  back(b)                                                 #
############################################################"""
        self.start()

    def start(self):
        print(self.MAINMENU)
        while True:
            var = input("Input a command:")
            if var == "0":
                return
            elif var =="1":
                self.Listemployees()
            elif var == "q":
                Goodbye()


    def Listemployees(self):

        while True:
            print(self.SUBMENU1)
            var = input("Input a command: ")
            if var == "1":
                staffObject_list = self.mainObject.getAllStaffLL()
                for staffMember in staffObject_list:
                    print('Name: {}, Role: {}'.format(staffMember.getName(), staffMember.getRole()))

            elif var == "2":
                cabinCrew_list = self.mainObject.getAllPilotsLL()
                for staffMember in cabinCrew_list:
                    print('Name: {}, Role: {}'.format(staffMember.getName(), staffMember.getRole()))
            elif var == "3":
                print("Not yet implemented")
            elif var == "4":
                print("Not yet implemented")
            elif var == "q":
                Goodbye()
            elif var == "0":
                return
            else:
                print("Invalid command")
