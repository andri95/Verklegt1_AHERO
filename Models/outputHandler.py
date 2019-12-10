#import dateutil.parser

EMPLOYEES = '_______ Employees _______'
EMPLOYEE = '_______ Employee _______'
PILOTS = '_______ Pilots _______'
CABINCREW = '_______ Cabin Crew _______'
AIRPLANES = '_______ Airplanes _______'
DESTINATIONS = '_______ Destinations _______'
VOYAGES = '_______ Voyages _______'
AVAILABLE = "_______ Available Staff _______"
NOPILOT = "No Pilot yet."
NOCOPILOT = "No Co-pilot yet."
NOFA1 = "No flight attendant nr 1 yet."
NOFA2 = "No flight attendant nr 2 yet."
ANYKEY = 'Press any key to continue.'

class OutputHandler:

    def allStaffOH(self, staffObject_list):
        print('\n{:^75}'.format(EMPLOYEES))
        print('\n{:<20} {:<11} {:<9} {:<20} {:<21}\n'.format('Name', 'SSN', 'Phone', 'Email', 'Rank'))
        for staffMember in staffObject_list:
            print('{:<20} {:<11} {:<9} {:<20} {:<21}'.format(staffMember.getName(), staffMember.getSSN(), staffMember.getCellPhone(),
                                                    staffMember.getEmail(), staffMember.getRank()))
        input(ANYKEY)


    def allPilotsOH(self, pilotObject_list):
        print('\n{:^81}'.format(PILOTS))
        print('\n{:<20} {:<11} {:<9} {:<20} {:<9} {:<12}\n'.format('Name', 'SSN', 'Phone', 'Email', 'Rank', 'License'))
        for staffMember in pilotObject_list:
            print('{:<20} {:<11} {:<9} {:<20} {:<9} {:<12}'.format(staffMember.getName(), staffMember.getSSN(), staffMember.getCellPhone(),
                                                    staffMember.getEmail(), staffMember.getRank(), staffMember.getLicense()))
        input(ANYKEY)

    def allCabinCrewOH(self, cabinCrewObject_list):
        print('\n{:^81}'.format(CABINCREW))
        print('\n{:<20} {:<11} {:<9} {:<20} {:<21}\n'.format('Name', 'SSN', 'Phone', 'Email', 'Rank'))
        for staffMember in cabinCrewObject_list:
            print('{:<20} {:<11} {:<9} {:<20} {:<21}'.format(staffMember.getName(), staffMember.getSSN(), staffMember.getCellPhone(),
                                                    staffMember.getEmail(), staffMember.getRank()))
        input(ANYKEY)

    def singleStaffListOH(self, staffObject_list):
        print('\n{:^30}'.format(EMPLOYEES))
        print('\n{:<20} {:<11}\n'.format('Name', 'SSN'))
        for staffMember in staffObject_list:
            print('{:<20} {:<11}'.format(staffMember.getName(), staffMember.getSSN()))

    def singleStaffHeaderOH(self):
        print('\n{:^75}'.format(EMPLOYEE))
        print('\n{:<20} {:<11} {:<9} {:<20} {:<21}\n'.format('Name', 'SSN', 'Phone', 'Email', 'Rank'))

    def singleStaffOH(self, staffMember):
        print('{:<20} {:<11} {:<9} {:<20} {:<21}'.format(staffMember.getName(), staffMember.getSSN(), staffMember.getCellPhone(),
                                                    staffMember.getEmail(), staffMember.getRank()))
        input(ANYKEY)

    def allAirplanesOH(self, airplaneObject_list):
        print('\n{:^32}'.format(AIRPLANES))
        print('\n{:<12} {:<7} {:<5} {:<8}'.format('ID', 'Type', 'Model', 'Capacity'))
        for airplane in airplaneObject_list:
            print('{:<12} {:<7} {:<5} {:<8}'.format(airplane.getPlaneId(), airplane.getType(), airplane.getModel(), airplane.getCapacity()))
        input(ANYKEY)

    def allDestinationsOH(self, destinationObject_list):
        print('\n{:^32}'.format(DESTINATIONS))
        print('\n{:<12} {:<9} {:<17}'.format('Country', 'Contact', 'Emergency Number'))
        for destination in destinationObject_list:
            print('{:<12} {:<9} {:<17}'.format(destination.getCountry(), destination.getContact(), destination.getEmergencyNumber()))
        input(ANYKEY)

    def allVoyagesOH(self, voyageObject_list):
        counter = 0
        print('\n{:^32}'.format(VOYAGES))
        for voyage in voyageObject_list:
            departureDateTime = voyage.getDepartureTime()
            parsedDateObject = dateutil.parser.parse(departureDateTime)
            print("Departing from: {} - Arriving at: {}".format(voyage.getDepartingFrom(),voyage.getArrivingAt()))
            print('\n{:<5} {:<5}'.format('Date', 'Time'))
            print('\n{:<9} {:<9}'.format(str(parsedDateObject.day) + '-' + str(parsedDateObject.month) + str(parsedDateObject.year), str(parsedDateObject.hour)))
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
            
            counter += 1

           # print("Pilot Id: {} Co-pilot Id: {} \nFlight attendants Id: {}, {} ".format(voyage.getCaptain(),voyage.getCoPilot(),voyage.getFa1(),voyage.getFa2()))
            #print("\n")
        input(ANYKEY)
    
    def availableDatesOH(self, availableDates_list):
        print('\n_______ Avaliable Dates _______\n')
        for date in availableDates_list:
            print(date)
        print()

    def workScheduleOH(self, workDict):
        counter = 0
        if len(workDict) != 0:
            for voyage in workDict:
                if len(workDict[voyage]) != 0:
                    print("\n\t_______ Voyage arriving at {} _______".format(voyage))
                    print('\n{:<20} {:<11} {:<21}'.format('Name', 'SSN', 'Rank'))
                    for staffMember in workDict[voyage]:
                        print('{:<20} {:<11} {:<21}'.format(staffMember.getName(), staffMember.getSSN(), staffMember.getRank()))
                else:
                    counter += 1
        else:
            print('\nNo staff working on this date!')

        if counter == len(workDict):
            print('\nNo staff working on this date!')

        input(ANYKEY)

    def workScheduleAvailableOH(self, availableStaff):
        print('\n{:^53}'.format(AVAILABLE))
        print('\n{:<20} {:<11} {:<21}'.format('Name', 'SSN', 'Rank'))
        for staffMember in availableStaff:
            print('{:<20} {:<11} {:<21}'.format(staffMember.getName(), staffMember.getSSN(), staffMember.getRank()))

        input(ANYKEY)

    def testPrint(self, testDict):
        for key, valu in testDict.items():
            print(key,valu)
