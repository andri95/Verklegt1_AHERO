import quitUI
class EmployeeMenu():
    def __init__(self):
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
                quitUI.Goodbye()


    def Listemployees(self):
        print(self.SUBMENU1)

        while True:
            var = input("Input a command: ")
            if var == "1":
                print("Not yet implemented")
            elif var == "2":
                print("Not yet implemented")
            elif var == "3":
                print("Not yet implemented")
            elif var == "4":
                print("Not yet implemented")
            elif var == "q":
                quitUI.Goodbye()
            elif var == "0":
                return
            else:
                print("Invalid command")
