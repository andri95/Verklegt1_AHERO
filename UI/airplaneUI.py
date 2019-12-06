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
            mainCommand_dict = {'1': self.getAirplanesUI, '2': self.registerAirplaneUI, 'q': QuitUI}
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

    def getAirplanesUI(self):
        airplanes = [str(a) for a in self.mainObject.getAirplanesLL()]
        for line in airplanes:
            print(line)
        input("press any key to continue.")

    def registerAirplaneUI(self):
        newAirplane = self.inputObject.addNewAirplaneIH()
        self.mainObject.addAirplaneLL(newAirplane)
        print("New airplane saved!")
        input("Press any key to continue.")
