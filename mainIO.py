from IO.createIO import CreateIO
from IO.readIO import ReadIO
from IO.updateIO import UpdateIO


class MainIO:

    def __init__(self, dataList):
        self.dataList = dataList
        #self.createObject = CreateIO()
        #self.readObject = ReadIO()
        self.updateObject = UpdateIO()

    def updateDestIO(self):
        return self.updateObject.updateDest(self.dataList)

    def addLicenseIO(self):
        return self.updateObject.addLicense(self.dataList)

    

    

    