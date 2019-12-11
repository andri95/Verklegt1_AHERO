from UI.quitUI import QuitUI
from LL.mainLL import MainLL
from Models.inputHandler import InputHandler
from Models.outputHandler import OutputHandler

class DestinationUI():
    def __init__(self):
        self.mainObject = MainLL()
        self.inputObject = InputHandler()
        self.outputObject = OutputHandler()

        self.MAINMENU = """
############################################################
#                           _|_	               quit(q)     #
#                   --@--@--(_)--@--@--                    #
#__________________________________________________________#
#                      Destinations                        #	   			   
#                                                          #
#                                                          #
#                                                          #  
#                  1. All destinations                     #
#                  2. Add a new destination                #             
#                  3. Update destination                   #
#                  4. Most popular destination             #
#                                                          #
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
            mainCommand_dict = {'1': self.getAllDestiantionUI, '2': self.addNewDestinationUI,
                                '3': self.updateDestinationUI, 'q': QuitUI}
            user_input = input("Input a command: ")
            if user_input != 'b':
                if user_input in mainCommand_dict:
                    for key in mainCommand_dict:
                        if user_input == key:
                            mainCommand_dict[key]()
                else:
                    print('Invalid command!')
            else:
                return

    def getAllDestiantionUI(self):
        destinationObject_list = self.mainObject.getAllDestinationsLL()
        return self.outputObject.allDestinationsOH(destinationObject_list)

    def addNewDestinationUI(self):
        newDestination = self.inputObject.addNewDestinationIH()
        destinationID = self.mainObject.destinationObject.generadeDestinationId()
        newDestination.setDestinationId(destinationID)
        self.mainObject.addNewDestinationLL(newDestination)
        
        

    def updateDestinationUI(self):
        dataList = self.inputObject.updateDestinationIH()
        self.mainObject.updateDestinationLL(dataList)