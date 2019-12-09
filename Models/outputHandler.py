#import dateutil.parser

EMPLOYEES = '_______ Employees _______'
EMPLOYEE = '_______ Employee _______'
PILOTS = '_______ Pilots _______'
CABINCREW = '_______ Cabin Crew _______'
AIRPLANES = '_______ Airplanes _______'
DESTINATIONS = '_______ Destinations _______'
VOYAGES = '_______ Voyages _______'
DELIMITER = '_______________________'
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
        counter = 1
        print('\n{:^32}'.format(VOYAGES))
        for voyage in voyageObject_list:
            departureDateTime = voyage.getDepartureTime()
            parsedDateObject = dateutil.parser.parse(departureDateTime)
            print("\nDeparting from: {} - Arriving at: {}".format(voyage.getDepartingFrom(),voyage.getArrivingAt()))
            print('\n{:<11} {:<9}'.format('Date', 'Time'))
            print('{:<11} {:<9}'.format(str(parsedDateObject.day) + '-' + str(parsedDateObject.month) + '-' + str(parsedDateObject.year),
                                         str(parsedDateObject.hour) + ':' + str(parsedDateObject.minute)))
            if counter % 2 == 0:
                print("\nStaff")
                if voyage.getCaptain() == "":
                    print(NOPILOT)
                else:
                    print("Pilot: {}".format(voyage.getCaptain()))

                if voyage.getCoPilot() == "":
                    print(NOCOPILOT)
                else:
                    print("Co-pilot: {}".format(voyage.getCoPilot()))

                if voyage.getFa1() == "":
                    print(NOFA1)
                else:
                    print("Flight Service Manager: {}".format(voyage.getFa1()))
                if voyage.getFa2() == "":
                    print(NOFA2)
                else:
                    print("Flight Attendant: {}".format(voyage.getFa2()))

                print(DELIMITER)
            
            counter += 1
        input(ANYKEY)

    def allPilotsLicenseOH(self, pilotObject_list):
        print('\n{:^30}'.format(PILOTS))
        print('\n{:<20} {:<11} {:<12}\n'.format('Name', 'SSN', 'Current License'))
        for staffMember in pilotObject_list:
            print('{:<20} {:<11} {:<12}'.format(staffMember.getName(), staffMember.getSSN(), staffMember.getLicense()))
    
    def allUnavailablestaffOH(self,voyageObject_list):
        pass
