from UI.quitUI import Goodbye
class VoyageMenu():
    def __init__(self):
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
                print("Not yet implemented")
            elif var == "2":
                print("Not yet implemented")
                #Addvoyage()
            elif var == "3":
                print("Not yet implemented")
                #Editvoyage()
            elif var == "4":
                print("Not yet implemented")
            elif var == "q":
                quitUI.Goodbye()
            elif var == "0":
                return
            else:
                print("Invalid command")




