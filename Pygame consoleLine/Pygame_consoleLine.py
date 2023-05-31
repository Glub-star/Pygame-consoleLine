from ctypes.wintypes import INT
from inspect import getfullargspec, ismemberdescriptor
from math import remainder
from re import sub
import time,random,os,sys
from tkinter.tix import INTEGER



# colours #
yellow = "\033[0;33m"
green = "\033[0;32m"
white = "\033[0;97m"
blue = "\033[0;34m"
red = "\033[0;31m"
magenta = "\033[0;35m"
# colours #



# globals #
Cheats = False
isBoss = 0
isMimic = 1
potionSize = 0
phealth = 0
pdamdage = 0
pmaxhealth = 0
score = 0
coins = 0
difficulty = 0
difficultyModifier = 0
speedModifier = 0
speed = 0
Quit = False
# globals #



def StartMenu():
   global name
   global phealth
   global pmaxhealth
   global pdamage
   global coins
   global score
   global potionSize

   global isMimic
   global isBoss

   global Cheats
   global difficulty
   global speed
   global difficultyModifier
   global speedModifier
   startgame = False

   diffcolour = " "
   speedColour = " "

   while startgame != True:
       

       if difficulty == 3:
           difficulty = 0

       if difficulty == 0:
           diffcolour =  green + "easy" + white
           difficultyModifier = 1
       elif difficulty == 1:
           diffcolour =  yellow + "medium" + white
           difficultyModifier = 1.5
       elif difficulty == 2:
           diffcolour = red + "hard" + white
           difficultyModifier = 2


       if speed == 4:
           speed = 0

       if speed == 0:
           speedColour = green + "fast" + white
           speedModifier = 1
       elif speed == 1:
           speedColour =  yellow + "medium" + white
           speedModifier = 1.5
       elif speed == 2:
           speedColour = red + "slow" + white
           speedModifier = 2
       elif speed == 3:
           speedColour = blue + "V fast" + white
           speedModifier = 0.5

       print("\n1.) Difficulty = " + diffcolour + "\n2.) Game speed = " + speedColour + " \n3.) Start" + "\n4.) Cheats ")
       x = input("")

       if x == "1":
           difficulty = difficulty + 1
       elif x == "2":
           speed = speed + 1
       elif x == "3":

           Cheats = magenta
           isMimic = 1
           isBoss = 0
           score = 0
           phealth = 100
           pdamage = 20
           pmaxhealth = 100
           potionSize = 5

           startgame = True
           FloorManager()

       elif x == "4":

           done = False
           coins = 0
           score = 0
           phealth = 100
           pdamage = 20
           pmaxhealth = 100
           potionSize = 5

           while done != True:
               Cheats = red
               os.system('Cls||Clear')
               z = 0
               z = input("1.) Max Health = " + str(pmaxhealth) + "\n2.) Health = "+str(phealth) + "\n3.) Damage = " + str(pdamage) + "\n4.) Potion Size = " + str(potionSize) + "\n5.) Coins = " + str(coins) + "\n6.) Score = " + str(score) + "\n7. Done \n")
               if z != "7":
                    y = input("What would you like to change the value to? ")
               if z == "1":
                   pmaxhealth = int(y)
               elif z == "2":
                   phealth = int(y)
               elif z == "3":
                   pdamage = int(y)
               elif z == "4":
                   potionSize = int(y)
               elif z == "5":
                   coins = int(y)
               elif z == "6":
                   score = int(y)
               elif z == "7":
                   print("Setup Done \n Starting game. . .")
                   done = True
                   time.sleep(1)
              

           startgame = True
           FloorManager()
       os.system('cls||clear')

def HC():
    global phealth
    global pmaxhealth

    if phealth <= 0:
        GameOver()
    if phealth > pmaxhealth:
        phealth = pmaxhealth

def Fight():
    global Cheats
    global isBoss
    global isMimic
    global speedModifier
    global pdamage
    global score
    global phealth
    global difficultyModifier
    global potionSize
    global coins
    ecoins = 0



    subtract = 0

    if score >= 100:
        subtract = 99
    elif score <= 0:
        subtract = 1
    else:
        subtract = score

    maxVal = 100 - subtract

    goblinChance = random.randint(1,maxVal)

    if goblinChance == 1:
        enemy = 1
    else:
        enemy = 0


    if enemy == 0:
        ename = green+"Slime"+white
        emaxhealth = int(50 * difficultyModifier)
        ehealth = int(emaxhealth)
        edamage = 5 
    elif enemy == 1:
        ename = green+"Goblin"+white
        emaxhealth = int(70 * difficultyModifier)
        ehealth = int(emaxhealth)
        edamage = 15

    if isMimic == 2:
        ename = green + "Mimic" + white
        emaxhealth = int(60 * difficultyModifier)
        ehealth = emaxhealth
        edamage = int(pdamage)
        if edamage > 50:
            edamage = 50

    if isBoss == 1:
        ename = green + "The punisher" + white
        emaxhealth = int(250 * difficultyModifier)
        ehealth = emaxhealth
        edamage = 30
        
    ecoins = ehealth

    while ehealth > 1:
        print(" " + ename + "\n Health = " + str(ehealth) + "/" + str(emaxhealth) + "\n Damage = " + str(edamage))
        emove = random.randint(1,4)
        if emove != 4:
            print("\nThe " + ename + " Attcked! " + red + "(-" + str(edamage) + " HP)\n" + white)
            phealth = phealth - edamage
            HC()
        elif emove == 4:
            print("\nThe " + ename + " missed!\n")

        DisplayStats()

        print("what do you do? \n1.) heal \n2.) Attack")
        choice = input()
        if choice == "1":
            HealChance = (1,4)
            if HealChance != 4:
                print("You failed to heal! ")
            else:
                phealth = phealth + potionSize
                print("You healed " + yellow + str(potionSize) + " HP" + white)
            HC()
        elif choice == "2":
            print("You attacked the " + ename + green + " (-" + str(pdamage) + " HP)" + white)
            ehealth = ehealth - pdamage
        time.sleep(speedModifier)

        if ehealth <= 0:
            isMimic = 1
            isBoss = 0
            print("You killed the " + ename +"!")
            print("The "+ ename + " dropped " + yellow +str(ecoins) + " coins! " + white)
            coins = coins + ecoins
            time.sleep(speedModifier + 0.5)
        os.system('cls||clear')

def pool():
    global speed
    global pdamage
    global phealth

    print("you see a glowing orb at the bottom of a lake?\nDo you swim to get it?\n1.) No\n2.) Yes")
    choice = input()
    x = random.randint(1,2)
    if choice == "2":
        if x == 1:
            print("You found a "+blue+" whetstone (+20 ATK)" + white)
            pdamage = pdamage + 20
            time.sleep(speedModifier)

        elif x == 2:
            print("It was a " + red + " trap (-15 HP) "+ white)
            phealth = phealth - 15
            time.sleep(speedModifier)

            HC()
    os.system('cls||clear')

def Chest():
    global isMimic
    global potionSize

    isMimic = 1

    print("you see a strange chest ahead \n Do you open it?\n1.) No\n2.) Yes")
    x = input()
    if x == "1":
        print("You leave the chest alone... ")
    elif x == "2":
        isMimic = random.randint(1,2)
        if isMimic == 1:
            print("You found a " + green + "potion upgrade! " + white)
            potionSize = potionSize + 5
            time.sleep(speedModifier + 0.5)
            os.system('cls||clear')
        elif isMimic == 2:
            os.system('cls||clear')
            print("It was a mimic! ")
            Fight()

def altar():
    global speedModifier
    global pmaxhealth
    global isBoss
    isBoss = 0
    x = ""

    x = input(" You see an ominious altar...\n It glows with a powerfull energy \n\n  1.) Leave it alone \n  2.) Apparoch the altar ")
    if x == "2":
        y = random.randint(1,4)
        if y == 1:
            print("\nThe altar glows and you feel stronger! "+ red + "(+20 Max HP)" + white )
            pmaxhealth = pmaxhealth + 20
            time.sleep(speedModifier + 0.5)
            os.system('Cls||Clear')
        else:
            isBoss = 1
            Fight()
            os.system('Cls||Clear')
    else:
        print("You leave the altar alone... ")
        time.sleep(speedModifier)
        os.system('Cls||Clear')
        
def FloorManager():
    global name
    global score
    global Quit
    

    name = input ("what is your name adventurer? ")
    os.system('cls||clear')

    while Quit != True:


        en = random.randint(1,5)

        if en == 1:
            Fight()
        elif en == 2:
            pool()
        elif en == 3:
            Chest()
        elif en == 4:
            Shop()
        elif en == 5:
            altar()
        
        
        score = score + 1

def GameOver():
    time.sleep(2)
    print("You died! ")
    os.system('cls||Clear')
    print("You died! ")

    DisplayStats()

    print("Score = " + green + str(score) + white + "\n\n What now?\n1.)Play again\n2.)Quit")
    x = input()
    if x == "1":
        StartMenu()
    elif x == "2":
       sys.exit("You exited the app")

def DisplayStats():
    global Cheats
    global name
    global phealth
    global pmaxhealth
    global pdamage
    global potionSize
    global coins

    print(Cheats + name + white + "\n Health = "+ red + str(phealth) + white + "/" + red + str(pmaxhealth) + white + "\n Damage = "+ blue + str(pdamage) + white + "\n Potion size = " + green + str(potionSize) + white + "\n Coins = " + yellow + str(coins) + white + "\n Score = " + magenta + str(score) + white + "\n")

def Shop():
    global pmaxhealth
    global pdamage
    global phealth
    global coins
    Exit = False
    cost = 0

    while Exit != True :
        x = ""
        print("You found a shop! ")
        print("You have " + yellow + str(coins) + " Coins\n" + white + "1.) " + red + "Hax heal "+ yellow + "(100 coins)\n" + white + "2.) " + blue + "Whetstone " + yellow + "(250 coins)\n" + white + "3.) " + red + "Max Health " + yellow + "(500 coins)\n" + white + "5.) Leave")
        print("\n")
        DisplayStats()
        x = input()
        os.system('cls||clear')


        if x == "1":
            cost = 100
        if x == "2":
            cost = 250
        if x == "3":
            cost = 500
        if x == "5":
            Exit = True
            cost = 0
            x = ""


        if cost > coins:
            print("You dont have enough " + yellow + "coins" + white)
        else:
            coins = coins - cost
            if x == "1":
                phealth = pmaxhealth
            elif x == "2":
                pdamage = pdamage + 20
            elif x == "3":
                pmaxhealth = pmaxhealth + 20

            

StartMenu()