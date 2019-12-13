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
AIRPLANESTATUS = '_______ Airplane Status _______'
LICENSEDPILOTS = '_______ Licensed Pilots _______'
NOPILOT = "No Captain yet."
NOCOPILOT = "No Copilot yet."
NOFA1 = "No Flight Service Manager yet."
NOFA2 = "No Flight Attendant yet."
ANYKEY = 'Press any key to continue.'

class OutputHandler:
    '''The class OutputHandler has method that are called in multiple different methods. The methods in the class
     have parameters that are usually lists of instances (fx.list of airplanes). Then we use our get method to
       extract the info we choose '''
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

    def singleStaffListOH(self, staffObject_dict):
        print('\n{:^30}'.format(EMPLOYEES))
        print('\n{:>2}  {:<20} {:<11}'.format('Nr', 'Name', 'SSN'))
        for staffMember in staffObject_dict:
            print('{:>2}. {:<20} {:<11}'.format(staffMember, staffObject_dict[staffMember].getName(), staffObject_dict[staffMember].getSSN()))

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
        for i, airplane in enumerate(airplane_list, 1):
            print('{}. {}'.format(i, airplane.getPlaneId()))

    def singleAirplaneIdOH(self, airplaneID):
        print('\n' + LICENSEDPILOTS)
        print('\n{:<12} {:<9}'.format('Airplane', 'Pilots'))
        for airLicense, pilot in airplaneID.items():
            print('{:<12} {:<9}'.format(airLicense, ', '.join(pilot)))

        
        input(ANYKEY)
    
    def allDestinationsOH(self, destinationObject_list):
        print('\n{:^32}'.format(DESTINATIONS))
        print('\n{:<12} {:<9} {:<17} {:<7}'.format('Country', 'Contact', 'Emergency Number', 'DestID'))
        for destination in destinationObject_list:
            print('{:<12} {:<9} {:<17} {:<7}'.format(destination.getCountry(), destination.getContact(), destination.getEmergencyNumber(), destination.getDestId()))
        input(ANYKEY)

    def availableDestinationsOH(self, destinationObject_dict):
        print('\n{:^32}'.format(DESTINATIONS))
        print('{:>2}. {:<15}'.format('Nr', 'Destination'))
        for destination in destinationObject_dict:
            print('{:>2}. {:<15}'.format(destination, destinationObject_dict[destination].getCountry()))

    def voyageDestinationOH(self, destinationObject_list):
        for i, destination in enumerate(destinationObject_list):
            if destination.getCountry() == "keflavik":
                pass
            else:
                print('{}.{:<12} '.format(i,destination.getCountry()))
        print()



    def allVoyagesOH(self, voyageObject_dict):
        counter = 1
        print('\n{:^32}'.format(VOYAGES))
        for voyage in voyageObject_dict:
            departureDateTime = voyage.getDepartureTime()
            parsedDateObject = dateutil.parser.parse(departureDateTime)
            if len(str(parsedDateObject.minute)) == 1:
                minute = str(parsedDateObject.minute) + '0' # add one because when using the dateutil method it changes 00 to 0
            else:
                minute = str(parsedDateObject.minute)
            print("\nDeparting from: {} - Arriving at: {}".format(voyage.getDepartingFrom(),voyage.getArrivingAt()))
            print('\n{:<11} {:<9} {:<14}'.format('Date', 'Time', 'Flight number'))
            print('{:<11} {:<9} {:<14}'.format(str(parsedDateObject.day) + '-' + str(parsedDateObject.month) + '-' + str(parsedDateObject.year),
                                         str(parsedDateObject.hour) + ':' + minute, voyage.getFlightNumber()))
            # The reason for the counter is because we dont want to print the staff twice
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
                print('_______________________________________________________')
            counter += 1
        input(ANYKEY)


    def availableDatesOH(self, availableDates_dict):
        print('\n_______ Avaliable Dates _______\n')
        print('{:>2}. {:<13}'.format('Nr', 'Date'))
        for date in availableDates_dict:
            print('{:>2}. {:<13}'.format(date, availableDates_dict[date]))
        print()

    def workScheduleAvailableOH(self, availableStaff):
        print('\n{:^53}'.format(AVAILABLE))
        print('\n{:<20} {:<11} {:<21}'.format('Name', 'SSN', 'Rank'))
        if len(availableStaff) != 0:
            for staffMember in availableStaff:
                print('{:<20} {:<11} {:<21}'.format(staffMember.getName(), staffMember.getSSN(), staffMember.getRank()))
        else:
            print('No staff available on this date!')

        input(ANYKEY)

    def allPilotsLicenseOH(self, pilotObject_dict):
         print('\n{:^30}'.format(PILOTS))
         print('\n{:>2}. {:<20} {:<11} {:<12}'.format('Nr','Name', 'SSN', 'Current License'))
         for staffMember in pilotObject_dict:
             print('{:>2}. {:<20} {:<11} {:<12}'.format(staffMember, pilotObject_dict[staffMember].getName(), pilotObject_dict[staffMember].getSSN(),
                                                 pilotObject_dict[staffMember].getLicense()))


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
        
    def airplaneStatusOH(self, airplaneStatus_dict):
        print('\n{:^32}'.format(AIRPLANESTATUS))
        print('\n{:<13} {:<20}'.format('Airplane ID', 'Status'))
        for airplane in sorted(airplaneStatus_dict):
            print('{:<13} {:<20}'.format(airplane, airplaneStatus_dict[airplane]))
        input(ANYKEY)

    def airplaneLicensedOH(self, licensecDict):
        print('\n{:53}'.format(LICENSEDPILOTS))
        print('\n{:<20} {:<11}'.format('Aircraft ID', 'Pilot'))
        for key, valu in sorted(licensecDict.items()):
            print('{:<20} {:<11}'.format(key, ', '.join(valu)))

        input(ANYKEY)
