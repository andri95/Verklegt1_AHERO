from UI.quitUI import QuitUI
from LL.mainLL import MainLL
from Models.destinationData import DestinationData

class DestinationUI():
    def __init__(self):
        self.mainObject = MainLL()

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
#                                                          #
#                                                          #
#                                                          #
#                                                          #
#                                                          #
#                                                          #	
#                                                          #
############################################################
"""
        self.start()

    def start(self):
        print(self.MAINMENU)
        while True:
            mainCommand_dict = {'1': self.getAllDestiantionUI, '2': self.addNewDestinationUI, 'q': QuitUI}
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

    def getAllDestiantionUI(self):
        destination_list = self.mainObject.getAllDestinationsLL()
        for destination in destination_list:
            print('Country: {} Contact Name: {} Emergency Number {}'.format(destination.getCountry(), destination.getContact(), destination.getEmergencyNumber() ))

    def addNewDestinationUI(self):
        country = input('Enter country: ')
        flighttime = input('Enter flight time: ')
        contact = input('Enter contact: ')
        emergencynum = input('Enter emergency number: ')
        newDestination = DestinationData(country, flighttime, contact, emergencynum)
        self.mainObject.addNewDestinationLL(newDestination)
