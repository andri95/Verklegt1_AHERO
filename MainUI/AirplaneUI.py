
class Airplanemenu:
    def __init__(self):
        self.MAINMENU = """
############################################################
#		           _|_	                       quit(q)     #		  
#		    --@--@--(_)--@--@--	 		                   #
#__________________________________________________________#				  					                   
#			Airplanes			                           #
#		   					                               #
#		   					                               #
#		   					                               #
#		   1. List Airplanes			                   #
#		   2. Add Airplane			                       #
#							                               #
#						                                   #
#							                               #
#							                               #
#							                               #
# 0. Back						                           #
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
                Goodbye()
                break
            elif var == "0":
                return
            else:
                print("Invalid command")






