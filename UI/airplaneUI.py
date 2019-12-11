from UI.quitUI import QuitUI
from Models.inputHandler import InputHandler
from Models.outputHandler import OutputHandler
from LL.mainLL import MainLL


class AirplaneUI:
    def __init__(self):

        self.mainObject = MainLL()
        self.inputObject = InputHandler()
        self.outputObject = OutputHandler()
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
#                   3. Add licensed pilot                  #
#                   4. Pilot license                       #
#                                                          #
#                                                          #
#                                                          #
#                                                          #
#  back(b)                                                 #
############################################################
"""
        self.start()

    def start(self):
        
        while True:
            print(self.MAINMENU)
            #  A dictionary that handles users input.
            mainCommand_dict = {'1': self.getAirplanesUI, '2': self.registerAirplaneUI, '3': self.addLicenseUI,'4': self.getLicenseDictUI ,'q': QuitUI}
            user_input = input("Input a command: ")
            if user_input != 'b':
                if user_input in mainCommand_dict:  #  Checks if the users input is correct.
                    for key in mainCommand_dict:
                        if user_input == key:
                            mainCommand_dict[key]() #  Calls the correct command.
                else:
                    print('Invalid command!')
            else:
                return  #  If user input is 0, returns to main menu.

    def getAirplanesUI(self):
        airplaneObject_list = self.mainObject.getAirplanesLL()
        return self.outputObject.allAirplanesOH(airplaneObject_list)

    def registerAirplaneUI(self):
        newAirplane = self.inputObject.addNewAirplaneIH()   # calls the item-handler for registering airplanes
        self.mainObject.addAirplaneLL(newAirplane)
        print("New airplane saved!")
        input("Press any key to continue.")

    def addLicenseUI(self):
        pilotObject_list = self.mainObject.getAllPilotsLL()
        self.outputObject.allPilotsLicenseOH(pilotObject_list)
        dataList = self.inputObject.addLicenseIH()
        return self.mainObject.addLicenseLL(dataList)

    def getLicenseDictUI(self):
        licenseObject_dict = self.mainObject.getLicenseDictLL()
        return self.outputObject.testPrint(licenseObject_dict)
