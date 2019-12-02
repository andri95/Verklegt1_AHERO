def make_menu_list():
    menu = open("Menus.txt", 'r')
    print_list = []
    temp = []
    for line in menu:
        line = line.strip()
        if line == "":
            print_list.append(temp)
            
            temp = []
        else:
            temp.append(line)

    menu.close()
    return print_list


def print_main(list_menu):
    ''' returns main menu '''
    main = list_menu[0]
    
    for line in main:
        print(line)



def print_airplanes(list_menu):
    ''' returns airplanes submenu '''
    air_planes = list_menu[1]
    
    for line in air_planes:
        print(line)
    


def print_voyage(list_menu):
    ''' returns voyage submenu '''

    voyage = list_menu[2]
    for line in voyage:
        print(line)

  




def main():

    list_menu = make_menu_list()
    
    print_main(list_menu)
    print_airplanes(list_menu)
    print_voyage(list_menu)

main()