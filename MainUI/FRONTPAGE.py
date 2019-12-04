from MainUI.AirplaneUI import AirplaneUI
from MainUI.DestinationUI import DestinationUI
from MainUI.EmployeeUI import EmployeeUI
from MainUI.VoyageUI import VoyageUI
class MainMenu():
    def __init__(self):
        self.MAINMENU = """
############################################################
#                            |                             #
#                            |                             #
#                          .-'-.                           #
#                         ' ___ '                          #
#               ---------'  .-.  '---------                #
#________________________'  '-'  '_________________________#
#''''''-|---|--/    \==][^',_m_,'^][==/    \--|---|-'''''' #
#              \    /  ||/   H   \||  \    /               #
#               '--'   OO   O|O   OO   '--' _              #
#            _   _       _   _      __   (_)               #
#           |  \| | __ _|  \| |    /  \   _ _ __           #
#           | . ` |/ _` | . ` |   / /\ \ | | '__|          #
#           | |\  | (_| | |\  |  / ____ \| | |             #
#           |_| \_|\__,_|_| \_| /_/    \_\_|_|             #
#                                                          #
############################################################
#            #               #               #             #
#            #               #               #             #
# 1.Voyage   # 2.Employees   # 3.Destination # 4.Airplanes #
#            #               #               #             #
#            #               #               #             #
############################################################
"""
        self.start()



    def start(self):
        print(self.MAINMENU)

        while True:
            var = input("Input a command: ")
            if var =="1":
                voyageMenu()
            elif var == "2":
                employeemenu()
            elif var =="3":
                destinationmenu()
            elif var =="4":
                Airplanemenu()
            elif var =="q":
                Goodbye()
            else:
                print("Invalid command")



