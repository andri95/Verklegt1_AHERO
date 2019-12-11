from IO.mainIO import MainIO




class DestinationLL():
    def __init__(self):
        self.mainObject = MainIO()

    def addNewDestination(self, newDestination):
        return self.mainObject.addNewDestIO(newDestination)
        
    def getDestination(self):
        return self.mainObject.getDestinationsIO()
    
    def getDestinationByID(self, country):
        destinationObjectList = self.mainObject.getDestinationsIO()
        for destination in destinationObjectList:
            if destination.getCountry == country:
                return destination
        
    def updateDestination(self, dataList):
        return self.mainObject.updateDestIO(dataList)

    def generadeDestinationId(self):
        destinationObjectList = self.mainObject.getDestinationsIO()
        destinationID_list = []
        for destID in destinationObjectList:
           destinationID_list.append(destID.getDestId())
        lastID = destinationID_list[-1]
        newId = int(lastID) + 1
        newId = '0' + str(newId)
        return newId



