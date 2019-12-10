from UI.quitUI import QuitUI
from Models.inputHandler import InputHandler
from LL.mainLL import MainLL
NOPILOT = "No Pilot yet."
NOCOPILOT = "No Co-pilot yet."
NOFA1 = "No flight attendant nr 1 yet."
NOFA2 = "No flight attendant nr 2 yet."

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
#                      1.List voyages                      #
#                      2.Add voyage                        #
#                      3.Complete voyage                   #
#                                                          #
#                                                          #
#                                                          #				
#                                                          #
#  0.Back                                                  #
############################################################	"""
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
        voyageObject_list = self.mainObject.getVoyageLL()   #  Gets information needed from getvoyage logic layer.
        for voyage in voyageObject_list:
            print("Arriving from {} Arriving at {}".format(voyage.getDepartingFrom(),voyage.getArrivingAt()))
            print("Staff:")
            if voyage.getCaptain() == "":
                print(NOPILOT)
            else:
                print("Pilot Id: {}".format(voyage.getCaptain()))

            if voyage.getCoPilot() == "":
                print(NOCOPILOT)
            else:
                print("Co-pilot Id: {}".format(voyage.getCoPilot()))

            if voyage.getFa1() == "":
                print(NOFA1)
            else:
                print("Flight attendant 1 Id: {}".format(voyage.getFa1()))
            if voyage.getFa2() == "":
                print(NOFA2)
            else:
                print("Flight attendant 2 Id {}".format(voyage.getFa2()))
            print("\n")

           # print("Pilot Id: {} Co-pilot Id: {} \nFlight attendants Id: {}, {} ".format(voyage.getCaptain(),voyage.getCoPilot(),voyage.getFa1(),voyage.getFa2()))
            #print("\n")
        input("Press any key to continue.")


    
    def addNewVoyageUI(self):
        print("_____First Flight_____")
        firstFlight = self.inputObject.addNewFlightIH()
        if self.mainObject.generateFlightNumberLL(firstFlight) != False:
            firstFlightId = "NA" + self.mainObject.generateFlightNumberLL(firstFlight) + "0"
            firstFlight.setFlightNumber(str(firstFlightId))
            print("This fight has the Id: ", firstFlight.getFlightNumber())
        else:
            print(firstFlight.getArrivingAt(), "is not a valid destination")
        self.mainObject.addNewVoyageLL(firstFlight)
        #print("This flight was given the number", firstFlightId)
        print("_____Second Flight_____")
        secondFlight = self.inputObject.addNewFlightIH()
        secondflightId = "NA"+self.mainObject.generateFlightNumberLL(firstFlight) + "1"
        secondFlight.setFlightNumber(str(secondflightId))
        self.mainObject.addNewVoyageLL(secondFlight)
        print("This flight was given the number", secondflightId)
        print("New Voyage saved! You can complete it now in 'complete voyage'")
        print("----------------")
        input("Press any key to continue.")


    def completeVoyageUI(self):
        counter = 0
        voyageDict = {}
        flightObject_list = self.mainObject.getVoyageLL()
        for number1, flight1 in enumerate(flightObject_list):
            for number2, flight2 in enumerate(flightObject_list):
                if number2 - number1 == 1 and number1 % 2 == 0:
                    counter += 1
                    voyageDict[counter] = [flight1, flight2]
                    print("{}: {} --> {}, {} --> {}\n".format(counter, flight1.getDepartingFrom(),
                        flight1.getArrivingAt(),flight2.getDepartingFrom(), flight2.getArrivingAt()))

        pickVoyage = int(input("Pick a voyage to complete: "))
        if pickVoyage != 0:
            if pickVoyage in voyageDict:
                for key, val in voyageDict.items():
                    if pickVoyage == key:
                        staffList = self.inputObject.updateVoyageIH()
                        self.mainObject.updateVoyageLL(val, staffList)
            else:
                print("Invalid Voyage")
        else:
            return











