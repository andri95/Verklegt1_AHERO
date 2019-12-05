from IO.mainIO import MainIO

class VoyageLL():
    def __init__(self):
        self.MainObject = MainIO()

    
    def listVoyage(self):
        return self.MainObject.getVoyagesIO()
        
