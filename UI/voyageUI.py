from UI.quitUI import QuitUI
from Models.inputHandler import InputHandler
from LL.mainLL import MainLL


class VoyageUI:
    def __init__(self):
        self.mainObject = MainLL()
        self.inputObject = InputHandler()
        self.MAINMENU = """Verklegt1_AHERO"""
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
            print("Pilot Id: {} Co-pilot Id: {} \nFlight attendants Id: {}, {} ".format(voyage.getCaptain(),voyage.getCoPilot(),voyage.getFa1(),voyage.getFa2()))
            print("\n")
        input("Press any key to continue.")
    
    def addNewVoyageUI(self):
        print("_____First Flight_____")
        firstFlight = self.inputObject.addNewFlightIH()
        self.mainObject.addNewVoyageLL(firstFlight)
        print("_____Second Flight_____")
        secondFlight = self.inputObject.addNewFlightIH()
        self.mainObject.addNewVoyageLL(secondFlight)
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











