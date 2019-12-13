from IO.mainIO import MainIO
import datetime
import dateutil.parser
import random

class VoyageLL():
    '''Instances of appropriate classes created in constructor so the class
       has access to their functions. MainLL connects the class to the logic layer
       and the other classes handle inputs, outputs and errors'''
    def __init__(self):
        self.mainObject = MainIO()
  
    def listVoyage(self):
        """ Returns a dictionary where the keys are voyages and their values are staff members. """
        voyageObject_list = self.mainObject.getVoyagesIO()
        staffObject_list = self.mainObject.getStaffIO()
        voyage_dict = {}
        for voyage in voyageObject_list:
            if voyage.getStaff() == ['', '', '', '']:  # If there is no staff assigned to the voyage,
                voyage_dict[voyage] = voyage.getStaff()  # Then assign the staff to the voyage.
            else:
                for staffMember in staffObject_list:
                    if staffMember.getSSN() in voyage.getStaff():
                        if voyage in voyage_dict:
                            voyage_dict[voyage].append(staffMember)
                        else:
                            voyage_dict[voyage] = [staffMember]
        return voyage_dict

    def addVoyages(self, newFlight):
        ''' Takes a voyage model and returns the addNewVoyageIO method in the MainIO. '''
        return self.mainObject.addNewVoyageIO(newFlight)

    def updateVoyage(self, dataList, staffList):
        '''Takes a voyage model and returns the updateVoyageIO method in the MainIO. '''
        return self.mainObject.updateVoyageIO(dataList, staffList)

    def generateFlightNumber(self, flight):
        ''' Generates a flight number for the flight to the destination and back. If there are no flights to the target destination
            at the target date then we simply add 2 zeros to "NA" and the destination Id then returns the correct flight number'''
        flightNumberList = []
        destination = flight.getArrivingAt()
        voyageList = self.mainObject.getVoyagesIO()
        destinationList = self.mainObject.getDestinationsIO()
        for dest in destinationList:
            if dest.getCountry() == destination:
                destId = dest.getDestId()                       # Finds the destination Id for the flight
        flightDate = flight.getDepartureTime().split("T")
        currentDate = flightDate[0].split('-')                  # index 0 should be the date
        currentDateObject = datetime.datetime(int(currentDate[0]), int(currentDate[1]), int(currentDate[2])) # Create a dateTimeobject from the flight


        for i, voyage in enumerate(voyageList): # we use enumerate because one voyage is 2 flights in 2 lines.
            bookedFlightNum = voyage.getDepartureTime().split("T")
            date_list = bookedFlightNum[0].split('-')
            dateObject = datetime.datetime(int(date_list[0]), int(date_list[1]), int(date_list[2]))
            if dateObject == currentDateObject and voyage.getArrivingAt() == flight.getArrivingAt(): # If it finds a flight to the same destination
                                                                                                     # And with the same date then generate a flight number
                flightIdFirst = voyage.getFlightNumber()                                             # for this flight and the one after (2flights=1voyage)
                flightNumberList.append(int(flightIdFirst[-2:]))
                try:
                    flightIdSecond = voyageList[i + 1].getFlightNumber()
                    flightNumberList.append(int(flightIdSecond[-2:]))
                except IndexError:
                    pass
                except Exception as e:
                    print(e)

        if flightNumberList == []:
            return "NA" + destId + "00"         # If there there are no flight that day to that destination then give it NAXX00
        else:
            findMostRecent = max(flightNumberList)
            if findMostRecent >= 10:            # If the flight number has not reached 10 then we add "0" to it
                newFlightNumber = "NA" + destId + str(findMostRecent + 1)
            else:
                newFlightNumber = "NA" + destId + "0" + str(findMostRecent + 1)
        return newFlightNumber

    def findArrivalTime(self, flight):
        '''Creates the arrival time, calculated by the flight time to the destination '''
        allDest = self.mainObject.getDestinationsIO()
        for dest in allDest:
            if dest.getCountry() == flight.getArrivingAt():
                flightTime = dest.getFlightTime()
        try:
            if flightTime == "0":           # keflavik has the flighttime of 0 so if the flight is arriving to keflavik
                for dest in allDest:        # then we calculate with the flight time of departing destination
                    if dest.getCountry() == flight.getDepartingFrom():
                        flightTime = dest.getFlightTime()
        except UnboundLocalError:
            return False
        departureTimeTemp = flight.getDepartureTime().split("T")
        departureTime = " ".join(departureTimeTemp)
        tdelta = datetime.timedelta(hours=int(flightTime))

        datetime_object = datetime.datetime.strptime(departureTime, '%Y-%m-%d %H:%M:%S')
        totalTime = datetime_object + tdelta
        updatedTime = datetime.datetime.strftime(totalTime,'%Y-%m-%dT%H:%M:%S')

        return updatedTime

    def flightCollision(self, flight):
        ''' Checks if the new flight is departing at the same time as another flight.
            We only check by the minute, a airplane can take off at 16:00 and another at 16:01'''
        voyageList = self.mainObject.getVoyagesIO()
        flightTime = flight.getDepartureTime()[:-2] # Takes the seconds of the time
        for voyage in voyageList:
            voyageTime = voyage.getDepartureTime()[:-2]
            if voyageTime == flightTime:
                return True
            else:
                pass

    def availableDates(self):
        '''Finds the dates where there are booked voyages and returns a list of those dates '''
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
        voyageObject_list = self.mainObject.getVoyagesIO()
        for voyage in voyageObject_list:
            departureDateTime = voyage.getDepartureTime()
            parsedDateObject = dateutil.parser.parse(departureDateTime)
            timeCompare = datetime.datetime(parsedDateObject.year, parsedDateObject.month, parsedDateObject.day)
            if timeCompare >= dataList[0]:
                if timeCompare <= dataList[1]:
                    if dataList[2] in voyage.getStaff():
                        workWeekObject_list.append(voyage)
        return workWeekObject_list

    def findAvalibleAirplanes(self, flight):
        '''Gets a list with all Nan airplanes, removes those that are unavailable today. Returns one airplane from a the list'''

        allNanPlanes = self.mainObject.getAirplanesIO()
        allVoyages = self.mainObject.getVoyagesIO()
        dateToFind = flight.getDepartureTime().split("T")
        allavalibleAirplanes = []
        for plane in allNanPlanes:
            allavalibleAirplanes.append(plane.getPlaneId()) # List of all airplanes

        for voyage in allVoyages:
            uppcomingVoyageDates = voyage.getDepartureTime().split("T")
            if uppcomingVoyageDates[0] == dateToFind[0]:
                busyAirplanes = voyage.getAircraftId()
                try:                                            # we use try because for each voyage we only want to remove the airplane once
                    allavalibleAirplanes.remove(busyAirplanes)  # where the airplane appears 2 times we pass when we remove it again
                except ValueError:
                    pass
        if allavalibleAirplanes == []:                          # the list is empty if there are no available airplanes
            return False
        else:
            return random.choice(allavalibleAirplanes)          # Returns the a random airplane

    def getAllCaptains(self):
        """ Gets all staff members and returns a list of all captains. """
        staffObject_list = self.mainObject.getStaffIO()
        captainObject_list = []
        for staffMember in staffObject_list:
            if staffMember.getRank() == 'captain':
                captainObject_list.append(staffMember)
        return captainObject_list

    def getAllCoPilots(self):
        """ Gets all staff members and returns a list of all Co-pilots. """
        staffObject_list = self.mainObject.getStaffIO()
        coPilotObject_list = []
        for staffMember in staffObject_list:
            if staffMember.getRank() == 'copilot':
                coPilotObject_list.append(staffMember)
        return coPilotObject_list

    def getAllFlightAttendants(self):
        """ Gets all staff members and returns a list of all flight attendants. """
        staffObject_list = self.mainObject.getStaffIO()
        flightAttendantObject_list = []
        for staffMember in staffObject_list:
            if staffMember.getRank() == 'flight attendant':
                flightAttendantObject_list.append(staffMember)
        return flightAttendantObject_list

    def getAllFlightServiceManagers(self):
        """ Gets all staff members and returns a list of all flight service managers. """
        staffObject_list = self.mainObject.getStaffIO()
        flightServiceManagerObject_list = []
        for staffMember in staffObject_list:
            if staffMember.getRank() == 'flight service manager':
                flightServiceManagerObject_list.append(staffMember)
        return flightServiceManagerObject_list

    def findAvailableFlightAttendants(self, flight):
        """ This method takes a flight as an argument, gets all flight attendants, all voyages and the desired date.
        Returns all available flight attendants for that date. """
        allFlightAttendants = self.getAllFlightAttendants()
        allVoyages = self.mainObject.getVoyagesIO()
        dateToFind = flight.getDepartureTime().split("T")
        allAvalibleFlightAttendants = []
        for flightAttendant in allFlightAttendants:
            allAvalibleFlightAttendants.append(flightAttendant.getName())  # Appending all flight attendants to the list of all available flight attendants.

        busyflightAttendants = []
        for voyage in allVoyages:
            uppcomingVoyageDates = voyage.getDepartureTime().split("T")
            if uppcomingVoyageDates[0] == dateToFind[0]:  # Index 0 of upcoming voyage date is the date.
                if voyage.getFa2() not in busyflightAttendants:
                    busyflightAttendants.append(voyage.getFa2())
                    try:
                        for flightAttendant in busyflightAttendants:  # Filtering out busy flight attendants from the list of all available flight attendants.
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
        """ This method takes a flight as an argument, gets all flight service managers, all voyages and the desired date.
        Returns all available flight service managers for that date. """
        allFlightServiceManagers = self.getAllFlightServiceManagers()
        allVoyages = self.mainObject.getVoyagesIO()
        dateToFind = flight.getDepartureTime().split("T")
        allAvalibleFlightServiceManagers = []
        for FlightServiceManager in allFlightServiceManagers:
            allAvalibleFlightServiceManagers.append(FlightServiceManager.getName())  # Appending all flight service managers to the list of all available flight service managers.

        busyFlightServiceManagers = []
        for voyage in allVoyages:
            uppcomingVoyageDates = voyage.getDepartureTime().split("T")
            if uppcomingVoyageDates[0] == dateToFind[0]:  # Index 0 of upcoming voyage date is the date.
                if voyage.getFa1() not in busyFlightServiceManagers:
                    busyFlightServiceManagers.append(voyage.getFa1())
                    try:
                        for FlightServiceManager in busyFlightServiceManagers:  # Filtering out busy flight attendants from the list of all available flight service managers.
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
        """ This method takes a flight as an argument, gets all co-pilots, all voyages and the aircraft id for the voyage.
        Returns all available co-pilots for that date that also have license on the specific aircraft. """
        allCoPilots = self.getAllCoPilots()
        allVoyages = self.mainObject.getVoyagesIO()
        dateToFind = flight.getDepartureTime().split("T")
        idToFind = flight.getAircraftId()
        allAvalibleCoPilots = []
        for coPilot in allCoPilots:
            allAvalibleCoPilots.append(coPilot.getName())  # Appending all co-pilots to the list of all available co-pilots.

        busyCoPilots = []
        for voyage in allVoyages:
            uppcomingVoyageDates = voyage.getDepartureTime().split("T")
            if uppcomingVoyageDates[0] == dateToFind[0]:  # Index 0 of upcoming voyage date is the date.
                if voyage.getCoPilot() not in busyCoPilots:
                    busyCoPilots.append(voyage.getCoPilot())
                    try:
                        for coPilot in busyCoPilots:  # Filtering out busy co-pilots from the list of all available co-pilots.
                            if coPilot in allAvalibleCoPilots:
                                allAvalibleCoPilots.remove(coPilot)
                            else:
                                pass
                    except ValueError:
                        pass
        if allAvalibleCoPilots == []:
            return False
        else:
            qualifiedCoPilots = []  # New list that will be returned which will contain only available co-pilots that also have license on the specific aircraft.
            for coPilot in allCoPilots:
                if coPilot.getLicense() == idToFind and coPilot.getName() in allAvalibleCoPilots:
                    qualifiedCoPilots.append(coPilot)
            return qualifiedCoPilots

    def findAvailableCaptains(self, flight):
        """ This method takes a flight as an argument, gets all captains, all voyages and the aircraft id for the voyage.
        Returns all available captains for that date that also have license on the specific aircraft. """
        allCaptains = self.getAllCaptains()
        allVoyages = self.mainObject.getVoyagesIO()
        dateToFind = flight.getDepartureTime().split("T")
        idToFind = flight.getAircraftId()
        allAvalibleCaptains = []
        for captain in allCaptains:
            allAvalibleCaptains.append(captain.getName())  # Appending all captains to the list of all available captains.

        busyCaptains = []
        for voyage in allVoyages:
            uppcomingVoyageDates = voyage.getDepartureTime().split("T")
            if uppcomingVoyageDates[0] == dateToFind[0]:  # Index 0 of upcoming voyage date is the date.
                if voyage.getCaptain() not in busyCaptains:
                    busyCaptains.append(voyage.getCaptain())
                    try:
                        for captain in busyCaptains:  # Filtering out busy captains from the list of all available captains.
                            if captain in allAvalibleCaptains:
                                allAvalibleCaptains.remove(captain)
                            else:
                                pass
                    except ValueError:
                        pass
                if allAvalibleCaptains == []:
                    return False
                else:
                    qualifiedCaptains = []  # New list that will be returned which will contain only available captains that also have license on the specific aircraft.
                    for captain in allCaptains:
                        if captain.getLicense() == idToFind and captain.getName() in allAvalibleCaptains:
                            qualifiedCaptains.append(captain)

                    return qualifiedCaptains

    def errorCheckDate(self, flight):
        ''' Uses a few method to error check the user date and time and returns a error message and False if it fails the checker,
         else True. we mostly use try and except and changing the string to int '''

        errorMessageDate = "Date was not entered correctly (YYYY-MM-DD), please try again "
        errorMessageTime = "Time was not entered correctly (HH:MM), please try again"
        flightTime = flight.getDepartureTime()
        date = flightTime.split("T") # date[0] is the date, date[1] is the time
        try:
            year, month, day = date[0].split("-")
            temp = datetime.date(int(year), int(month), int(day))
            if len(year) != 4:
                print(errorMessageDate)
                return False
        except ValueError:
            print(errorMessageDate)
            return False
        try:
            temp = datetime.date(int(year), int(month), int(day))
        except TypeError:
            print(errorMessageDate)
            return False
        try:
            hour, minute, second = date[1].split(":")
            temp = datetime.time(int(hour), int(minute))
        except ValueError:
            print(errorMessageTime)
            return False
        try:
            temp = datetime.time(int(hour), int(minute))
        except TypeError:
            print(errorMessageTime)
            return False
        return True

    def generateSecondFlight(self, firstFlight):
        ''' When creating a voyage the user only needs to input where he will be arriving at and when he want the flight to depart.
        Those information are sufficient to generate rest of the information as well as the returning flight'''
        departingFrom = firstFlight.getArrivingAt() # flight2 will depart from flight1 arriving destination
        arravingAt = firstFlight.getDepartingFrom() # flight 2 will always fly back to keflavik
        airplane = firstFlight.getAircraftId()      # flight 2 uses the same airplane
        departureTimeTemp = firstFlight.getArrivalTime().split("T") # use the same method that generated flight 1 arriving time
        departureTime = " ".join(departureTimeTemp)
        tdelta = datetime.timedelta(hours=int(1))   # add one hour for docking and refueling
        datetime_object = datetime.datetime.strptime(departureTime, '%Y-%m-%d %H:%M:%S')
        newDepartureTime = datetime_object + tdelta
        newtime = datetime.datetime.strftime(newDepartureTime, '%Y-%m-%dT%H:%M:%S')

        return departingFrom, arravingAt, newtime, airplane

