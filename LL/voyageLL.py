from IO.mainIO import MainIO
import datetime
import dateutil.parser

class VoyageLL():
    def __init__(self):
        self.mainObject = MainIO()
  
    def listVoyage(self):
        voyageObject_list = self.mainObject.getVoyagesIO()
        staffObject_list = self.mainObject.getStaffIO()
        voyage_dict = {}
        for voyage in voyageObject_list:
            if voyage.getStaff() == ['', '', '', '']:
                voyage_dict[voyage] = voyage.getStaff()
            for staffMember in staffObject_list:
                if staffMember.getSSN() in voyage.getStaff():
                    if voyage in voyage_dict:
                        voyage_dict[voyage].append(staffMember)
                    else:
                        voyage_dict[voyage] = [staffMember]           
        return voyage_dict

    def addVoyages(self, newFlight):
        return self.mainObject.addNewVoyageIO(newFlight)

    def updateVoyage(self, dataList, staffList):
        return self.mainObject.updateVoyageIO(dataList, staffList)

    def generateFlightNumber(self, flight):
        flightNumberList = []
        destination = flight.getArrivingAt()
        voyageList = self.mainObject.getVoyagesIO()
        destinationList = self.mainObject.getDestinationsIO()
        for dest in destinationList:
            if dest.getCountry() == destination:
                destId = dest.getDestId()
        flightDate = flight.getDepartureTime().split("T")
        currentDate = flightDate[0].split('-')
        print(currentDate)
        currentDateObject = datetime.datetime(int(currentDate[0]), int(currentDate[1]), int(currentDate[2]))
        for voyage in voyageList:
            bookedFlightNum = voyage.getDepartureTime().split("T")
            #print("boyyy:", bookedFlightNum)
            date_list = bookedFlightNum[0].split('-')
            #print("dis", date_list)
            dateObject = datetime.datetime(int(date_list[0]), int(date_list[1]), int(date_list[2]))
            print("1",dateObject)
            print("2",currentDateObject)
            if dateObject == currentDateObject and voyage.getArrivingAt() == flight.getArrivingAt() or voyage.getDepartingFrom() == flight.getArrivingAt():
                flightId = voyage.getFlightNumber()
                flightIdLastNums = flightId[-2:]
                flightNumberList.append(int(flightIdLastNums))
        if flightNumberList == []:
            return "NA" + destId + "00"
        else:
            findMostRecent = max(flightNumberList)
            if findMostRecent >= 10:
                newFlightNumber = "NA" + destId + str(findMostRecent + 1)
            newFlightNumber = "NA" + destId + "0" + str(findMostRecent + 1)
        return newFlightNumber


    def findArrivalTime(self, flight):
        allDest = self.mainObject.getDestinationsIO()
        for dest in allDest:
            if dest.getCountry() == flight.getArrivingAt():
                flightTime = dest.getFlightTime()
        try:
            if flightTime == "0":
                for dest in allDest:
                    if dest.getCountry() == flight.getDepartingFrom():
                        flightTime = dest.getFlightTime()
        except UnboundLocalError:
            return False
        departureTimeTemp = flight.getDepartureTime().split("T")
        departureTime = " ".join(departureTimeTemp)
        tdelta = datetime.timedelta(hours=int(flightTime))

        datetime_object = datetime.datetime.strptime(departureTime, '%Y-%m-%d %H:%M:%S')
        totalTime = datetime_object + tdelta
        newtime = datetime.datetime.strftime(totalTime,'%Y-%m-%dT%H:%M:%S')

        return newtime

    def availableDates(self):
        availableDates_list = []
        voyageObject_list = self.mainObject.getVoyagesIO()
        for voyage in voyageObject_list:
            departureTime = voyage.getDepartureTime()
            date = departureTime.split('T')
            if date[0] not in availableDates_list:
                availableDates_list.append(date[0])
        return availableDates_list

    def getWorkWeek(self, dataList):
        workWeekObject_list = []
        voyabeObject_list = self.mainObject.getVoyagesIO()
        for voyage in voyabeObject_list:
            departureDateTime = voyage.getDepartureTime()
            parsedDateObject = dateutil.parser.parse(departureDateTime)
            timeCompare = datetime.datetime(parsedDateObject.year, parsedDateObject.month, parsedDateObject.day)
            if timeCompare >= dataList[0]:
                if timeCompare <= dataList[1]:
                    if dataList[2] in voyage.getStaff():
                        workWeekObject_list.append(voyage)
        return workWeekObject_list

    def findAvalibleAirplanes(self, flight):
        allNanPlanes = self.mainObject.getAirplanesIO()
        allVoyages = self.mainObject.getVoyagesIO()
        dateToFind = flight.getDepartureTime().split("T")
        allavalibleAirplanes = []
        for plane in allNanPlanes:
            allavalibleAirplanes.append(plane.getPlaneId())

        for voyage in allVoyages:
            uppcomingVoyageDates = voyage.getDepartureTime().split("T")
            if uppcomingVoyageDates[0] == dateToFind[0]:
                busyAirplanes = voyage.getAircraftId()
                try:
                    allavalibleAirplanes.remove(busyAirplanes)
                except ValueError:
                    pass
        if allavalibleAirplanes == []:
            return False
        else:
            return allavalibleAirplanes[0]

    def generateSecondFlight(self, firstFlight):
        departingFrom = firstFlight.getArrivingAt()
        arravingAt = firstFlight.getDepartingFrom()
        airplane = firstFlight.getAircraftId()
        departureTimeTemp = firstFlight.getArrivalTime().split("T")
        departureTime = " ".join(departureTimeTemp)
        tdelta = datetime.timedelta(hours=int(1))
        datetime_object = datetime.datetime.strptime(departureTime, '%Y-%m-%d %H:%M:%S')
        newDepartureTime = datetime_object + tdelta
        newtime = datetime.datetime.strftime(newDepartureTime, '%Y-%m-%dT%H:%M:%S')

        return departingFrom, arravingAt, newtime, airplane



