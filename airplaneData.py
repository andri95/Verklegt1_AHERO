
class AirplaneData():
    def __init__(self, id, type, manufacturer, capacity):
        self.id = id
        self.type = type
        self.manufacturer = manufacturer
        self.capacity = capacity
    def __str__(self):
        return "".format(self.id, self.type, self.type, self.manufacturer, self.capacity)


newAirplane = AirplaneData("NABAE146", "F28", "BAE", 82 )
print(newAirplane)