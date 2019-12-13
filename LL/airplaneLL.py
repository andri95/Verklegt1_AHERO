from IO.mainIO import MainIO
import datetime
import dateutil.parser

class AirplaneLL:
    '''Instance of MainIO created in constructor to give the class access to 
       all IO layer functionality'''
    def __init__(self):
        self.mainObject = MainIO()

    '''Recieves newAirplane object, passes it down into MainIO'''
    def addAirplane(self, newAirplane):
        return self.mainObject.addNewAirplaneIO(newAirplane)

    '''Returns MainIO function call that returns list of all airplanes as objects'''
    def getAirplanes(self):
        return self.mainObject.getAirplanesIO()

    '''Checks status of all airplanes at a given date and time, returns dictionary with airplaneID as key and status
       as value.'''
    def getAirplaneStatus(self, date, time):
        airplaneStatus_dict = {}
        voyagePair_list = []
        temp_list = []

        # Lists of all airplane objects and voyage objects created
        airplaneObject_list = self.mainObject.getAirplanesIO()
        voyageObject_list = self.mainObject.getVoyagesIO()

        # Input date and time split into lists, datetime object created out of lists
        date_list = date.split('-')
        time_list = time.split(':')
        dateObject = datetime.datetime(int(date_list[0]), int(date_list[1]), int(date_list[2]), int(time_list[0]), int(time_list[1]))

        # voyages pairs put into lists, pairs then put into voyagePair_list 
        counter = 1
        for voyage in voyageObject_list:
            temp_list.append(voyage)
            if counter % 2 == 0:
                voyagePair_list.append(temp_list)
                temp_list = []
            counter += 1
        
        for voyage in voyagePair_list:

            # datetime objects created out of voyage pair departure and arrival times
            voyageOneDeparting = dateutil.parser.parse(voyage[0].getDepartureTime())
            voyageOneArriving = dateutil.parser.parse(voyage[0].getArrivalTime())
            dateOneDeparting = datetime.datetime(voyageOneDeparting.year, voyageOneDeparting.month, voyageOneDeparting.day, 
                                                    voyageOneDeparting.hour, voyageOneDeparting.minute)
            dateOneArriving = datetime.datetime(voyageOneArriving.year, voyageOneArriving.month, voyageOneArriving.day, 
                                                    voyageOneArriving.hour, voyageOneArriving.minute)

            voyageTwoDeparting = dateutil.parser.parse(voyage[1].getDepartureTime())
            voyageTwoArriving = dateutil.parser.parse(voyage[1].getArrivalTime())
            dateTwoDeparting = datetime.datetime(voyageTwoDeparting.year, voyageTwoDeparting.month, voyageTwoDeparting.day, 
                                                    voyageTwoDeparting.hour, voyageTwoDeparting.minute)
            dateTwoArriving = datetime.datetime(voyageTwoArriving.year, voyageTwoArriving.month, voyageTwoArriving.day, 
                                                    voyageTwoArriving.hour, voyageTwoArriving.minute)
            
            # If statement cluster to determine status of each airplane at a given time. Results put into dictionary with airplaneID as key and status as value
            if dateObject.date() != dateOneDeparting.date():
                if dateObject.date() != dateTwoDeparting.date():
                    airplaneStatus_dict[voyage[0].getAircraftId()] = 'Available'
            else:
                if dateOneDeparting > dateObject:
                    airplaneStatus_dict[voyage[0].getAircraftId()] = 'Voyage today to ' + voyage[0].getArrivingAt()
                elif dateTwoArriving < dateObject:
                    airplaneStatus_dict[voyage[0].getAircraftId()] = 'Available'
                else:
                    if dateOneDeparting < dateObject:
                        if dateOneArriving > dateObject:
                            airplaneStatus_dict[voyage[0].getAircraftId()] = 'In transit from ' + voyage[0].getDepartingFrom() + ' to ' + voyage[0].getArrivingAt()
                        elif dateTwoDeparting < dateObject:
                            if dateTwoArriving > dateObject:
                                airplaneStatus_dict[voyage[1].getAircraftId()] = 'In transit from ' + voyage[1].getDepartingFrom() + ' to ' + voyage[1].getArrivingAt()
                            else:
                                airplaneStatus_dict[voyage[1].getAircraftId()] = 'In voyage to ' + voyage[1].getArrivingAt()
                        else:
                            airplaneStatus_dict[voyage[0].getAircraftId()] = 'In voyage to ' + voyage[0].getArrivingAt()
        
        # If an airplane is not in airplaneStatus_dict it means that the airplane has no voyage on given date, then available
        for airplane in airplaneObject_list:
            if airplane.getPlaneId() not in airplaneStatus_dict:
                airplaneStatus_dict[airplane.getPlaneId()] = 'Available'

        return airplaneStatus_dict

    '''Recieves ID, creates dict of all airplanes and licensed pilots. Iterates through dict,
       finds appropriate license and returns dict containing only desired airplane id and 
       licensed pilots'''
    def getAirplaneByID(self, ID):
        license_dict = self.getLicenseDict()
        return_dict = {}
        for pilotLicense in license_dict:
            if pilotLicense == ID:
                return_dict[pilotLicense] = license_dict[pilotLicense]
        return return_dict

    '''Recieves dataList and returns addLicenseIO function call'''
    def addLicense(self, dataList):
        return self.mainObject.addLicenseIO(dataList)

    '''Gets list of all staff as objects from getStaffIO function call. Iterates through list
       and finds all staff that have pilot as role. Returns list of only pilot objects'''
    def getAllPilots(self):
        staffObject_list = self.mainObject.getStaffIO()
        pilotObject_list = []
        for staffMember in staffObject_list:
            if staffMember.getRole() == 'pilot':
                pilotObject_list.append(staffMember)
        return pilotObject_list

    '''Returns dictionary with all airplane IDs as keys and all licensed pilots on each 
       airplane as values'''
    def getLicenseDict(self):
        # Get lists of all staff objects and airplane objects through MainIO function calls
        staffObject_list = self.mainObject.getStaffIO()
        aiprlaneObject_list = self.mainObject.getAirplanesIO()
        pilotObject_list = []
        license_Dict = {}

        # All pilots found and put into pilotObject_list
        for staffMember in staffObject_list:
            if staffMember.getRole() == 'pilot':
                pilotObject_list.append(staffMember)

        # Iterates through pilot list, sets license as key and pilot name as value
        for staffMember in pilotObject_list:
            if staffMember.getLicense() not in license_Dict:
                license_Dict[staffMember.getLicense()] = [staffMember.getName()]
            # If airplane is already in dict, pilot is appended to value
            else:
                license_Dict[staffMember.getLicense()].append(staffMember.getName())
        
        # If airplane is not in license_dict, no pilot is licensed on given airplane
        for airplane in aiprlaneObject_list:
            if airplane.getPlaneId() not in license_Dict:
                license_Dict[airplane.getPlaneId()] = ['No licensed pilot']
        return license_Dict



