from UI.quitUI import QuitUI
from Models.inputHandler import InputHandler
from Models.outputHandler import OutputHandler
from Models.errorHandler import ErrorHandler
from LL.mainLL import MainLL


class AirplaneUI:
    def __init__(self):
        ''' Appropriate classes initiated in constructor so the airplaneUI has access to 
            them. mainObject connects it to the MainLL class and so on.'''

        self.mainObject = MainLL()
        self.inputObject = InputHandler()
        self.outputObject = OutputHandler()
        self.errorObject = ErrorHandler()
        self.MAINMENU = """
############################################################
#                           _|_	               quit(q)     #
#                   --@--@--(_)--@--@--                    #
#__________________________________________________________#
#                                                          #
#                       Airplanes                          #
#                                                          #
#                   1. List Airplanes                      #
#                   2. Add airplanes                       #
#                   3. Airplane status                     #
#                   4. Add licensed pilot                  #
#                   5. Licensed pilots                     #
#                   6. Find airplane by ID                 #
#                   7. Number of flights by Airplane       #
#                                                          #
#                                                          #
#                                                          #
#  back(b)                                                 #
############################################################
"""     
        # start called in constructor so that start runs as son as AirplaneUI instance is initiated.
        self.start()

    def start(self):
        
        while True:
            print(self.MAINMENU)
            #  A dictionary that handles users input.
            mainCommand_dict = {'1': self.getAirplanesUI, '2': self.registerAirplaneUI,'3': self.airplaneStatusUI, '4': self.addLicenseUI,'5': self.getLicenseDictUI,
                                 '6': self.getAirplaneByIdUI, '7': self.MostpopularUI,'q': QuitUI}
            user_input = input("Input a command: ")
            if user_input != 'b':
                if user_input in mainCommand_dict:  #  Checks if the users input is correct.
                    for key in mainCommand_dict:
                        if user_input == key:
                            mainCommand_dict[key]() #  Calls the correct command.
                else:
                    print('Invalid command!')
            else:
                return  #  If user input is 0, returns to main menu.

    '''Calls getAirplanesLL (list of airplane objects) function in mainObject into variable,
     returns function in outputObject'''
    def getAirplanesUI(self):
        airplaneObject_list = self.mainObject.getAirplanesLL()
        return self.outputObject.allAirplanesOH(airplaneObject_list)

    '''Creates list of all voyages (objects), counts how many times each airplane occurrs. Results are put
       into dictionary and contents of dictionary are printed'''
    def MostpopularUI(self):
        voyageObject_list = self.mainObject.getVoyageLL()
        Popular_dict = {}
        for voyage in voyageObject_list:
            if voyage.getAircraftId() not in Popular_dict:
                Popular_dict[voyage.getAircraftId().upper()] = 1
            else:
                Popular_dict[voyage.getAircraftId().upper()] +=1
        print("Number of flights flown by each airplane:")
        for key,val in Popular_dict.items():
            print("The airplane {} has flown {} times.".format(key,val))
        input("Enter any key to continue: ")

    '''Creates dictionary of all airplane objects with numbers as value. User selects desired airplane
       and the selected airplanes id is passed down into the logic layer where the airplane object is found.
       The airplane object is then passed into outputObject where detailed information is printed'''
    def getAirplaneByIdUI(self):
        airplaneIdList = self.mainObject.getAirplanesLL()
        airplaneIdDict = {}
        for i, airplane in enumerate(airplaneIdList, 1):
            airplaneIdDict[str(i)] = airplane.getPlaneId()
        self.outputObject.singleAirplanelistOH(airplaneIdList)
        input_airId = input("Enter Airplane ID number: ")
        while input_airId not in airplaneIdDict:
            print("Sorry that was not a valid airplane")
            input_airId = input("Enter Airplane ID number: ")
        license_dict = self.mainObject.getAirplaneByIdLL(airplaneIdDict[input_airId])
        self.outputObject.singleAirplaneIdOH(license_dict)  # held

    '''inputObject.addNewAirplaneIH is called into newAirplane variable. (airplane object) is then passed
    down into logic layer through MainLL'''
    def registerAirplaneUI(self):
        newAirplane = self.inputObject.addNewAirplaneIH()   # calls the input-handler for registering airplanes
        self.mainObject.addAirplaneLL(newAirplane)
        print("\nNew airplane saved!")
        input("Press any key to continue.")

    '''User inputs date and time which is then passed into getAirplaneStatusLL. Return value is dictionary with
       airplane ID as key and status as value. Dictionary then passed into outputObject where the information is printed'''
    def airplaneStatusUI(self):
        flagDate = True
        flagTime = True
        while flagDate:
            date = input('Enter date "YYYY-MM-DD": ')
            if self.errorObject.errorCheckDateEH(date):
                flagDate = False
            else:
                continue
        while flagTime:
            time = input('Enter time "HH:MM": ')
            if self.errorObject.errorCheckTimeEH(time):
                flagTime = False
            else:
                continue
        airplaneStatus_dict = self.mainObject.getAirplaneStatusLL(date, time)
        self.outputObject.airplaneStatusOH(airplaneStatus_dict)

    '''List of all pilots (objects) called into variable. Dictionary created with number as key and staff object as value.
       All pilots are printed onto screen with outputhandler. Inputhandler function called into dataList and datalist is then
       passed down into logic layer.'''
    def addLicenseUI(self):
        pilotObject_dict = {}
        pilotObject_list = self.mainObject.getAllPilotsLL()
        for counter, pilot in enumerate(pilotObject_list):
            pilotObject_dict[str(counter)] = pilot
        self.outputObject.allPilotsLicenseOH(pilotObject_dict)
        dataList = self.inputObject.addLicenseIH(pilotObject_dict)
        return self.mainObject.addLicenseLL(dataList)

    '''getLicenseDictLL called into variable, passes variable into outputObject where information is printed'''
    def getLicenseDictUI(self):
        licenseObject_dict = self.mainObject.getLicenseDictLL()
        return self.outputObject.airplaneLicensedOH(licenseObject_dict)

    
