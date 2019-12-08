from UI.quitUI import QuitUI
from Models.inputHandler import InputHandler
from LL.mainLL import MainLL


class VoyageUI:
    def __init__(self):
        self.mainObject = MainLL()
        self.inputObject = InputHandler()
        self.MAINMENU = """
############################################################
#                           _|_	               quit(q)     #
#                   --@--@--(_)--@--@--                    #
#__________________________________________________________#
#                                                          #
#                         Voyage                           #
#                                                          #
#                 1.List voyages                           #
#                 2.Add voyage                             #
#                 3.Complete Voyage                        #
#                                                          #
#                                                          #
#                                                          #
#                                                          #
#                                                          #
#                                                          #
#  0.Back                                                  #
############################################################	
"""
        self.start()

    def start(self):

        while True:
            mainCommand_dict = {'1': self.getVoyagesUI, '2': self.addNewVoyageUI, '3': self.completeVoyageUI, 'q': QuitUI}
            print(self.MAINMENU)
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
                

    def getVoyagesUI(self):
        voyageObject_list = self.mainObject.getVoyageLL()
        for voyage in voyageObject_list:
            print("Pilot: {} Co-Pilot: {} ".format(voyage.getPilot(), voyage.getCoPilot()))
        input("Press any key to continue.")
    
    def addNewVoyageUI(self):
        print("_____First Flight_____")
        firstFlight = self.inputObject.addNewFlightIH()
        self.mainObject.addNewFlight(firstFlight)
        print("_____Second Flight_____")
        secondFlight = self.inputObject.addNewFlightIH()
        self.mainObject.addNewFlight(secondFlight)
        print("New flight saved!")
        print("----------------")
        input("Press any key to continue.")
        # Addvoyage()
        # Editvoyage()

    def completeVoyageUI(self):
        counter = 0
        flightObject_list = self.mainObject.getFlightsLL()
        for number1, flight1 in enumerate(flightObject_list):
            for number2, flight2 in enumerate(flightObject_list):
                if number2 - number1 == 1 and number1 % 2 == 0:
                    counter += 1
                    print("{}: {} --> {}, {} --> {}\n".format(counter, flight1.getDepartingFrom(),
                                                                flight1.getArrivingAt(),
                                                                flight2.getDepartingFrom(),
                                                                flight2.getArrivingAt()))

                    # {1: flight1, flight2 2: }
        print("Pick a voyage to complete")