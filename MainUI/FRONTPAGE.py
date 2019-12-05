from MainUI.AirplaneUI import AirplaneMenu
from MainUI.DestinationUI import DestinationMenu
from MainUI.EmployeeUI import EmployeeMenu
from MainUI.VoyageUI import VoyageMenu
from MainUI.quitUI import Goodbye
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

        while True:
            print(self.MAINMENU)
            var = input("Input a command: ")
            if var =="1":
                VoyageMenu()
            elif var == "2":
                EmployeeMenu()
            elif var =="3":
                DestinationMenu()
            elif var =="4":
                AirplaneMenu()
            elif var =="q":
                Goodbye()
            else:
                print("Invalid command")



