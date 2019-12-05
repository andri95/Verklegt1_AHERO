from MainUI.quitUI import Goodbye

class AirplaneMenu:
    def __init__(self):
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
                airplanes = [str(a) for a in AirplaneLL().getAirplanes()]
                for types in airplanes:
                    print(types)
            elif var == "2":
                print("Not yet implemented")
            elif var == "3":
                print("Not yet implemented")
            elif var == "4":
                print("Not yet implemented")
            elif var == "q":
                quitUI.Goodbye()
                break
            elif var == "0":
                return
            else:
                print("Invalid command")






