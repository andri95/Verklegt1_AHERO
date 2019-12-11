import dateutil.parser

EMPLOYEES = '_______ Employees _______'
EMPLOYEE = '_______ Employee _______'
PILOTS = '_______ Pilots _______'
CABINCREW = '_______ Cabin Crew _______'
AIRPLANES = '_______ Airplanes _______'
DESTINATIONS = '_______ Destinations _______'
VOYAGES = '_______ Voyages _______'
AVAILABLE = "_______ Available Staff _______"
WORKSCHEDULE = '_______ Work Schedule _______'
NOPILOT = "No Captain yet."
NOCOPILOT = "No Copilot yet."
NOFA1 = "No Flight Service Manager yet."
NOFA2 = "No Flight Attendant yet."
ANYKEY = 'Press any key to continue.'
LICENSE = 'Airplane License'

class OutputHandler:

    def allStaffOH(self, staffObject_list):
        print('\n{:^75}'.format(EMPLOYEES))
        print('\n{:<20} {:<11} {:<9} {:<20} {:<21}'.format('Name', 'SSN', 'Phone', 'Email', 'Rank'))
        for staffMember in staffObject_list:
            print('{:<20} {:<11} {:<9} {:<20} {:<21}'.format(staffMember.getName(), staffMember.getSSN(), staffMember.getCellPhone(),
                                                    staffMember.getEmail(), staffMember.getRank()))
        input(ANYKEY)

    def allPilotsOH(self, pilotObject_list):
        print('\n{:^81}'.format(PILOTS))
        print('\n{:<20} {:<11} {:<9} {:<20} {:<9} {:<12}'.format('Name', 'SSN', 'Phone', 'Email', 'Rank', 'License'))
        for staffMember in pilotObject_list:
            print('{:<20} {:<11} {:<9} {:<20} {:<9} {:<12}'.format(staffMember.getName(), staffMember.getSSN(), staffMember.getCellPhone(),
                                                    staffMember.getEmail(), staffMember.getRank(), staffMember.getLicense()))
        input(ANYKEY)

    def allCabinCrewOH(self, cabinCrewObject_list):
        print('\n{:^81}'.format(CABINCREW))
        print('\n{:<20} {:<11} {:<9} {:<20} {:<21}'.format('Name', 'SSN', 'Phone', 'Email', 'Rank'))
        for staffMember in cabinCrewObject_list:
            print('{:<20} {:<11} {:<9} {:<20} {:<21}'.format(staffMember.getName(), staffMember.getSSN(), staffMember.getCellPhone(),
                                                    staffMember.getEmail(), staffMember.getRank()))
        input(ANYKEY)

    def singleStaffListOH(self, staffObject_list):
        print('\n{:^30}'.format(EMPLOYEES))
        print('\n{:<20} {:<11}'.format('Name', 'SSN'))
        for staffMember in staffObject_list:
            print('{:<20} {:<11}'.format(staffMember.getName(), staffMember.getSSN()))

    def singleStaffHeaderOH(self):
        print('\n{:^75}'.format(EMPLOYEE))
        print('\n{:<20} {:<11} {:<9} {:<20} {:<21}'.format('Name', 'SSN', 'Phone', 'Email', 'Rank'))

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

    def singleAirplanelistOH(self, airplane_list):
        for airplane in airplane_list:
            print('{}'.format(airplane))

    def singleAirplaneIdOH(self, airplaneID):
        print('____________')
        print('\n{:<12} {:<9}'.format('Airplane', 'Pilots'))
        for airLicense, pilot in airplaneID.items():
            print('{:<12} {:<9}'.format(airLicense, ''.join(pilot)))

        
        input(ANYKEY)
    
    def allDestinationsOH(self, destinationObject_list):
        print('\n{:^32}'.format(DESTINATIONS))
        print('\n{:<12} {:<9} {:<17}'.format('Country', 'Contact', 'Emergency Number'))
        for destination in destinationObject_list:
            print('{:<12} {:<9} {:<17}'.format(destination.getCountry(), destination.getContact(), destination.getEmergencyNumber()))
        input(ANYKEY)

    def allVoyagesOH(self, voyageObject_dict):
        counter = 1
        print('\n{:^32}'.format(VOYAGES))
        for voyage in voyageObject_dict:
            departureDateTime = voyage.getDepartureTime()
            parsedDateObject = dateutil.parser.parse(departureDateTime)
            print("\nDeparting from: {} - Arriving at: {}".format(voyage.getDepartingFrom(),voyage.getArrivingAt()))
            print('\n{:<11} {:<9}'.format('Date', 'Time'))
            print('{:<11} {:<9}'.format(str(parsedDateObject.day) + '-' + str(parsedDateObject.month) + '-' + str(parsedDateObject.year),
                                         str(parsedDateObject.hour) + ':' + str(parsedDateObject.minute)))

            if counter % 2 == 0:
                print("\nStaff:")
                if voyage.getCaptain() == "":
                    print(NOPILOT)
                else:
                    print('\n{:<20} {:<11} {:<21}'.format('Name', 'SSN', 'Rank'))
                    for staffMember in voyageObject_dict[voyage]:
                        if staffMember.getSSN() == voyage.getCaptain():
                            print('{:<20} {:<11} {:<21}'.format(staffMember.getName(), staffMember.getSSN(), staffMember.getRank()))

                if voyage.getCoPilot() == "":
                    print(NOCOPILOT)
                else:
                    for staffMember in voyageObject_dict[voyage]:
                        if staffMember.getSSN() == voyage.getCoPilot():
                            print('{:<20} {:<11} {:<21}'.format(staffMember.getName(), staffMember.getSSN(), staffMember.getRank()))

                if voyage.getFa1() == "":
                    print(NOFA1)
                else:
                    for staffMember in voyageObject_dict[voyage]:
                        if staffMember.getSSN() == voyage.getFa1():
                            print('{:<20} {:<11} {:<21}'.format(staffMember.getName(), staffMember.getSSN(), staffMember.getRank()))
                if voyage.getFa2() == "":
                    print(NOFA2)
                else:
                    for staffMember in voyageObject_dict[voyage]:
                        if staffMember.getSSN() == voyage.getFa2():
                            print('{:<20} {:<11} {:<21}'.format(staffMember.getName(), staffMember.getSSN(), staffMember.getRank()))
                print('__________________________')
            counter += 1
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
        if len(availableStaff) != 0:
            for staffMember in availableStaff:
                print('{:<20} {:<11} {:<21}'.format(staffMember.getName(), staffMember.getSSN(), staffMember.getRank()))
        else:
            print('No staff available on this date!')

        input(ANYKEY)

<<<<<<< HEAD
=======
    def allPilotsLicenseOH(self, pilotObject_list):
         print('\n{:^30}'.format(PILOTS))
         print('\n{:<20} {:<11} {:<12}\n'.format('Name', 'SSN', 'Current License'))
         for staffMember in pilotObject_list:
             print('{:<20} {:<11} {:<12}'.format(staffMember.getName(), staffMember.getSSN(), staffMember.getLicense()))


>>>>>>> 8fb01adbea46939593482c02a8d75bab0cf8ac80
    def workWeekOH(self, workList):
        counter = 1
        if len(workList) != 0:
            print('\n{:^32}'.format(WORKSCHEDULE))
            for voyage in workList:
                departureDateTime = voyage.getDepartureTime()
                parsedDateObject = dateutil.parser.parse(departureDateTime)
                print("\nDeparting from: {} - Arriving at: {}".format(voyage.getDepartingFrom(),voyage.getArrivingAt()))
                print('\n{:<5} {:<5}'.format('Date', 'Time'))
                print('{:<9} {:<9}'.format(str(parsedDateObject.day) + '-' + str(parsedDateObject.month) + '-' + str(parsedDateObject.year),
                                             str(parsedDateObject.hour) + ':' + str(parsedDateObject.minute)))
                if counter % 2 == 0:
                    print('__________________________')
                counter += 1
        else:
            print('Staffmember has no voyages in chosen week!')
        input(ANYKEY)

    def testPrint(self, testDict):
        print('\n{:53}'.format(LICENSE))
        print('\n{:<20} {:<11}'.format('Aircraft ID', 'Pilot'))
        for key, valu in testDict.items():
            print('{:<20} {:<11}'.format(key, ', '.join(valu)))

        input(ANYKEY)



