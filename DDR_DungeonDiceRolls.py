from random import randint
from time import sleep

# Class
class Dice:

    def __init__(self, faces, values):
        self.faces = faces
        self.values = values
    
    def check_faces(self):
        if self.faces != (4 or 6 or 8 or 10 or 12 or 20 or 100):
            self.faces == False
            if self.faces == False:
                print("Unavailable faces. Please, repeat the operation.")
                return rolldice()
            else:
                return
        else:
            return 

            
# Dices sets 
ds1, ds2, ds3, ds4, ds5, ds6 = ([], [], [], [], [], [])

# Roll
temp = list()


def rolldice():
    # part 1
    print()
    try:
        dc = int(input("Dice quantities:\n"))
        fc = int(input("Dice(s) faces:\n"))
    except ValueError as errb:
        print(f"Error in Roll section: {errb}")
        rolldice()
    roll = Dice(fc, dc)
    roll.check_faces()
    print()

    i = 1
    for x in range(0, dc):
        rand = randint(1, fc)
        temp.append(rand)
        print(f"{i}/{dc} roll: {rand}")
        i = i + 1


        # part 2
        def rolldicept2():
            print(f"\nresults:\n {temp}")
            decision = input("Want to storage this values? y/n\n")
            if decision == "y":
                global ds1, ds2, ds3, ds4, ds5, ds6
                dsopt = input(f"choose an empty variable to storage: \nds1: {ds1}\nds2: {ds2}\nds3: {ds3}\nds4: {ds4}\nds5: {ds5}\nds6: {ds6}\n\n")
                if dsopt == "ds1":
                    ds1 = temp.copy()
                    return menu()
                elif dsopt == "ds2":
                    ds2 = temp.copy()
                    return menu()
                elif dsopt == "ds3":
                    ds3 = temp.copy()
                    return menu()
                elif dsopt == "ds4":
                    ds4 = temp.copy()
                    return menu()
                elif dsopt == "ds5":
                    ds5 = temp.copy()
                    return menu()                   
                elif dsopt == "ds6":
                    ds6 = temp.copy()
                    return menu()
                else:
                    print("Only need to write 'ds+1, 2, 3, 5, 6'. \nTry again\n")
                    return rolldicept2()
            elif decision == "n":
                temp.clear()                
                return menu()
            else:
                return rolldicept2()
        # end of part 2


    return rolldicept2()
    # end of part 1


# Menu
def menu():
    print('Dungeon Dice Rolls made with Python!\n(1) Roll dices\n(2) Dices storage\n(3) Quit aplication')
    try:
        opt = int(input('Tip an option below: '))
    except ValueError as erra:
        print(f"Error in Menu Section: {erra}\n")
        menu()
    if opt == 1:
        rolldice()
    elif opt == 2:
         print(f"\nds1: {ds1}\nds2: {ds2}\nds3: {ds3}\nds4: {ds4}\nds5: {ds5}\nds6: {ds6}\n\n")
         sleep(3)
         return menu()
    else:
        print("You need to tip a number between 1 - 3. \nTry again\n")
        menu()


menu()
