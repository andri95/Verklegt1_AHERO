from UI.airplaneUI import AirplaneUI
from UI.destinationUI import DestinationUI
from UI.staffUI import StaffUI
from UI.voyageUI import VoyageUI
from UI.quitUI import QuitUI
from UI.secretUI import SecretUI

class MainUI:
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
            #  A dictionary that handles users input.
            mainCommand_dict = {'1': VoyageUI, '2': StaffUI, '3': DestinationUI, '4': AirplaneUI, 'q': QuitUI, 'chuck norris':SecretUI}
            print(self.MAINMENU)
            user_input = input("Input a command: ")
            if user_input in mainCommand_dict:  #  Checks if the users input is correct.
                for key in mainCommand_dict:
                    if user_input == key:
                        mainCommand_dict[key]()  #  Calls the correct command.
            else:
                print('Invalid command!')
                



