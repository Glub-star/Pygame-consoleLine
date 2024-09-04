  x = "1"
  print("█▀▀ █▀█ █ █▄░█\n█▄▄ █▄█ █ █░▀█\n")
  x = input(
    "A stranger walks up to you with a coin \n'Do you want this high stake coin toss? '\nOne side has a "
    + red + "÷2" + white + "\nthe other has a " + blue + "X2" + white +
    " written on the back\n1.) Refuse 2.) Accept\n")

  if x == "1":
    print("The stranger looks at you dispointed and walks away. ")
  if x == "2":
    print("The coin flies high in the air...")
    time.sleep(3)

  y = random.randint(1, 2)
  if y == 1:
    print("It landed on the ÷2! ")
    print("Your " + red + "max health" + white + " and" + blue + "damage " +
          white + "were " + red + "halved! ")
    pmaxhealth = int(pmaxhealth / 2)
    pdamage = int(pdamage / 2)
    HC()
  if y == 2:
    print("It landed on the X2 ! ")
    print("Your " + red + "max health " + white + "and " + blue + " damage" +
          white + " were " + magenta + "doubled! " + white)
    pmaxhealth = int(pmaxhealth * 2)
    pdamage = int(pdamage * 2)
    HC()


def DefaultEnemy():
  global score
  global ename
  global edisplay
  global enamedisplay
  global ehealth
  global emaxhealth
  global edamage

  subtract = 0

  if score >= 100:
    subtract = 99
  elif score <= 0:
    subtract = 1
  else:
    subtract = score

  maxVal = 100 - subtract

  goblinChance = random.randint(1, maxVal)

  if goblinChance == 1:
    enemy = 1
  else:
    enemy = 0

  if enemy == 0:
    ename = green + "Slime" + white
    edisplay = slimeDisplay
    enamedisplay = green + "█▀ █░░ █ █▀▄▀█ █▀▀\n▄█ █▄▄ █ █░▀░█ ██▄" + white
    emaxhealth = int(50 * difficultyModifier)
    ehealth = int(emaxhealth)
    edamage = 5
  elif enemy == 1:
    ename = green + "Goblin" + white
    edisplay = goblinDisplay
    enamedisplay = green + "█▀▀ █▀█ █▄▄ █░░ █ █▄░█\n█▄█ █▄█ █▄█ █▄▄ █ █░▀█" + white
    emaxhealth = int(70 * difficultyModifier)
    ehealth = int(emaxhealth)
    edamage = 15

  Fight()


def ChickenSwarm():
  print("A swarm of chicked approches! ")


StartMenu()
