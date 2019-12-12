from IO.mainIO import MainIO
from LL.staffLL import StaffLL
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
        currentDateObject = datetime.datetime(int(currentDate[0]), int(currentDate[1]), int(currentDate[2]))

        # if conditions are met for the iteration then
        for i, voyage in enumerate(voyageList):
            bookedFlightNum = voyage.getDepartureTime().split("T")
            date_list = bookedFlightNum[0].split('-')
            dateObject = datetime.datetime(int(date_list[0]), int(date_list[1]), int(date_list[2]))
            if dateObject == currentDateObject and voyage.getArrivingAt() == flight.getArrivingAt():

                flightIdFirst = voyage.getFlightNumber()
                flightNumberList.append(int(flightIdFirst[-2:]))
                try:
                    flightIdSecond = voyageList[i + 1].getFlightNumber()
                    flightNumberList.append(int(flightIdSecond[-2:]))
                except IndexError:
                    pass
                except Exception as e:
                    print(e)

        if flightNumberList == []:
            return "NA" + destId + "00"
        else:
            findMostRecent = max(flightNumberList)
            if findMostRecent >= 10:
                newFlightNumber = "NA" + destId + str(findMostRecent + 1)
            else:
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
        updatedTime = datetime.datetime.strftime(totalTime, '%Y-%m-%dT%H:%M:%S')

        return updatedTime

    def errorCheckDate(self, flight):
        errorMessage = "Date was not entered correctly (YYYY-MM-DD), please try again "
        flightTime = flight.getDepartureTime()
        date = flightTime.split("T")
        try:
            year, month, day = date[0].split("-")
            dateTimeObject = datetime.date(int(year), int(month), int(day))
            if len(year) != 4:
                print(errorMessage)
                return False
        except ValueError:
            print(errorMessage)
            return False
        try:
            dateTimeObject = datetime.date(int(year), int(month), int(day))
        except TypeError:
            print(errorMessage)
            return False
        return True

    def flightCollision(self, flight):
        voyageList = self.mainObject.getVoyagesIO()
        for voyage in voyageList:
            if voyage.getDepartureTime() == flight.getDepartureTime():
                return True
            else:
                pass

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

    def findAvailableFlightAttendants(self, flight):
        allFlightAttendants = StaffLL().getAllFlightAttendants()
        allVoyages = self.mainObject.getVoyagesIO()
        dateToFind = flight.getDepartureTime().split("T")
        allAvalibleFlightAttendants = []
        for flightAttendant in allFlightAttendants:
            allAvalibleFlightAttendants.append(flightAttendant.getName())  ##############################

        busyflightAttendants = []
        for voyage in allVoyages:
            uppcomingVoyageDates = voyage.getDepartureTime().split("T")
            if uppcomingVoyageDates[0] == dateToFind[0]:
                if voyage.getFa2() not in busyflightAttendants:
                    busyflightAttendants.append(voyage.getFa2())
                    try:
                        for flightAttendant in busyflightAttendants:
                            if flightAttendant in allAvalibleFlightAttendants:
                                allAvalibleFlightAttendants.remove(flightAttendant)
                            else:
                                pass
                    except ValueError:
                        pass
        if allAvalibleFlightAttendants == []:
            return False
        else:
            return allAvalibleFlightAttendants


    def findAvailableFlightServiceManagers(self, flight):
        allFlightServiceManagers = StaffLL().getAllFlightServiceManagers()
        allVoyages = self.mainObject.getVoyagesIO()
        dateToFind = flight.getDepartureTime().split("T")
        allAvalibleFlightServiceManagers = []
        for FlightServiceManager in allFlightServiceManagers:
            allAvalibleFlightServiceManagers.append(FlightServiceManager.getName())  ##############################

        busyFlightServiceManagers = []
        for voyage in allVoyages:
            uppcomingVoyageDates = voyage.getDepartureTime().split("T")
            if uppcomingVoyageDates[0] == dateToFind[0]:
                if voyage.getFa1() not in busyFlightServiceManagers:
                    busyFlightServiceManagers.append(voyage.getFa1())
                    try:
                        for FlightServiceManager in busyFlightServiceManagers:
                            if FlightServiceManager in allAvalibleFlightServiceManagers:
                                allAvalibleFlightServiceManagers.remove(FlightServiceManager)
                            else:
                                pass
                    except ValueError:
                        pass
        if allAvalibleFlightServiceManagers == []:
            return False
        else:
            return allAvalibleFlightServiceManagers

    def findAvailableCoPilots(self, flight):
        allCoPilots = StaffLL().getAllCoPilots()
        allVoyages = self.mainObject.getVoyagesIO()
        dateToFind = flight.getDepartureTime().split("T")
        idToFind = flight.getAircraftId()
        allAvalibleCoPilots = []
        for coPilot in allCoPilots:
            allAvalibleCoPilots.append(coPilot.getName())  ##############################

        busyCoPilots = []
        for voyage in allVoyages:
            uppcomingVoyageDates = voyage.getDepartureTime().split("T")
            if uppcomingVoyageDates[0] == dateToFind[0]:
                if voyage.getCoPilot() not in busyCoPilots:
                    busyCoPilots.append(voyage.getCoPilot())
                    try:
                        for coPilot in busyCoPilots:
                            if coPilot in allAvalibleCoPilots:
                                allAvalibleCoPilots.remove(coPilot)
                            else:
                                pass
                    except ValueError:
                        pass
        if allAvalibleCoPilots == []:
            return False
        else:
            qualifiedCoPilots = []
            for coPilot in allCoPilots:
                if coPilot.getLicense() == idToFind and coPilot.getName() in allAvalibleCoPilots:
                    qualifiedCoPilots.append(coPilot)

            return qualifiedCoPilots

    def findAvailableCaptains(self, flight):
        allCaptains = StaffLL().getAllCaptains()
        allVoyages = self.mainObject.getVoyagesIO()
        dateToFind = flight.getDepartureTime().split("T")
        idToFind = flight.getAircraftId()
        allAvalibleCaptains = []
        for captain in allCaptains:
            allAvalibleCaptains.append(captain.getName())  ##############################

        busyCaptains = []
        for voyage in allVoyages:
            uppcomingVoyageDates = voyage.getDepartureTime().split("T")
            if uppcomingVoyageDates[0] == dateToFind[0]:
                if voyage.getCaptain() not in busyCaptains:
                    busyCaptains.append(voyage.getCaptain())
                    try:
                        for captain in busyCaptains:
                            if captain in allAvalibleCaptains:
                                allAvalibleCaptains.remove(captain)
                            else:
                                pass
                    except ValueError:
                        pass
                if allAvalibleCaptains == []:
                    return False
                else:
                    qualifiedCaptains = []
                    for captain in allCaptains:
                        if captain.getLicense() == idToFind and captain.getName() in allAvalibleCaptains:
                            qualifiedCaptains.append(captain)

                    return qualifiedCaptains

    def generateSecondFlight(self, firstFlight):
        departingFrom = firstFlight.getArrivingAt()
        arravingAt = firstFlight.getDepartingFrom()
        airplane = firstFlight.getAircraftId()
        departureTimeTemp = firstFlight.getArrivalTime().split("T")
        departureTime = " ".join(departureTimeTemp)
        tdelta = datetime.timedelta(hours=int(1))
        datetime_object = datetime.datetime.strptime(departureTime, '%Y-%m-%d %H:%M:%S')
        newDepartureTime = datetime_object + tdelta
        updatedTime = datetime.datetime.strftime(newDepartureTime, '%Y-%m-%dT%H:%M:%S')

        return departingFrom, arravingAt, updatedTime, airplane

    def voyageStaffErrorCheck(self, stafflist):
        updatedStaffSSN = []
        allStaff = self.mainObject.getStaffIO()
        for emp in allStaff:
            if emp.getName() in stafflist:
                updatedStaffSSN.append(emp.getSSN())
            if len(updatedStaffSSN) != 4:
               return False
        return updatedStaffSSN


