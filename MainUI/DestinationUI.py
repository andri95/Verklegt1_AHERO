from MainUI.quitUI import Goodbye
class DestinationMenu():
    def __init__(self):
        self.MAINMENU = """
############################################################
#                           _|_	               quit(q)     #
#                   --@--@--(_)--@--@--                    #
#__________________________________________________________#
#                      Destinations                        #	   			   
#                                                          #
#                                                          #
#                                                          #  
#                  1. All destinations                     #
#                  2. Add a new destination                #             
#                                                          #
#                                                          #
#                                                          #
#                                                          #
#                                                          #
#                                                          #	
#                                                          #
############################################################
"""
        self.start()

    def start(self):
        print(self.MAINMENU)
        while True:
            var = input("Input a command: ")
            if var == "1":
                print("Not yet implemented")
            elif var == "2":
                print("Not yet implemented")
            elif var == "3":
                print("Not yet implemented")
            elif var == "4":
                print("Not yet implemented")
            elif var == "q":
                quitUI.Goodbye()
            elif var == "0":
                return
            else:
                print("Invalid command")
