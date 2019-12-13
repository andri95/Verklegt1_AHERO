from IO.mainIO import MainIO

class DestinationLL():
    ''' DestinationLL class has methods that performs methods offered in the destination user interface'''
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
        ''' When creating a destination we call this method to generate the id'''
        destinationObjectList = self.mainObject.getDestinationsIO()
        destinationID_list = []
        for destID in destinationObjectList:
           destinationID_list.append(destID.getDestId())
        lastID = destinationID_list[-1]
        newId = int(lastID) + 1
        newId = '0' + str(newId)
        return newId



