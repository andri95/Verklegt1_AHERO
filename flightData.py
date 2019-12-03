
class FlightData:
    def __init__(self, destination, date, time, pilots, flightAttentants, flightID):
        self.destination = destination
        self.date = date
        self.time = time
        self.pilots = pilots
        self.flightAttentants = flightAttentants
        self.flightID = flightID

    def getDestination(self):
        return self.destination

    def getDate(self):
        return self.date

    def getTime(self):
        return self.time

    def getPilots(self):
        return self.pilots

    def getFlightAttendants(self):
        return self.flightAttentants

    def getFlightID(self):
        return self.flightID

    def __str__(self):
        return 'Destination: {}\nDate: {}\nTime: {}\nPilots: {}\nFlight Attentants: {}\nVoyage ID: {}'.format(self.destination, self.date, self.time, '\n'.join([pilot for pilot in self.pilots]), '\n'.join([fa for fa in self.flightAttentants]), self.flightID)
