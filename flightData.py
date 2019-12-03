
class FlightData:
    def __init__(self, flightNumber, departingFrom, arrivingAt, departure, arrival):
        self.flightNumber = flightNumber
        self.departingFrom = departingFrom
        self.arrivingAt = arrivingAt
        self.departure = departure
        self.arrival = arrival


    def getFlightNumber(self):
        return self.flightNumber

    def getDepartingFrom(self):
        return self.departingFrom

    def getDrrivingAt(self):
        return self.arrivingAt

    def getDeparture(self):
        return self.departure

    def getArrival(self):
        return self.arrival

    def __str__(self):
        return 'Destination: {}\nDate: {}\nTime: {}\nPilots: {}\nFlight Attentants: {}\nVoyage ID: {}'.format(self.destination, self.date, self.time, '\n'.join([pilot for pilot in self.pilots]), '\n'.join([fa for fa in self.flightAttentants]), self.flightID)

''' ÓKLÁRAÐ, ÞURFUM AÐ GERA READIO FYRST'''