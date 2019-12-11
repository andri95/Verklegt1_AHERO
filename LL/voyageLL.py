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
        destination = flight.getArrivingAt()
        destinationList = self.mainObject.getDestinationsIO()
        for dest in destinationList:
            if dest.getCountry() == destination:
                return dest.getDestId()
            else:
                result = False
        return result

    def findArrivalTime(self, flight):
        allDest = self.mainObject.getDestinationsIO()
        for dest in allDest:
            if dest.getCountry() == flight.getArrivingAt():
                flightTime = dest.getFlightTime()
        if flightTime == "0":
            for dest in allDest:
                if dest.getCountry() == flight.getDepartingFrom():
                    flightTime = dest.getFlightTime()

        departureTimeTemp = flight.getDepartureTime().split("T")
        departureTime = " ".join(departureTimeTemp)
        tdelta = datetime.timedelta(hours=int(flightTime))

        datetime_object = datetime.datetime.strptime(departureTime, '%Y-%m-%d %H:%M')
        totalTime = datetime_object + tdelta
        return totalTime
        #print("lendinga tími: ", totalTime)


        #print(datetime_object)
        #print(totalTime)
        #return totalTime



    def availableDates(self):
        availableDates_list = []
        voyageObject_list = self.mainObject.getVoyagesIO()
        for voyage in voyageObject_list:
            departureTime = voyage.getDepartureTime()
            date = departureTime.split('T')
            if date[0] not in availableDates_list:
                availableDates_list.append(date[0])
        return availableDates_list

<<<<<<< HEAD
    
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
=======
    def findAvalibleAirplanes(self):
        allNanPlanes = self.mainObject.getAirplanesIO()
        allVoyages = self.mainObject.getVoyagesIO()
        avalibleAirplanes = []
        for plane in allNanPlanes:
            pass
        print(avalibleAirplanes)

>>>>>>> 050c7543bc4ca316d42a38e36007d9f108ba53c5
