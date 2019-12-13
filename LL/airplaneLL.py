from IO.mainIO import MainIO
import datetime
import dateutil.parser

class AirplaneLL:
    def __init__(self):
        self.mainObject = MainIO()

    def addAirplane(self, newAirplane):
        return self.mainObject.addNewAirplaneIO(newAirplane)

    def getAirplanes(self):
        return self.mainObject.getAirplanesIO()

    def getAirplaneStatus(self, date, time):
        airplaneStatus_dict = {}
        voyagePair_list = []
        temp_list = []
        airplaneObject_list = self.mainObject.getAirplanesIO()
        voyageObject_list = self.mainObject.getVoyagesIO()
        date_list = date.split('-')
        time_list = time.split(':')
        dateObject = datetime.datetime(int(date_list[0]), int(date_list[1]), int(date_list[2]), int(time_list[0]), int(time_list[1]))
        counter = 1
        for voyage in voyageObject_list:
            temp_list.append(voyage)
            if counter % 2 == 0:
                voyagePair_list.append(temp_list)
                temp_list = []
            counter += 1
        for voyage in voyagePair_list:
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
                    
        for airplane in airplaneObject_list:
            if airplane.getPlaneId() not in airplaneStatus_dict:
                airplaneStatus_dict[airplane.getPlaneId()] = 'Available'

        return airplaneStatus_dict

    def getAirplaneByID(self, ID):
        license_dict = self.getLicenseDict()
        return_dict = {}
        for pilotLicense in license_dict:
            if pilotLicense == ID:
                return_dict[pilotLicense] = license_dict[pilotLicense]
        return return_dict

    def addLicense(self, dataList):
        return self.mainObject.addLicenseIO(dataList)

    def getAllPilots(self):
        staffObject_list = self.mainObject.getStaffIO()
        pilotObject_list = []
        for staffMember in staffObject_list:
            if staffMember.getRole() == 'pilot':
                pilotObject_list.append(staffMember)
        return pilotObject_list

    def getLicenseDict(self):
        staffObject_list = self.mainObject.getStaffIO()
        aiprlaneObject_list = self.mainObject.getAirplanesIO()
        pilotObject_list = []
        for staffMember in staffObject_list:
            if staffMember.getRole() == 'pilot':
                pilotObject_list.append(staffMember)
        license_Dict = {}
        for staffMember in pilotObject_list:
            if staffMember.getLicense() not in license_Dict:
                license_Dict[staffMember.getLicense()] = [staffMember.getName()]
            else:
                license_Dict[staffMember.getLicense()].append(staffMember.getName())
        for airplane in aiprlaneObject_list:
            if airplane.getPlaneId() not in license_Dict:
                license_Dict[airplane.getPlaneId()] = ['No licensed pilot']
        return license_Dict



