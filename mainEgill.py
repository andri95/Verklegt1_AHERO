from IO.createIO import CreateIO
from Models.flightData import FlightData
from Models.voyageData import VoyageData

ioTest = CreateIO()
new_flight = FlightData("hope", "dis", "shit", "work", "now")
ioTest.addNewFlight(new_flight)

new_flight2 = FlightData("Also", "hope", "dis", "shit", "work")
ioTest.addNewFlight(new_flight2)

new_voyage = VoyageData(new_flight, new_flight2, "Raj", "leonard", "steve", "howard", "sheldon")
ioTest.addNewVoyage(new_flight, new_flight2, new_voyage)
