import csv
class FileHandler:

    def __init__(self, path):
        self.path = path

    def readFile(self):
        returnFile = open(self.path, 'r')
        return returnFile

    def writeFile(self):
        returnFile = open(self.path, 'w')
        return returnFile

    def appendFile(self):
        returnFile = open(self.path, 'a')
        return returnFile

    def findFieldNames(self):
        fileStream = open(self.path, 'r')
        reader = csv.reader(fileStream)
        self.fieldnames = next(reader)
        return self.fieldnames






    