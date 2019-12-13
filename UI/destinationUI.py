from UI.quitUI import QuitUI
from LL.mainLL import MainLL
from Models.inputHandler import InputHandler
from Models.outputHandler import OutputHandler

class DestinationUI():
    ''' Destination UI has method to get, add and update destinations'''
    def __init__(self):
        '''Instances of appropriate classes created in constructor so the class
               has access to their functions. MainLL connects the class to the logic layer
               and the other classes handle inputs, outputs and errors'''
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
#                  1. All destinations                     #
#                  2. Add a new destination                #             
#                  3. Update destination                   #
#                                                          #
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
        destinationID = self.mainObject.generadeDestinationIdLL()
        newDestination.setDestinationId(destinationID)
        self.mainObject.addNewDestinationLL(newDestination)
        
        
    def updateDestinationUI(self):
        destinationObject_dict = {} # Option dictionary for user
        destinationObject_list = self.mainObject.getAllDestinationsLL()
        for counter, destination in enumerate(destinationObject_list, 1):
            destinationObject_dict[str(counter)] = destination
        self.outputObject.availableDestinationsOH(destinationObject_dict)
        dataList = self.inputObject.updateDestinationIH(destinationObject_dict)
        self.mainObject.updateDestinationLL(dataList)