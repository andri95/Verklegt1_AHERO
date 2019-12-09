class SecretUI:
    def __init__(self):

        self.CHUCKNORRIS = """
                                       MMMMMMMMMMMMMMMMM
                                   NMMMMMMMMMMMMMMMMMMMMMMMM
                                 MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
                                MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN
                                MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
                               MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
                               MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMD
                              DMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
                              MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
                              MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
                             MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
                             MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
                            MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN
                            MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN
                           MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN
                           MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN
      NM                  MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
      MMMMM              MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
       MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMMMMM8MMMMMMMMMIMMMMM8,. ...........OMMMMMMMMMMMMMMMMMMMMMMMMMMMM
           MMMMMMMMMMMMMMMMMMMMMMM ..N. .....~MMMM...............:MMMMNMMMMMMMMMMMMMMMMMMMMMMM
             NMMMMMMMMMMMMMMMMMMMMM.....:..DMMMMMNZ Z.... .......M$MMMMMMMMMMMMMMMMMMMMMMMMMMM
                 MMMMMMMMMMNMMMMMMM....... 7=MMMMMMO....Z .......MM7MMMMMMMMMMMMMMMMMMMMMMMMM
                    MMMMMMMMMMMMMMMMM  Z...MMMZ .. .,M..,........MMMMMMMMMMMMMMMMMMMMMMMMMMMM
                        MMMMMM.......DOM ....N7..................MMMMMMMMMMMMMMMMMMMMMMMMMMM
                           MMM....... M. ... .  ... ..............M...$MMMMMMMMMMMMMMMMMMMM
                             ........... ........~. ..............M..=....+MMMMMMMMMMMMMM
                             ......+.NMI~........ . ..............M.,.I...MMMMMMMMMMMMMMN
                             ......$... ...... O..................,.....$MMMMMMMMMMMMN
                             .....M.......... M M.. .............. 8  .OMMMMMMMMMMMN
                              ..=7I,,.,,IMI...M.................. ..MMMMMMMMMMM
                              ....DMMMMMMMMMMMMMMMO..............D...MMMMMMMMM
                               .MMMMMMMMMMMMMMDDMM:,N..............DMMMMMMMMMMM
                               NMMMMMNMM8 . .... ...,~............  MMMMMMMMM
                               MMMMM,:......::~..M8M8MM...............MMMMMM
                               MMMM ... . .........,MM..............MMMMMO$
                               MMMMM... =.=. .. . . MM ....... . ...MMMMMMM
                                NMMMMMMMMMM?  ..O.?NM7 ....... ......MMMMMM
                                 NMMMMMMMMMMMMMMMMM........  $ . ...MMMNMMM
                                  MMMMMMMMMMMMMMM.........,, ......MMMMMMMM
                                   OMMMMMMMM8 , .. .. .,N.... ...:MMMMMMMMMMN
                                    MMMMMMMM?N. ...~MD.:MNI8MMMMMMMMMMMMMMMMMN
                               MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN
                            NMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN
                           MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN
                        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
                     MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
                    NMMMMMMMMMMMMNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
                   MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
____    ____  ______    __    __   ______    ____  _______     _______   ______    __    __  .__   __.  _______           
\   \  /   / /  __  \  |  |  |  | (_ )   \  /   / |   ____|   |   ____| /  __  \  |  |  |  | |  \ |  | |       \          
 \   \/   / |  |  |  | |  |  |  |  |/ \   \/   /  |  |__      |  |__   |  |  |  | |  |  |  | |   \|  | |  .--.  |         
  \_    _/  |  |  |  | |  |  |  |      \      /   |   __|     |   __|  |  |  |  | |  |  |  | |  . `  | |  |  |  |         
    |  |    |  `--'  | |  `--'  |       \    /    |  |____    |  |     |  `--'  | |  `--'  | |  |\   | |  '--'  |         
    |__|     \______/   \______/         \__/     |_______|   |__|      \______/   \______/  |__| \__| |_______/          
                                                                                                                          
  ______  __    __   __    __    ______  __  ___    .__   __.   ______   .______      .______       __       _______. __  
 /      ||  |  |  | |  |  |  |  /      ||  |/  /    |  \ |  |  /  __  \  |   _  \     |   _  \     |  |     /       ||  | 
|  ,----'|  |__|  | |  |  |  | |  ,----'|  '  /     |   \|  | |  |  |  | |  |_)  |    |  |_)  |    |  |    |   (----`|  | 
|  |     |   __   | |  |  |  | |  |     |    <      |  . `  | |  |  |  | |      /     |      /     |  |     \   \    |  | 
|  `----.|  |  |  | |  `--'  | |  `----.|  .  \     |  |\   | |  `--'  | |  |\  \----.|  |\  \----.|  | .----)   |   |__| 
 \______||__|  |__|  \______/   \______||__|\__\    |__| \__|  \______/  | _| `._____|| _| `._____||__| |_______/    (__) """
        self.start()


    def start(self):
        print(self.CHUCKNORRIS)
        while True:
            user_input = input("Enter a command:")
            if user_input == "0":
                return
            else:
                print("The mighty Chuck Norris doesn't allow that")