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
punisher_display = [
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
punisher_name_display = "▀█▀ █░█ █▀▀   █▀█ █░█ █▄░█ █ █▀ █░█ █▀▀ █▀█\n░█░ █▀█ ██▄   █▀▀ █▄█ █░▀█ █ ▄█ █▀█ ██▄ █▀▄"
#endregion


class Player:
  def __init__(self, name= "player", health=100, damage=20, coins= 0, score=1,potion_size= 20):
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
      map.Game_Over(player)
    if self.health > self.max_health:
      self.health = self.max_health

  def player_turn(self,enemy):
    print(f"{self.name} \n {self.name} = {red}{self.health}{white}/{red}{self.max_health}{white}")
    ncols = 25
    print(f"\033[F\033[{ncols}G What do you do?")
    print(f" Damage = {blue}{self.damage}{white}")
    ncols = 26
    print(f"\033[F\033[{ncols}G 1.) Heal ")
    print(f" Potion size = {green}{self.potionSize}{white}")
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
          print(f"You healed {yellow}{self.potionSize} HP{white}")
        self.health_check()
      case "2":
        print(f"You attacked the {enemy.name}{green} (-{self.damage} HP{white}")
        enemy.health -= self.damage
    os.system('cls||clear')

  def display_stats(self):  
    print(f"{self.name}{white}\nHealth = {red}{self.health}{white}\{red}{self.max_health}{white}\nDamage = {blue}{self.damage}{white}\nPotion size = {green}{self.potionSize}{white}\nCoins = {yellow}{self.coins}{white}\nScore = {magenta}{self.score}{white}")
class Enemy:
  def __init__(self, name = "Slime", health = 50, damage = 5,sprites = slime_display, name_display = slime_name_dsiplay, hit_chance = 0.75):
      self.name = name
      self.health = health
      self.max_health = health
      self.damage = damage
      self.coins = self.health
      self.spirte_sheet = sprites
      self.name_display = name_display
      self.hit_chance = hit_chance

  def enemy_turn(self,map,player):
     
    self.enemy_move = random.random()
    missed = random.random() < self.hit_chance

    # region enemy display manager
    if not missed:
      self.Expression = self.spirte_sheet[0]
    if self.health < self.max_health * 0.5:
        self.Expression = self.spirte_sheet[1]
    if missed:
      self.Expression = self.spirte_sheet[2]
    # endregion
    
    print(f"{self.name_display}\n\n {map.difficulty_colour[map.difficulty_index]}{self.Expression}\n{white}\nHealth = {self.health} / {self.max_health}\nDamage = {self.damage}")
    ##########################
    if missed:
      print(f"\nThe {self.name} Attcked! {red} (-{self.damage} HP)" + white)
      player.health -= self.damage
      player.health_check()
    else:
      print(f"\nThe {self.name} missed!")
    print("_________________________________________________\n")
      
class MapManager:
  def __init__(self):
    self.location = 0
    self.difficulty_colour = [magenta,green,yellow,red]
    self.difficulty = ["baby","easy","medium","hard"]
    self.difficulty_index = 1
    self.difficulty_modifier = 1

    self.boss_modifier = 1
        
        
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
    previous_floor = 0
    i = 0
    print(player.score % 50 ==0)
    if player.score % 50 == 0 and player.score != 0:
      self.Harder_Boss()
      print(f"From the bosses reamins you find a {red}Max Heal{white}")
      time.sleep(2 * self.speed_modifier)
      player.health = player.max_health

    while previous_floor == i:
      i = random.randint(1,5)
    previous_floor = i

    match i:
      case 1:
        self.Fight()
      case 2:
        self.Pool(player)
      case 3:
        self.Shop(player)
      case 4:
        self.Chest(player)
      case 5:
        self.Altar(player)

  def Fight(self, enemy = None):
    if enemy == None:
      enemy = Enemy()
    os.system('cls||clear')
    enemy.max_health = enemy.health * self.difficulty_modifier
    enemy.health = enemy.max_health
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
        player.score -= 1
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
            player.coins -= 100
        case "2":
          if player.coins < 250:
            poor = True
          else:
            player.damage += 20
            player.coins -= 250
        case "3":
          if player.coins < 500:
            poor = True
          else:
            player.max_health += 20
            player.coins -= 500
        case "x":
          break
    player.score -= 1

  def Chest(self,player):
    os.system('cls||clear')
    print("█▀▀ █░█ █▀▀ █▀ ▀█▀\n█▄▄ █▀█ ██▄ ▄█ ░█░\n")
    if input("you see a strange chest ahead \n Do you open it?\n1.) No\n2.) Yes\n") == "2":
      if random.randint(0,1) == 1:
        print("It was a mimic! ")
        mimic_damage = player.damage * self.difficulty_modifier
        if mimic_damage < 15:
          mimic_damage = 15
        elif mimic_damage > player.health *0.3:
          mimic_damage = player.health * 0.3
        self.Fight(enemy=Enemy(name="mimic", health=60,damage=mimic_damage,sprites=mimic_display,name_display=mimic_name_display))
        time.sleep(self.speed_modifier + 0.5)
      else:
        print(f"You found a {green}potion upgrade{white}!")
        player.potionSize += 5
        time.sleep(self.speed_modifier + 0.5)
    else:
      print("You leave it alone... ")
      player.score -= 1
    
  def Altar(self, player):
    os.system('cls||clear')
    print("▄▀█ █░░ ▀█▀ ▄▀█ █▀█\n█▀█ █▄▄ ░█░ █▀█ █▀▄\n")
    match input(" You see an ominious altar...\n It glows with a powerfull energy \n\n  1.) Leave it alone \n  2.) Apparoch the altar "):
      case "2":
        match random.randint(0,1):
          case 0:
            print(f"\nThe altar glows and you feel stronger! {red}(+20 Max HP){white}")
            player.max_health += 20
            time.sleep(self.speed_modifier + 0.5)
            os.system('cls||clear')
          case 1:
            self.Fight(enemy=Enemy(
              name = "The punisher",
              health = player.max_health + 20,
              damage = 40,
              hit_chance=0.25,
              name_display=punisher_name_display,
              sprites=punisher_display))
      case "1":
        print("you leave it alone...")
        time.sleep(2 * self.speed_modifier)
        os.system('cls||clear')
        player.score -= 1

  def Harder_Boss(self):
    os.system('cls||clear')
    print("You hear terrible footsteps appraching from the shadows... ")
    time.sleep(1)
    print("The shadows mass together as one... ")
    self.Fight(enemy=Enemy(
      name = "Bound God",
      health = 1000 * self.difficulty_modifier * self.boss_modifier,
      damage = 40 * self.difficulty_modifier * self.boss_modifier,
      sprites = harder_boss_display,
      name_display = "N/A",
      hit_chance = 0.5

    ))

    self.boss_modifier *= 1.2

  def Game_Over(self,player):
    time.sleep(2)
    os.system('cls||clear')
    print("You died! ")

    player.display_stats()

    print(f"_______________________________\nScore = {green}{player.score}{white} \n\n What now?\n1.) Play again\n2.) Quit")
    x = input()
    if x == "2":
      sys.exit("")
    else:
      os.system('cls||clear')
      self.Start_Menu()


  def Start_Game(self):
    player = Player()
    while True:
     player.score += 1
     self.Get_New_Floor()
     
map = MapManager()
player = Player()

map.Start_Menu()

'''
remainng: 
  Harder_boss :
    name display
  Coin tooss
  Cheats
  Chickens?

enemy types :
slime = No gimic
mimic = copies player's damage (applying difficulty modifer too)
        minimum damage of 15
        maximum damage of 1/3 of player's health
Punisher = Very strong, higher chance of missing(0.75), copies player's health + 20
Harder_Boss = Scales by 1.2x each time killed (stacking with difficulty modifier)
              Heals player when defeated
              Only appears ever 50 levels
              Base of 1000 health
              
'''