
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

    def setSSN(self, newPlaneId):
        self.planeId = newPlaneId

    def setType(self, newType):
        self.type = newType

    def setModel(self, newModel):
        self.Model = newModel

    def setCapacity(self, newCapacity):
        self.capacity = newCapacity




