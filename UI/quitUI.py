
class QuitUI:
    def __init__(self):
        self.goodbye = """
############################################################
#                                                          #
#         ______                                           #
#         _\ _~-\___                                       #
#  = = =(____NaN____D                                      #
#            \_____\___________________,-~~~~~~~`-.._      #
#             /     o O o o o o O O o o o o o o O o  |\_   #
#             `~-.__        ___..----..                  ) #
#                   `---~~\___________/------------`````   #
#                   =  ===(_________D#                     #
#                                                          #				
#                                                          #
#                      GOODBYE.......                      #
#                                                          #
#                                                          #
#                                                          #
############################################################
"""
        self.start()

    def start(self):
        print(self.goodbye)     
        quit()                  
	
