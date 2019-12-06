from UI.quitUI import QuitUI
#from Models.voyageData import VoyageData
from Models.inputHandler import InputHandler
from LL.mainLL import MainLL

class VoyageUI():
    def __init__(self):
        self.mainObject = MainLL()
        self.inputObject = InputHandler()
        self.MAINMENU = """
############################################################
#                           _|_	               quit(q)     #
#                   --@--@--(_)--@--@--                    #
#__________________________________________________________#
#                                                          #
#                         Voyage                           #
#                                                          #
#                 1.List voyages                           #
#                 2.Add voyage                             #
#                 3.Edit voyage                            #
#                 4.?                                      #
#                                                          #
#                                                          #
#                                                          #
#                                                          #
#                                                          #
#  0.Back                                                  #
############################################################	
"""
        self.start()

    def start(self):
        
        while True:
            print(self.MAINMENU)
            var = input("Input a command: ")
            if var == "1":
                voyageObject_list = self.mainObject.getVoyageLL()
                for voyage in voyageObject_list:
                    print("Pilot: {} Co-Pilot: {} Flight attendants: {}, {}".format(voyage.getPilot(),voyage.getCoPilot(),voyage.getFa1(),voyage.getFa2()))
                input("Press any key to continue.")
                break
            
            elif var == "2":
                print("Not yet implemented")
                #Addvoyage()
            elif var == "3":
                print("Not yet implemented")
                #Editvoyage()
            elif var == "4":
                print("Not yet implemented")
            elif var == "q":
                QuitUI()
            elif var == "0":
                return
            else:
                print("Invalid command")




