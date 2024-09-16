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
    print(f"{self.name} \n {self.health} ={red}{self.health}{white}/{red}{self.max_health}{white}")
    ncols = 25
    print(f"\033[F\033[{ncols}G What do you do?")
    print(f" Damage ={blue}{self.damage}{white}")
    ncols = 26
    print(f"\033[F\033[{ncols}G 1.) Heal ")
    print(f" Potion size = {green}{self.potionSize}{white}") ####################
    print(f"\033[F\033[{ncols}G 2.) Attack ")
    print(f" Coins = {yellow}{self.coins}{white} \n Score ={magenta}{self.score}{white}\n")
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
    
    print(f"{self.name}\n\n {map.difficulty_colour[map.difficulty_index]}{self.Expression}\n{white}Health = {self.health} / {self.max_health}\n Damage = {self.damage}")
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
    self.difficulty_colour = [green,yellow,red,magenta]
    self.difficulty = ["easy","medium","hard","baby"]
    self.difficulty_index = 0
        
        
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
          print(f"{self.difficulty_colour}{title_display}{white}")
          ######################
          x = int(input(f"{white}\n1.) Difficulty = {self.difficulty_colour[self.difficulty_index]}{self.difficulty[self.difficulty_index]}{white}\n2.) Game speed = {self.speed_colour[self.speed_index]}{self.speed[self.speed_index]}{white}\n3.) Start \n4.) Cheats \n{error} \n"))
          match x:
            case 1:
              self.difficulty_index +=1
              if self.difficulty_index >= 4:
                self.difficulty_index = 0
            case 2:
                self.speed_index +=1
                self.speed_modifier += 0.5
                if self.speed_index >= 4:
                    self.speed_index = 0
                if self.speed_modifier >= 2.5:
                  self.speed_modifier = 0.5
            case 3:
                # START Game
                Fight() ###############################
              
            case 4:
              # open cheats menu
              pass
        except IndexError:
          error = "Give a valid option"
        except ValueError:
          error = "Enter just the number"

            
def Fight():
  enemy = Enemy()
  while enemy.health > 0:
    enemy.enemy_turn(map,player)
    player.player_turn(enemy)
  
  print(f"{enemy.spirte_sheet[3]}\n\n{white}{enemy.name_display}\n\n Health = {enemy.health} / {enemy.max_health}\n Damage = {enemy.damage}")
  time.sleep(map.speed_modifier)
  print(f"\n You killed the {enemy.name}!")
  time.sleep(map.speed_modifier)
  print(f"The {enemy.name} dropped {yellow}{enemy.coins} coins! {white}")

  player.coins += enemy.coins
  time.sleep(map.speed_modifier + 0.5)
  os.system('cls||clear')
  


map = MapManager()
player = Player()

map.Start_Menu()
