
class FlightData:
    def __init__(self, destination, date, time, pilots, flightAttentants, flightID):
        self.destination = destination
        self.date = date
        self.time = time
        self.pilots = pilots
        self.flightAttentants = flightAttentants
        self.flightID = flightID

    def __str__(self):
        return 'Destination: {}\nDate: {}\nTime: {}\nPilots: {}\nFlight Attentants: {}\nVoyage ID: {}'.format(self.destination, self.date, self.time, '\n'.join([pilot for pilot in self.pilots]), '\n'.join([fa for fa in self.flightAttentants]), self.flightID)
