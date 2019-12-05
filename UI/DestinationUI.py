from UI.quitUI import Goodbye
from LL.mainLL import MainLL
from Models.destinationData import DestinationData

class DestinationMenu():
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
            var = input("Input a command: ")
            if var == "1":
                self.getAllDestiantionUI()
                
            elif var == "2":
                self.addNewDestinationUI()

            elif var == "q":
                Goodbye()

            elif var == "0":
                return

            else:
                print("Invalid command")


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
