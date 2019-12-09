from UI.quitUI import QuitUI
from Models.inputHandler import InputHandler
from LL.mainLL import MainLL
NOPILOT = "No Pilot yet."
NOCOPILOT = "No Co-pilot yet."
NOFA1 = "No flight attendant nr 1 yet."
NOFA2 = "No flight attendant nr 2 yet."

class VoyageUI():
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
            #  A dictionary that handles users input.
            mainCommand_dict = {'1': self.getVoyagesUI, '2': self.addNewVoyageUI, '3': self.completeVoyageUI, 'q': QuitUI}
            print(self.MAINMENU)
            user_input = input("Input a command: ")
            if user_input != '0':
                if user_input in mainCommand_dict: #  Checks if the users input is correct.
                    for key in mainCommand_dict:   
                        if user_input == key:  
                            mainCommand_dict[key]() #  Calls the correct command.
                else:
                    print('Invalid command!')
            else:
                return      #  If user input is 0, returns to main menu.
                

    def getVoyagesUI(self):
        voyageObject_list = self.mainObject.getVoyageLL()   #  Gets information needed from getvoyage logic layer.
        for voyage in voyageObject_list:
            print("Arriving from {} Arriving at {}".format(voyage.getDepartingFrom(),voyage.getArrivingAt()))
            print("Staff:")
            if voyage.getCaptain() == "":
                voyage.getCaptain() = NOPILOT
            if voyage.getCoPilot() == "":
                voyage.getCopilot() == NOCOPILOT
            if voyage.getFa1() == "":
                voyage.getFa1() == NOFA1
            if voyage.getFa2() == "":
                voyage.getFa2() == NOFA2

            print("Pilot Id: {} Co-pilot Id: {} \nFlight attendants Id: {}, {} ".format(voyage.getCaptain(),voyage.getCoPilot(),voyage.getFa1(),voyage.getFa2()))
            print("\n")
        input("Press any key to continue.")
    
    def addNewVoyageUI(self):
        print("_____First Flight_____")
        firstFlight = self.inputObject.addNewFlightIH()     #  Calls the item-handler for first flight.
        self.mainObject.addNewFlight(firstFlight)          
        print("_____Second Flight_____")
        secondFlight = self.inputObject.addNewFlightIH()    # Calls the item-handler for the second flight   
        self.mainObject.addNewFlight(secondFlight)
        print("New flight saved!")
        print("----------------")
        input("Press any key to continue.")
    

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



 




885
