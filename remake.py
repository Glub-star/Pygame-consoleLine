import random, time, sys, os

#region Colours
yellow = "\033[0;33m"
green = "\033[0;32m"
white = "\033[0;97m"
blue = "\033[0;34m"
red = "\033[0;31m"
magenta = "\033[0;35m"
#endregion

#region sprites
harder_boss_display = [
  "██▄   █████████   ▄█\n ▀██████▓█▓█▓█▓███▀ \n   ██▓█▓█▓█▓█▓█▓██  \n  ██▓█▓█▓█▓█▓█▓█▓███\n ██▓█▓█▓█▓█▓█▓█▓█▓██\n █▓█▓█▓█▓█▓█▓█▓█▓█▓█\n ██▓█▓█▓█▓█▓█▓█▓█▓██\n  ██▓█▓█▓█▓█▓█▓█▓██ \n   ██▓█▓█▓█▓█▓█▓██  \n ██▀ █████▓█▓█████  \n██       █████   ██ ",
  "██▄   █████████   ▄█\n ▀██████▓•▓•▓•▓•██▀ \n   ██▓•▓•▓•▓•▓•▓██  \n  ██▓•▓•▓•▓•▓•▓•▓███\n ██▓•▓•▓•▓•▓•▓•▓•▓██\n █▓•▓•▓•▓•▓•▓•▓•▓•▓█\n ██▓•▓•▓•▓•▓•▓•▓•▓██\n  ██▓•▓•▓•▓•▓•▓•▓██ \n   ██▓•▓•▓•▓•▓•▓██  \n ██▀ █████▓•▓█████  \n██       █████   ██ ",
  "██▄   █████████   ▄█\n ▀██████▒▓▒▓▒▓████▀ \n   ██▒▓▒▓▒▓▒▓▒▓▒██  \n  ██▒▓▒▓▒▓▒▓▒▓▒▓▒███\n ██▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒██\n █▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒█\n ██▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒██\n  ██▒▓▒▓▒▓▒▓▒▓▒▓▒██ \n   ██▒▓▒▓▒▓▒▓▒▓▒██  \n ██▀ █████▒▓▒█████  \n██       █████   ██ ",
  "██▄   █████████   ▄█\n ▀██████░░░░░░████▀ \n   ██░░░░░░░░░░░██  \n  ██░░░░░░░░░░░░░███\n ██░░░░░░░░░░░░░░░██\n █░░░░░░░░░░░░░░░░░█\n ██░░░░░░░░░░░░░░░██\n  ██░░░░░░░░░░░░▒██ \n   ██░░░░░░░░░░░██  \n ██▀ █████░░░█████  \n██       █████   ██ "
]
slime_display = [
  "         ████████\n      ████░░░░░███\n     ██░░░░░░░░░███\n    ██░░░░░░░░░░░██\n   ██░░░█░░░░█░░░██\n   █░░░░█░░░░█░░░░█\n   █░░░░░░░░░░░░░░█\n   █░░░░░░░░░░░░░░██\n   █░░░░░░░░░░░░░░██\n   ███░░░░░░░░░░░██\n     ██████████████",
  "         ████████\n      ████░░░░░███\n     ██░░░░░░░░░███\n    ██░░█░░░░░█░░██\n   ██░░░██░░██░░░██\n   █░░░░░█░░█░░░░░█\n   █░░░░░░░░░░░░░░█\n   █░░░░░░░░░░░░░░██\n   █░░░░░░░░░░░░░░██\n   ███░░░░░░░░░░░██\n     ██████████████",
  "         ████████\n      ████░░░░░███\n     ██░░░░░░░░░███\n    ██░░░░░░░░░░░██\n   ██░░░██░░░██░░██\n   █░░░░█░░░░░█░░░█\n   █░░░░▒░░░░░▒░░░█\n   █░░░░░░░░░░░░░░██\n   █░░░░░░░░░░░░░░██\n   ███░░░░░░░░░░░██\n     ██████████████",
  "         ████████\n      ████░░░░░███\n     ██░░░░░░░░░███\n    ██░░░░░░░░░░░██\n   ██░░█░█░░░█░█░██\n   █░░░░█░░░░░█░░░█\n   █░░░█░█░░░█░█░░█\n   █░░░░░░░░░░░░░░██\n   █░░░░░░░░░░░░░░██\n   ███░░░░░░░░░░░██\n     ██████████████"
]
goblin_display = [
  "      █████        \n    ███░░░░██     █\n█  ██░░░░░░░░█   ██\n██ ██░░▄░▄░░░█  █  \n █ ██░░░░░░░░████  \n ████░░░░░░░░███   \n   █████████████   \n      ███  ██      \n     ███    █      \n     ██     ██     \n     █       █     \n     █             ",
  "       █████        \n     ███░░░░██     █\n █  ██░▄░░░▄░░█   ██\n ██ ██░░█░█░░░█  █  \n  █ ██░░░░░░░░████  \n  ████░░░░░░░░███   \n    █████████████   \n       ███  ██      \n      ███    █      \n      ██     ██     \n      █       █     \n      █             ",
  "       █████        \n     ███░░░░██     █\n█  ██░░░░░░░░█   ██\n ██ ██░░▄░░▄░░█  █  \n  █ ██░░▒░░▒░░████  \n  ████░░░░░░░░███   \n    █████████████   \n       ███  ██      \n      ███    █      \n      ██     ██     \n      █       █     \n      █             ",
  "      █████        \n    ██░░░░░██     █\n█  ██░▄░▄░▄░▄█   ██\n██ ██░░█░░░█░█  █  \n █ ██░▀▒▀░▀░▀████  \n ████░░░░░░░░███   \n   █████████████   \n      ███  ██      \n     ███    █      \n     ██     ██     \n     █       █     \n     █             "
]
mimic_display = [
  "██████████████  \n██    ◾  ◾   ██ \n  ██          ██\n   ████████████ \n  █▓▓▓▓▓▓▓▓▓▓▓█ \n █▓▓▓▓▓▓▓▓▓▓▓██ \n ████████████▒█ \n █▒▒▒▒▒▒▒▒██▒▒█ \n █▒▒▒▒▒▒▒▒██▒█  \n ████████████   ",
  "   ▀▄      ▄▀   \n    ▀█▄  ▄█▀    \n██████████████  \n██    ◾  ◾   ██ \n  ██          ██\n   ████████████ \n  █▓▓▓▓▓▓▓▓▓▓▓█ \n █▓▓▓▓▓▓▓▓▓▓▓██ \n ████████████▒█ \n █▒▒▒▒▒▒▒▒██▒▒█ \n █▒▒▒▒▒▒▒▒██▒█  \n ████████████   ",
  " ██████████████  \n ██     ▄  ▄  ██ \n   ██  ▀▀  ▀▀  ██\n    ████████████ \n   █▓▓▓▓▓▓▓▓▓▓▓█ \n  █▓▓▓▓▓▓▓▓▓▓▓██ \n  ████████████▒█ \n  █▒▒▒▒▒▒▒▒██▒▒█ \n  █▒▒▒▒▒▒▒▒██▒█  \n  ████████████   ",
  "██████████████  \n██   ▄ ▄  ▄ ▄▀█ \n  ██ ▄▀▄  ▄▀▄ ██\n   ████████████ \n  █▓▓▓▓▓▓▓▓▓▓▓█ \n █▓▓▓▓▓▓▓▓▓▓▓██ \n ████████████▒█ \n █▒▒▒▒▒▒▒▒██▒▒█ \n █▒▒▒▒▒▒▒▒██▒█  \n ████████████   "
]
boss_display = [
  "▄              █\n█             ██\n██     ████████ \n ███████    ███ \n  ██          ██\n  █   ██  ██   █\n  ██          ██\n   ██        ██ \n    ██████████  \n        ██      \n      ██████    \n    ██   █  ██  \n   ██    █   ██ \n  ██     █    █ \n  █      █    █ ",
  " ▄              █\n █             ██\n ██     ████████ \n  ███████    ███ \n   ██ ▄     ▄  ██\n   █  ▀█▄ ▄█▀   █\n   ██          ██\n    ██        ██ \n     ██████████  \n         ██      \n       ██████    \n     ██   █  ██  \n    ██    █   ██ \n   ██     █    █ \n   █      █    █ ",
  "▄              █\n█             ██\n██     ████████ \n ███████    ███ \n  ██          ██\n  █   ▄█  █▄   █\n  ██  ▀█  █▀  ██\n   ██        ██ \n    ██████████  \n        ██      \n      ██████    \n    ██   █  ██  \n   ██    █   ██ \n  ██     █    █ \n  █      █    █ ",
  "▄              █\n█             ██\n██     ████████ \n ███████    ███ \n  ██ ▄ ▄  ▄ ▄ ██\n  █   █    █   █\n  ██ ▀ ▀  ▀ ▀ ██\n   ██        ██ \n    ██████████  \n        ██      \n      ██████    \n    ██   █  ██  \n   ██    █   ██ \n  ██     █    █ \n  █      █    █ "
]
title_display = "████████╗██╗░░██╗███████╗  ██████╗░██╗░░░██╗███╗░░██╗░██████╗░███████╗░█████╗░███╗░░██╗\n╚══██╔══╝██║░░██║██╔════╝  ██╔══██╗██║░░░██║████╗░██║██╔════╝░██╔════╝██╔══██╗████╗░██║\n░░░██║░░░███████║█████╗░░  ██║░░██║██║░░░██║██╔██╗██║██║░░██╗░█████╗░░██║░░██║██╔██╗██║\n░░░██║░░░██╔══██║██╔══╝░░  ██║░░██║██║░░░██║██║╚████║██║░░╚██╗██╔══╝░░██║░░██║██║╚████║\n░░░██║░░░██║░░██║███████╗  ██████╔╝╚██████╔╝██║░╚███║╚██████╔╝███████╗╚█████╔╝██║░╚███║\n░░░╚═╝░░░╚═╝░░╚═╝╚══════╝  ╚═════╝░░╚═════╝░╚═╝░░╚══╝░╚═════╝░╚══════╝░╚════╝░╚═╝░░╚══╝"
#endregion

#region name displays
slime_name_dsiplay = "█▀ █░░ █ █▀▄▀█ █▀▀\n▄█ █▄▄ █ █░▀░█ ██▄"
mimic_name_display = "█▀▄▀█ █ █▀▄▀█ █ █▀▀\n█░▀░█ █ █░▀░█ █ █▄▄"
#endregion


class Player:
  def __init__(self, name= "player", health=100, damage=20, coins= 0, score=0,potion_size= 5):
    self.name = name
    self.health = health
    self.max_health = health
    self.damage = damage
    self.coins = coins
    self.score = score
    self.potionSize = potion_size
    self.cheats = False
  
  def health_check(self):
    if self.health <= 0:
      # Game over
      pass
    if self.health > self.max_health:
      self.health = self.max_health

  def player_turn(self,enemy):
    print(f"{self.name} \n {self.name} = {red}{self.health}{white}/{red}{self.max_health}{white}")
    ncols = 25
    print(f"\033[F\033[{ncols}G What do you do?")
    print(f" Damage = {blue}{self.damage}{white}")
    ncols = 26
    print(f"\033[F\033[{ncols}G 1.) Heal ")
    print(f" Potion size = {green}{self.potionSize}{white}") ####################
    print(f"\033[F\033[{ncols}G 2.) Attack ")
    print(f" Coins = {yellow}{self.coins}{white} \n Score = {magenta}{self.score}{white}\n")
    x = input()

    match x:
      case "1":
        heal_chance = random.randint(1,4)
        if heal_chance == 4:
          print("You failed to heal! ")
        else:
          self.health += self.potionSize
          print(f"You healed {yellow}{self.potion_size} HP{white}")
        self.health_check()
      case "2":
        print(f"You attacked the {enemy.name}{green} (-{self.damage} HP{white}")
        enemy.health -= self.damage
    os.system('cls||clear')

  def display_stats(self): ################ 
    print(f"{self.name}{white}\nHealth = {red}{self.health}{white}\{red}{self.max_health}{white}\nDamage = {blue}{self.damage}{white}\nPotion size = {green}{self.potionSize}{white}\nCoins = {yellow}{self.coins}{white}\nScore = {magenta}{self.score}{white}")
    '''
    print(Cheats + name + white + "\n Health = " + red + str(phealth) + white +
        "/" + red + str(pmaxhealth) + white + "\n Damage = " + blue +
        str(pdamage) + white + "\n Potion size = " + green + str(potionSize) +
        white + "\n Coins = " + yellow + str(coins) + white + "\n Score = " +
        magenta + str(score) + white + "\n")
    '''
class Enemy:
  def __init__(self, name = "Slime", health = 50, damage = 5,sprites = slime_display, name_display = slime_name_dsiplay):
      self.name = name
      self.health = health
      self.max_health = health
      self.damage = damage
      self.coins = self.health
      self.spirte_sheet = sprites
      self.name_display = name_display

  def enemy_turn(self,map,player):
     
    self.enemy_move = random.randint(1, 4)

    # region enemy display manager
    if self.enemy_move != 4:
      self.Expression = self.spirte_sheet[0]
    if self.health < self.max_health * 0.5:
        self.Expression = self.spirte_sheet[1]
    if self.enemy_move == 4:
      self.Expression = self.spirte_sheet[2]
    # endregion
    
    print(f"{self.name_display}\n\n {map.difficulty_colour[map.difficulty_index]}{self.Expression}\n{white}\nHealth = {self.health} / {self.max_health}\nDamage = {self.damage}")
    ##########################
    if self.enemy_move != 4:
      print(f"\nThe {self.name} Attcked! {red} (-{self.damage} HP)" + white)
      player.health -= self.damage
      player.health_check()
    elif self.enemy_move == 4:
      print(f"\nThe {self.name} missed!")
    print("_________________________________________________\n")
      
class MapManager:
  def __init__(self):
    self.location = 0
    self.difficulty_colour = [magenta,green,yellow,red]
    self.difficulty = ["baby","easy","medium","hard"]
    self.difficulty_index = 1
    self.difficulty_modifier = 1
        
        
    self.speed_colour = [green,yellow,red,blue]
    self.speed = ["fast","medium","slow","fast"]
    self.speed_index = 3
    self.speed_modifier = 0.5
        
  def Start_Menu(self):
      game_start = False
      error = ""
      while not game_start:
        try:
          os.system('cls||clear')
          print(error)
          print(f"{self.difficulty_colour[self.difficulty_index]}{title_display}{white}")
          ######################
          x = int(input(f"{white}\n1.) Difficulty = {self.difficulty_colour[self.difficulty_index]}{self.difficulty[self.difficulty_index]}{white}\n2.) Game speed = {self.speed_colour[self.speed_index]}{self.speed[self.speed_index]}{white}\n3.) Start \n4.) Cheats \n{error} \n"))
          match x:
            case 1:
              self.difficulty_index +=1
              self.difficulty_modifier += 0.5
              if self.difficulty_index >= 4:
                self.difficulty_index = 0
              if self.difficulty_modifier > 2.5:
                self.difficulty_modifier = 0.5
            case 2:
                self.speed_index +=1
                self.speed_modifier += 0.5
                if self.speed_index >= 4:
                    self.speed_index = 0
                if self.speed_modifier >= 2.5:
                  self.speed_modifier = 0.5
            case 3:
                self.Start_Game()
              
            case 4:
              # open cheats menu
              pass
        except IndexError:
          error = "Give a valid option"
        except ValueError:
          error = "Enter just the number"

  def Get_New_Floor(self):
    i = random.randint(1,4)
    match i:
      case 1:
        self.Fight()
      case 2:
        self.Pool(player)
      case 3:
        self.Shop(player)
      case 4:
        self.Chest(player)

  def Fight(self, enemy = Enemy()):
    os.system('cls||clear')
    enemy.max_health = enemy.health * self.difficulty_modifier
    enemy.health = enemy.health * self.difficulty_modifier
    while enemy.health > 0:
      os.system('cls||clear')
      enemy.enemy_turn(self,player)
      player.player_turn(enemy)
    
    print(f"{enemy.spirte_sheet[3]}\n\n{white}{enemy.name_display}\n\n Health = {enemy.health} / {enemy.max_health}\n Damage = {enemy.damage}")
    time.sleep(self.speed_modifier)
    print(f"\n You killed the {enemy.name}!")
    time.sleep(self.speed_modifier)
    print(f"The {enemy.name} dropped {yellow}{enemy.coins} coins! {white}")

    player.coins += enemy.coins
    time.sleep(self.speed_modifier + 0.5)
    os.system('cls||clear')
  
  def Pool(self,player):
    os.system('cls||clear')
    choice  = 0
    print("█▀█ █▀█ █▀█ █░░\n█▀▀ █▄█ █▄█ █▄▄\n")
    while True:
      try:
        choice = int(input("you see a glowing orb at the bottom of a lake?\nDo you swim to get it?\n1.) No\n2.) Yes\n"))
        if choice > 2 or choice < 1:
          raise IndexError
        break
      except ValueError:
        print("Enter just the number ")
      except IndexError:
        print("Enter a valid number ")
  
    outcome = random.randint(1, 2)
    match choice:
      case 2:
        match outcome:
          case 1:
            print(f"You found a {blue}whetstone (+20 ATK){white}")
            player.damage += 20
            time.sleep(self.speed_modifier)

          case 2:
            print(f"It was a{red} trap (-15 HP) {white}")
            player.health -= 15
            player.health_check()
      case 1:
        print("You leave it alone... ")
    time.sleep(self.speed_modifier)
  
  def Shop(self,player):
    poor = False
    while True:
      os.system('cls||clear')
      if poor:
        print("You didnt have enough coins!")
        poor = False
      print("█▀ █░█ █▀█ █▀█\n▄█ █▀█ █▄█ █▀▀\n")
      print("You found a shop! ")
      print(f"You have {yellow}{player.coins} coins{white}\n1.) {red}Max Heal{yellow} (100 coins){white}\n2.) {blue}Whetstone{yellow} (250 coins){white}\n3.) {red}Max Health{yellow} (500 coins){white}\nx.) leave\n\n")
      player.display_stats()
      choice = input()
      match choice:
        case "1":
          if player.coins < 100:
            poor = True
          else:
            player.health = player.max_health
        case "2":
          if player.coins < 250:
            poor = True
          else:
            player.damage += 20
        case "3":
          if player.coins < 500:
            poor = True
          else:
            player.max_health += 20
        case "x":
          break

  def Chest(self,player):
    os.system('cls||clear')
    print("█▀▀ █░█ █▀▀ █▀ ▀█▀\n█▄▄ █▀█ ██▄ ▄█ ░█░\n")
    if input("you see a strange chest ahead \n Do you open it?\n1.) No\n2.) Yes\n") == "2":
      if random.randint(0,1) == 1:
        print("It was a mimic! ")
        self.Fight(enemy=Enemy(name="mimic", health=60,damage=player.damage,sprites=mimic_display,name_display=mimic_name_display))
        time.sleep(self.speed_modifier + 0.5)
      else:
        print(f"You found a {green}potion upgrade{white}!")
        player.potionSize += 5
        time.sleep(self.speed_modifier + 0.5)
    
    
      



  def Start_Game(self):
    while True:
     self.Get_New_Floor()
     player.score += 1

map = MapManager()
player = Player()

map.Start_Menu()
