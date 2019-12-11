from UI.quitUI import QuitUI
from Models.inputHandler import InputHandler
from Models.outputHandler import OutputHandler
from LL.mainLL import MainLL
from Models.voyageData import VoyageData
NOPILOT = "No Pilot yet."
NOCOPILOT = "No Co-pilot yet."
NOFA1 = "No flight attendant nr 1 yet."
NOFA2 = "No flight attendant nr 2 yet."

class VoyageUI:
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
#                         Voyage                           #
#                                                          #
#                      1.List voyages                      #
#                      2.Add voyage                        #
#                      3.Complete voyage                   #
#                      4.Most popular voyage               #
#                                                          #
#                                                          #
#                                                          #				
#                                                          #
#  back(b)                                                 #
############################################################	"""
        self.start()

    def start(self):

        while True:
            mainCommand_dict = {'1': self.getVoyagesUI, '2': self.addNewVoyageUI, '3': self.completeVoyageUI, '4':self.PopularVoyageUI,'q': QuitUI}
            print(self.MAINMENU)
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

    def PopularVoyageUI(self):
        voyageObject_list = self.mainObject.getVoyageLL()
        flights_dict = {}
        for voyage in voyageObject_list:
            if voyage.getArrivingAt() not in flights_dict:
                flights_dict[voyage.getArrivingAt().upper()] = 1
            else:
                flights_dict[voyage.getArrivingAt().upper()] +=1
        del flights_dict["KEF"]
        maximum = max(flights_dict, key=flights_dict.get)

        print("The most popular destination is {}, With {} flights!".format(maximum,flights_dict[maximum]))
        input("Press any key to continue: ")   
            
    def getVoyagesUI(self):
        voyageObject_list = self.mainObject.getVoyageLL()   #  Gets information needed from getvoyage logic layer.

        self.outputObject.allVoyagesOH(voyageObject_list)
    
    def addNewVoyageUI(self):
        print("_____First Flight_____")
        print("Pick a destination that Nan Air flys to:")
        dest = self.mainObject.destinationObject.getDestination()
        for d in dest:
            print("{}\t".format(d.getCountry()))
        #self.mainObject.voyageObject.findAvalibleAirplanes()
        firstFlight = self.inputObject.addNewFlightIH()
        arrivalTime = self.mainObject.voyageObject.findArrivalTime(firstFlight)
        if arrivalTime != False:
            firstFlight.setArrivalTime(str(arrivalTime))
        else:
            print("Sorry we dont fly to ", firstFlight.getArrivingAt())
            return None
        assignedAirplane = self.mainObject.voyageObject.findAvalibleAirplanes(firstFlight)
        if assignedAirplane != False:
            firstFlight.setAircraftId(str(assignedAirplane))
        else:
            print("Sorry, there are no avalible airplanes at this Time :(")
            return None
        firstFlightId = "NA" + self.mainObject.generateFlightNumberLL(firstFlight) + "00"
        if firstFlightId != False:
            firstFlight.setFlightNumber(str(firstFlightId))
            print("The flight {} was assigned the airplane {} \n It will arrive at {}".format(firstFlight.getFlightNumber(), firstFlight.getAircraftId(), arrivalTime))

        else:
            print(firstFlight.getArrivingAt(), "is not a valid destination")
            return None
        self.mainObject.addNewVoyageLL(firstFlight)

        print("_____Second Flight_____")
        departingFrom, arravingAt, DeparturTime, airplaneId = self.mainObject.voyageObject.generateSecondFlight(firstFlight)
        secondFlight = VoyageData("", departingFrom, arravingAt, DeparturTime, "", airplaneId)
        secondFlightId = "NA" + self.mainObject.generateFlightNumberLL(firstFlight) + "01"
        arrivalTimeSecondFlight = self.mainObject.voyageObject.findArrivalTime(secondFlight)
        secondFlight.setFlightNumber(str(secondFlightId))

        secondFlight.setArrivalTime(arrivalTimeSecondFlight)
        self.mainObject.addNewVoyageLL(secondFlight)
        print("The flight {} was assigned the airplane {} \n It will arrive at {}\n".format(secondFlight.getFlightNumber(),
                                                                                          secondFlight.getAircraftId(),
                                                                                          arrivalTimeSecondFlight))

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
                    if flight1.getCaptain() == "" and flight2.getCaptain() == "":
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











