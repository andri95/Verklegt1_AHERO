
class AirplaneData():
    def __init__(self, planeId, airtype, Model, capacity):
        self.planeId = planeId
        self.type = airtype
        self.Model = Model
        self.capacity = capacity


    def getPlaneId(self):
        return self.planeId

    def getType(self):
        return self.type

    def getModel(self):
        return self.Model

    def getCapacity(self):
        return self.capacity

    fieldnames = ["flightNumber", "departingFrom", "arrivingAt", "departure", "arrival"]
