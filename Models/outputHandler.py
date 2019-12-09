
class OutputHandler:

    def allStaffOH(self, staffObject_list):
        print('\n{:^75}'.format('_______ Employees _______'))
        print('\n{:<20} {:<11} {:<9} {:<20} {:<21}\n'.format('Name', 'SSN', 'Phone', 'Email', 'Rank'))
        for staffMember in staffObject_list:
            print('{:<20} {:<11} {:<9} {:<20} {:<21}'.format(staffMember.getName(), staffMember.getSSN(), staffMember.getCellPhone(),
                                                    staffMember.getEmail(), staffMember.getRank()))
        input("Press any key to continue.")

    def allPilotsOH(self, pilotObject_list):
        print('\n{:^81}'.format('_______ Pilots _______'))
        print('\n{:<20} {:<11} {:<9} {:<20} {:<9} {:<12}\n'.format('Name', 'SSN', 'Phone', 'Email', 'Rank', 'License'))
        for staffMember in pilotObject_list:
            print('{:<20} {:<11} {:<9} {:<20} {:<9} {:<12}'.format(staffMember.getName(), staffMember.getSSN(), staffMember.getCellPhone(),
                                                    staffMember.getEmail(), staffMember.getRank(), staffMember.getLicence()))
        input("Press any key to continue.")

    def allCabinCrewOH(self, cabinCrewObject_list):
        print('\n{:^81}'.format('_______ Cabin Crew _______'))
        print('\n{:<20} {:<11} {:<9} {:<20} {:<21}\n'.format('Name', 'SSN', 'Phone', 'Email', 'Rank'))
        for staffMember in cabinCrewObject_list:
            print('{:<20} {:<11} {:<9} {:<20} {:<21}'.format(staffMember.getName(), staffMember.getSSN(), staffMember.getCellPhone(),
                                                    staffMember.getEmail(), staffMember.getRank()))
        input("Press any key to continue.")

    def singleStaffListOH(self, staffObject_list):
        print('\n{:^30}'.format('_______ Employees _______'))
        print('\n{:<20} {:<11}\n'.format('Name', 'SSN'))
        for staffMember in staffObject_list:
            print('{:<20} {:<11}'.format(staffMember.getName(), staffMember.getSSN()))

    def singleStaffHeaderOH(self):
        print('\n{:^75}'.format('_______ Employee _______'))
        print('\n{:<20} {:<11} {:<9} {:<20} {:<21}\n'.format('Name', 'SSN', 'Phone', 'Email', 'Rank'))

    def singleStaffOH(self, staffMember):
        print('{:<20} {:<11} {:<9} {:<20} {:<21}'.format(staffMember.getName(), staffMember.getSSN(), staffMember.getCellPhone(),
                                                    staffMember.getEmail(), staffMember.getRank()))
        input("Press any key to continue.")

    def allAirplanesOH(self, airplaneObject_list):
        print('\n{:^32}'.format('_______ Airplanes _______'))
        print('\n{:<12} {:<7} {:<5} {:<8}'.format('ID', 'Type', 'Model', 'Capacity'))
        for airplane in airplaneObject_list:
            print('{:<12} {:<7} {:<5} {:<8}'.format(airplane.getPlaneId(), airplane.getType(), airplane.getModel(), airplane.getCapacity()))
        input("Press any key to continue.")

    def allDestinationsOH(self, destinationObject_list):
        print('\n{:^32}'.format('_______ Destinations _______'))
        print('\n{:<12} {:<9} {:<17}'.format('Country', 'Contact', 'Emergency Number'))
        for destination in destinationObject_list:
            print('{:<12} {:<9} {:<17}'.format(destination.getCountry(), destination.getContact(), destination.getEmergencyNumber()))
        input("Press any key to continue.")