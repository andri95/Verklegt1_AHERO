
class AirplaneData():
    def __init__(self, planeId, type, manufacturer, capacity):
        self.planeId = planeId
        self.type = type
        self.manufacturer = manufacturer
        self.capacity = capacity


    def getPlaneId(self):
        return self.planeId

    def getType(self):
        return self.type

    def getManufacturer(self):
        return self.manufacturer

    def getCapacity(self):
        return self.capacity

