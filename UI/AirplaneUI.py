from UI.quitUI import Goodbye
from Models.airplaneData import AirplaneData
from LL.mainLL import MainLL

class AirplaneMenu:
    def __init__(self):
        self.mainObject = MainLL()
        self.MAINMENU = """
############################################################
#                           _|_	               quit(q)     #
#                   --@--@--(_)--@--@--                    #
#__________________________________________________________#				  					                   
#                                                          #
#                       Airplanes                          #
#                                                          #
#                   1. list Airplanes                      #
#                   2. Add airplanes                       #
#                                                          #
#                                                          #
#                                                          #
#                                                          #
#                                                          #
#                                                          #
# 0. Back                                                  #
############################################################
"""
        self.start()

    def start(self):
        print(self.MAINMENU)
        while True:
            var = input("Input a command: ")
            if var == "1":
                airplanes = [str(a) for a in self.mainObject.getAirplanesLL()]
                for line in airplanes:
                    print(line)
                input("press any key to continue.")
                break

            elif var == "2":
                planeID = input("Enter airplane ID: ")
                types = input("Enter Airplane type: ")
                model = input("Enter Model name: ")
                capacity = input("Enter Airplane Capacity")
                newAirplane = AirplaneData(planeID, types,model,capacity)
                MainLL().AirplaneLL.addAirplane(newAirplane)
                print("New airplane saved!")
                input("Press any key to continue.")
                break
          
            elif var == "q":
                Goodbye()
                break
            elif var == "0":
                return
            else:
                print("Invalid command")






