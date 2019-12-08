from UI.quitUI import QuitUI
from Models.inputHandler import InputHandler
from LL.mainLL import MainLL


class AirplaneUI:
    def __init__(self):

        self.mainObject = MainLL()
        self.inputObject = InputHandler()
        self.MAINMENU = """
############################################################
#                           _|_	               quit(q)     #
#                   --@--@--(_)--@--@--                    #
#__________________________________________________________#				  					                   
#                                                          #
#                       Airplanes                          #
#                                                          #
#                   1. list Airplanes                      #
#                   2. Add airplanes                       #
#                                                          #
#                                                          #
#                                                          #
#                                                          #
#                                                          #
#                                                          #
# 0. Back                                                  #
############################################################
"""
        self.start()

    def start(self):
        print(self.MAINMENU)
        while True:
            #  A dictionary that handles users input.
            mainCommand_dict = {'1': self.getAirplanesUI, '2': self.registerAirplaneUI, 'q': QuitUI}
            user_input = input("Input a command: ")
            if user_input != '0':
                if user_input in mainCommand_dict:  #  Checks if the users input is correct.
                    for key in mainCommand_dict:
                        if user_input == key:
                            mainCommand_dict[key]() #  Calls the correct command.
                else:
                    print('Invalid command!')
            else:
                return  #  If user input is 0, returns to main menu.

    def getAirplanesUI(self):
        airplanes = [str(a) for a in self.mainObject.getAirplanesLL()]
        for line in airplanes: 
            print(line)
        input("press any key to continue.")

    def registerAirplaneUI(self):
        newAirplane = self.inputObject.addNewAirplaneIH()   # calls the item-handler for registering airplanes
        self.mainObject.addAirplaneLL(newAirplane)
        print("New airplane saved!")
        input("Press any key to continue.")
