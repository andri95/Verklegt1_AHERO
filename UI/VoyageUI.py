from UI.quitUI import QuitUI
from Models.voyageData import VoyageData
from Models.flightData import FlightData
from LL.mainLL import MainLL


class VoyageUI():
    def __init__(self):
        self.mainObject = MainLL()
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
            print(self.MAINMENU)
            var = input("Input a command: ")
            if var == "1":
                voyageObject_list = self.mainObject.getVoyageLL()
                for voyage in voyageObject_list:
                    print("Pilot: {} Co-Pilot: {} ".format(voyage.getPilot(), voyage.getCoPilot()))
                input("Press any key to continue.")
                break

            elif var == "2":
                print("_____First Flight_____")
                flightToDest = input("Enter an ID for the flight ")
                flightFrom = input("Where will you be flying from: ")
                flightFromDate = input("When will you be flying: (Y/M/D, TT:TT:TT): ")
                flightTo = input("Where will you be arriving at: ")
                flightToArr = input("When will you be arriving (Y/M/D, TT:TT:TT): ")
                firstFlight = FlightData(flightToDest, flightFrom, flightTo, flightFromDate, flightToArr)
                self.mainObject.addNewFlight(firstFlight)
                print("_____Second Flight_____")
                flightToDest = input("Enter an ID for the flight ")
                flightFrom = input("Where will you be flying from: ")
                flightFromDate = input("When will you be flying: (Y/M/D, TT:TT:TT): ")
                flightTo = input("Where will you be arriving at: ")
                flightToArr = input("When will you be arriving (Y/M/D, TT:TT:TT): ")
                secondFlight = FlightData(flightToDest, flightFrom, flightTo, flightFromDate, flightToArr)
                self.mainObject.addNewFlight(secondFlight)
                print("New flight saved!")
                print("----------------")
                input("Press any key to continue.")
                break
                # Addvoyage()
                # Editvoyage()
            elif var == "3":
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

            elif var == "q":
                quit()
            elif var == "0":
                return
            else:
                print("Invalid command")




