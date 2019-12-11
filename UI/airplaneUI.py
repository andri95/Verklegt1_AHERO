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
#                   5. Find airplane by ID                 #
#                   6. Number of flights by Airplane       #
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
            mainCommand_dict = {'1': self.getAirplanesUI, '2': self.registerAirplaneUI, '3': self.addLicenseUI,'4': self.getLicenseDictUI,'5': self.getAirplaneByIdUI, '6': self.MostpopularUI, 'q': QuitUI}
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

    
    def MostpopularUI(self):
        voyageObject_list = self.mainObject.getVoyageLL()
        Popular_dict = {}
        for voyage in voyageObject_list:
            if voyage.getAircraftId() not in Popular_dict:
                Popular_dict[voyage.getAircraftId().upper()] = 1
            else:
                Popular_dict[voyage.getAircraftId().upper()] +=1
        print("Number of flights flown by each airplane:")
        for key,val in Popular_dict.items():
            print("The airplane {} has flown {} times.".format(key,val))
        input("Enter any key to continue: ")

    def getAirplaneByIdUI(self):
        airplaneId_list = self.mainObject.getAirplanesLL()
        self.outputObject.singleAirplanelistOH(airplaneId_list)  # held
        input_airId = input("Enter Airplane ID number: ")
        license_dict = self.mainObject.getAirplaneByIdLL(input_airId)
        self.outputObject.singleAirplaneIdOH(license_dict)  # held

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
