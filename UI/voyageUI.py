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
            mainCommand_dict = {'1': self.getVoyagesUI, '2': self.addNewVoyageUI, '3': self.completeVoyageUI, '4':self.popularVoyageUI,'q': QuitUI}
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

    def popularVoyageUI(self):
        voyageObject_list = self.mainObject.getVoyageLL()
        flights_dict = {}
        for voyage in voyageObject_list:
            if voyage.getArrivingAt() not in flights_dict:
                flights_dict[voyage.getArrivingAt().lower()] = 1
            else:
                flights_dict[voyage.getArrivingAt().lower()] +=1
        del flights_dict["keflavik"]
        maximum = max(flights_dict, key=flights_dict.get)

        print("The most popular destination is {}, With {} flights!".format(maximum,flights_dict[maximum]))
        input("Press any key to continue: ")   
            
    def getVoyagesUI(self):
        voyageObject_list = self.mainObject.getVoyageLL()   #  Gets information needed from getvoyage logic layer.
        self.outputObject.allVoyagesOH(voyageObject_list)

    def createOptionDestDict(self, options):
        dictonary = {}


    
    def addNewVoyageUI(self):
        print('  ______Create a Voyage ______')
        print(" Pick a destination that Nan Air flys to:")
        destinationObject_list = self.mainObject.getAllDestinationsLL()
        self.outputObject.voyageDestinationOH(destinationObject_list)
        destDict = {}
        for i, dest in enumerate(destinationObject_list):
            if dest.getCountry() == "keflavik":
                pass
            else:
                destDict[i] = dest.getCountry()
        departingFromKef = "keflavik"
        pickDest = int(input("Where will you be arriving at: "))
        firstFlight = self.inputObject.addNewFlightIH()
        firstFlight.setDepartingFrom(departingFromKef)
        firstFlight.setArrivingAt(destDict[pickDest])
        if self.mainObject.voyageObject.errorCheckDate(firstFlight) == False:
            return None
        if self.mainObject.voyageObject.flightCollision(firstFlight) == True:
            print("You will cause a collision, do you really want to do that?")
            print("Every flight must have one hour between them")
            return None
        arrivalTime = self.mainObject.voyageObject.findArrivalTime(firstFlight)
        if arrivalTime != False:
            firstFlight.setArrivalTime(str(arrivalTime))
        else:
            print("Sorry you entered a invalid destination")
            return None
        assignedAirplane = self.mainObject.voyageObject.findAvalibleAirplanes(firstFlight)
        if assignedAirplane != False:
            firstFlight.setAircraftId(str(assignedAirplane))
        else:
            print("Sorry, there are no avalible airplanes at this Time :(")
            return None
        firstFlightId = self.mainObject.generateFlightNumberLL(firstFlight)
        if firstFlightId != False:
            firstFlight.setFlightNumber(str(firstFlightId))

        else:
            print(firstFlight.getArrivingAt(), "is not a valid destination")
            return None
        self.mainObject.addNewVoyageLL(firstFlight)

        departingFrom, arravingAt, DeparturTime, airplaneId = self.mainObject.voyageObject.generateSecondFlight(firstFlight)
        secondFlight = VoyageData("", departingFrom, arravingAt, DeparturTime, "", airplaneId)
        secondFlightId = self.mainObject.generateFlightNumberLL(firstFlight)
        arrivalTimeSecondFlight = self.mainObject.voyageObject.findArrivalTime(secondFlight)
        secondFlight.setFlightNumber(str(secondFlightId))

        secondFlight.setArrivalTime(arrivalTimeSecondFlight)
        self.mainObject.addNewVoyageLL(secondFlight)
        print()
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
                        flightTime = flight1.getDepartureTime().split("T")
                        print("{}.{:<4} ---> {:<9}  {:<10}---> {:<14}\n {} {} {}\n".format(counter, flight1.getDepartingFrom(),
                        flight1.getArrivingAt(),flight2.getDepartingFrom(), flight2.getArrivingAt(), "Departing at", flightTime[0], flightTime[1]))
        print("Press 0 if your want to cancel")
        if voyageDict == {}:
            print("There are no voyages to complete!")
            return None
        pickVoyage = int(input("Pick a voyage to complete: "))
        if pickVoyage != 0:
            if pickVoyage in voyageDict:
                for key, val in voyageDict.items():
                    if pickVoyage == key:
                        pilotObject_list = self.mainObject.getAllPilotsLL()
                        cabinCrewObject_list = self.mainObject.getAllCabinCrewLL()
                        staffObject_list = self.mainObject.getAllStaffLL()
                        #staffList = self.inputObject.updateVoyageIH()  # COMMENTAÐI UT INPUT HANDLER::
                        staff_list = []
                        print("\n______ Available Captains ______")
                        availableCaptains = self.mainObject.getAvailableCaptains(val[0])  ####HEHEH
                        captainDict = {}
                        for i, captain in enumerate(availableCaptains, 1):
                            captainDict[i] = captain.getName()
                            print(str(i) + ".",captain.getName())
                        captainOfChoice = int(input("\nEnter a Captain: "))
                        staff_list.append(captainDict[captainOfChoice])

                        print("\n______ Available Co-Pilots ______")
                        coPilotDict = {}
                        availableCoPilots = self.mainObject.getAvailableCoPilots(val[0])  ####HEHEH
                        for k, coPilot in enumerate(availableCoPilots, 1):
                            coPilotDict[k] = coPilot.getName()
                            print(str(k) + ".",coPilot.getName())
                        coPilotOfChoice = int(input("\nEnter a Co-Pilots: "))
                        staff_list.append(coPilotDict[coPilotOfChoice])

                        print("\n ______ Available flight service managers ______")
                        fsmDict = {}
                        availableFlightServicerManagers = self.mainObject.getAvailableFlightServiceManagers(val[0])
                        for x, flightServiceManager in enumerate(availableFlightServicerManagers, 1):
                            fsmDict[x] = flightServiceManager
                            print(str(x) + ".", flightServiceManager)
                        fsmOfChoice = int(input("\nEnter a flight service manager: "))
                        staff_list.append(fsmDict[fsmOfChoice])

                        print("\n ______ Available flight attendants ______")
                        cabinCrewDict = {}
                        availableFlightAttendants = self.mainObject.getAvailableFlightAttendants(val[0])
                        for l, flightAttendant in enumerate(availableFlightAttendants, 1):
                            cabinCrewDict[l] = flightAttendant
                            print(str(l) + ".", flightAttendant)
                        attendatOfChoice = int(input("\nEnter a flight attendant:  "))
                        staff_list.append(cabinCrewDict[attendatOfChoice])
                        print(staff_list)

                        errorChecked = self.inputObject.updateVoyageIH(staff_list, pilotObject_list, cabinCrewObject_list, staffObject_list)
                        self.mainObject.updateVoyageLL(val, errorChecked)
            else:
                print("Invalid Voyage")
        else:
            return













