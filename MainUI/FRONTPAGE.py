import AirplaneUI
import DestinationUI
import EmployeeUI
import VoyageUI
import quitUI
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
                VoyageUI.VoyageMenu()
            elif var == "2":
                EmployeeUI.EmployeeMenu()
            elif var =="3":
                DestinationUI.DestinationMenu()
            elif var =="4":
                AirplaneUI.AirplaneMenu()
            elif var =="q":
                quitUI.Goodbye()
            else:
                print("Invalid command")



