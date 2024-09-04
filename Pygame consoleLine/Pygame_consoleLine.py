import random, time, sys, os

# colours #
yellow = "\033[0;33m"
green = "\033[0;32m"
white = "\033[0;97m"
blue = "\033[0;34m"
red = "\033[0;31m"
magenta = "\033[0;35m"
# colours #

# globals #
ehealth = 0
emaxhealth = 0
edamage = 0
ename = ""
enamedisplay = ""
edisplay = []
Cheats = False
potionSize = 0
phealth = 0
pdamdage = 0
pmaxhealth = 0
score = 0
coins = 0
difficulty = 0
difficultyModifier = 0
speedModifier = 0
BossModifier = 1
speed = 0
Quit = False
playerDisplay = ["", "", "", ""]
BoundGodDisplay = [
  "â–ˆâ–ˆâ–„   â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆ   â–„â–ˆ\n â–€â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–“â–ˆâ–“â–ˆâ–“â–ˆâ–“â–ˆâ–ˆâ–ˆâ–€ \n   â–ˆâ–ˆâ–“â–ˆâ–“â–ˆâ–“â–ˆâ–“â–ˆâ–“â–ˆâ–“â–ˆâ–ˆ  \n  â–ˆâ–ˆâ–“â–ˆâ–“â–ˆâ–“â–ˆâ–“â–ˆâ–“â–ˆâ–“â–ˆâ–“â–ˆâ–ˆâ–ˆ\n â–ˆâ–ˆâ–“â–ˆâ–“â–ˆâ–“â–ˆâ–“â–ˆâ–“â–ˆâ–“â–ˆâ–“â–ˆâ–“â–ˆâ–ˆ\n â–ˆâ–“â–ˆâ–“â–ˆâ–“â–ˆâ–“â–ˆâ–“â–ˆâ–“â–ˆâ–“â–ˆâ–“â–ˆâ–“â–ˆ\n â–ˆâ–ˆâ–“â–ˆâ–“â–ˆâ–“â–ˆâ–“â–ˆâ–“â–ˆâ–“â–ˆâ–“â–ˆâ–“â–ˆâ–ˆ\n  â–ˆâ–ˆâ–“â–ˆâ–“â–ˆâ–“â–ˆâ–“â–ˆâ–“â–ˆâ–“â–ˆâ–“â–ˆâ–ˆ \n   â–ˆâ–ˆâ–“â–ˆâ–“â–ˆâ–“â–ˆâ–“â–ˆâ–“â–ˆâ–“â–ˆâ–ˆ  \n â–ˆâ–ˆâ–€ â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–“â–ˆâ–“â–ˆâ–ˆâ–ˆâ–ˆâ–ˆ  \nâ–ˆâ–ˆ       â–ˆâ–ˆâ–ˆâ–ˆâ–ˆ   â–ˆâ–ˆ ",
  "â–ˆâ–ˆâ–„   â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆ   â–„â–ˆ\n â–€â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–“â€¢â–“â€¢â–“â€¢â–“â€¢â–ˆâ–ˆâ–€ \n   â–ˆâ–ˆâ–“â€¢â–“â€¢â–“â€¢â–“â€¢â–“â€¢â–“â–ˆâ–ˆ  \n  â–ˆâ–ˆâ–“â€¢â–“â€¢â–“â€¢â–“â€¢â–“â€¢â–“â€¢â–“â–ˆâ–ˆâ–ˆ\n â–ˆâ–ˆâ–“â€¢â–“â€¢â–“â€¢â–“â€¢â–“â€¢â–“â€¢â–“â€¢â–“â–ˆâ–ˆ\n â–ˆâ–“â€¢â–“â€¢â–“â€¢â–“â€¢â–“â€¢â–“â€¢â–“â€¢â–“â€¢â–“â–ˆ\n â–ˆâ–ˆâ–“â€¢â–“â€¢â–“â€¢â–“â€¢â–“â€¢â–“â€¢â–“â€¢â–“â–ˆâ–ˆ\n  â–ˆâ–ˆâ–“â€¢â–“â€¢â–“â€¢â–“â€¢â–“â€¢â–“â€¢â–“â–ˆâ–ˆ \n   â–ˆâ–ˆâ–“â€¢â–“â€¢â–“â€¢â–“â€¢â–“â€¢â–“â–ˆâ–ˆ  \n â–ˆâ–ˆâ–€ â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–“â€¢â–“â–ˆâ–ˆâ–ˆâ–ˆâ–ˆ  \nâ–ˆâ–ˆ       â–ˆâ–ˆâ–ˆâ–ˆâ–ˆ   â–ˆâ–ˆ ",
  "â–ˆâ–ˆâ–„   â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆ   â–„â–ˆ\n â–€â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–’â–“â–’â–“â–’â–“â–ˆâ–ˆâ–ˆâ–ˆâ–€ \n   â–ˆâ–ˆâ–’â–“â–’â–“â–’â–“â–’â–“â–’â–“â–’â–ˆâ–ˆ  \n  â–ˆâ–ˆâ–’â–“â–’â–“â–’â–“â–’â–“â–’â–“â–’â–“â–’â–ˆâ–ˆâ–ˆ\n â–ˆâ–ˆâ–’â–“â–’â–“â–’â–“â–’â–“â–’â–“â–’â–“â–’â–“â–’â–ˆâ–ˆ\n â–ˆâ–’â–“â–’â–“â–’â–“â–’â–“â–’â–“â–’â–“â–’â–“â–’â–“â–’â–ˆ\n â–ˆâ–ˆâ–’â–“â–’â–“â–’â–“â–’â–“â–’â–“â–’â–“â–’â–“â–’â–ˆâ–ˆ\n  â–ˆâ–ˆâ–’â–“â–’â–“â–’â–“â–’â–“â–’â–“â–’â–“â–’â–ˆâ–ˆ \n   â–ˆâ–ˆâ–’â–“â–’â–“â–’â–“â–’â–“â–’â–“â–’â–ˆâ–ˆ  \n â–ˆâ–ˆâ–€ â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–’â–“â–’â–ˆâ–ˆâ–ˆâ–ˆâ–ˆ  \nâ–ˆâ–ˆ       â–ˆâ–ˆâ–ˆâ–ˆâ–ˆ   â–ˆâ–ˆ ",
  "â–ˆâ–ˆâ–„   â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆ   â–„â–ˆ\n â–€â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–‘â–‘â–‘â–‘â–‘â–‘â–ˆâ–ˆâ–ˆâ–ˆâ–€ \n   â–ˆâ–ˆâ–‘â–‘â–‘â–‘â–‘â–‘â–‘â–‘â–‘â–‘â–‘â–ˆâ–ˆ  \n  â–ˆâ–ˆâ–‘â–‘â–‘â–‘â–‘â–‘â–‘â–‘â–‘â–‘â–‘â–‘â–‘â–ˆâ–ˆâ–ˆ\n â–ˆâ–ˆâ–‘â–‘â–‘â–‘â–‘â–‘â–‘â–‘â–‘â–‘â–‘â–‘â–‘â–‘â–‘â–ˆâ–ˆ\n â–ˆâ–‘â–‘â–‘â–‘â–‘â–‘â–‘â–‘â–‘â–‘â–‘â–‘â–‘â–‘â–‘â–‘â–‘â–ˆ\n â–ˆâ–ˆâ–‘â–‘â–‘â–‘â–‘â–‘â–‘â–‘â–‘â–‘â–‘â–‘â–‘â–‘â–‘â–ˆâ–ˆ\n  â–ˆâ–ˆâ–‘â–‘â–‘â–‘â–‘â–‘â–‘â–‘â–‘â–‘â–‘â–‘â–’â–ˆâ–ˆ \n   â–ˆâ–ˆâ–‘â–‘â–‘â–‘â–‘â–‘â–‘â–‘â–‘â–‘â–‘â–ˆâ–ˆ  \n â–ˆâ–ˆâ–€ â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–‘â–‘â–‘â–ˆâ–ˆâ–ˆâ–ˆâ–ˆ  \nâ–ˆâ–ˆ       â–ˆâ–ˆâ–ˆâ–ˆâ–ˆ   â–ˆâ–ˆ "
]
slimeDisplay = [
  "         â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆ\n      â–ˆâ–ˆâ–ˆâ–ˆâ–‘â–‘â–‘â–‘â–‘â–ˆâ–ˆâ–ˆ\n     â–ˆâ–ˆâ–‘â–‘â–‘â–‘â–‘â–‘â–‘â–‘â–‘â–ˆâ–ˆâ–ˆ\n    â–ˆâ–ˆâ–‘â–‘â–‘â–‘â–‘â–‘â–‘â–‘â–‘â–‘â–‘â–ˆâ–ˆ\n   â–ˆâ–ˆâ–‘â–‘â–‘â–ˆâ–‘â–‘â–‘â–‘â–ˆâ–‘â–‘â–‘â–ˆâ–ˆ\n   â–ˆâ–‘â–‘â–‘â–‘â–ˆâ–‘â–‘â–‘â–‘â–ˆâ–‘â–‘â–‘â–‘â–ˆ\n   â–ˆâ–‘â–‘â–‘â–‘â–‘â–‘â–‘â–‘â–‘â–‘â–‘â–‘â–‘â–‘â–ˆ\n   â–ˆâ–‘â–‘â–‘â–‘â–‘â–‘â–‘â–‘â–‘â–‘â–‘â–‘â–‘â–‘â–ˆâ–ˆ\n   â–ˆâ–‘â–‘â–‘â–‘â–‘â–‘â–‘â–‘â–‘â–‘â–‘â–‘â–‘â–‘â–ˆâ–ˆ\n   â–ˆâ–ˆâ–ˆâ–‘â–‘â–‘â–‘â–‘â–‘â–‘â–‘â–‘â–‘â–‘â–ˆâ–ˆ\n     â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆ",
  "         â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆ\n      â–ˆâ–ˆâ–ˆâ–ˆâ–‘â–‘â–‘â–‘â–‘â–ˆâ–ˆâ–ˆ\n     â–ˆâ–ˆâ–‘â–‘â–‘â–‘â–‘â–‘â–‘â–‘â–‘â–ˆâ–ˆâ–ˆ\n    â–ˆâ–ˆâ–‘â–‘â–ˆâ–‘â–‘â–‘â–‘â–‘â–ˆâ–‘â–‘â–ˆâ–ˆ\n   â–ˆâ–ˆâ–‘â–‘â–‘â–ˆâ–ˆâ–‘â–‘â–ˆâ–ˆâ–‘â–‘â–‘â–ˆâ–ˆ\n   â–ˆâ–‘â–‘â–‘â–‘â–‘â–ˆâ–‘â–‘â–ˆâ–‘â–‘â–‘â–‘â–‘â–ˆ\n   â–ˆâ–‘â–‘â–‘â–‘â–‘â–‘â–‘â–‘â–‘â–‘â–‘â–‘â–‘â–‘â–ˆ\n   â–ˆâ–‘â–‘â–‘â–‘â–‘â–‘â–‘â–‘â–‘â–‘â–‘â–‘â–‘â–‘â–ˆâ–ˆ\n   â–ˆâ–‘â–‘â–‘â–‘â–‘â–‘â–‘â–‘â–‘â–‘â–‘â–‘â–‘â–‘â–ˆâ–ˆ\n   â–ˆâ–ˆâ–ˆâ–‘â–‘â–‘â–‘â–‘â–‘â–‘â–‘â–‘â–‘â–‘â–ˆâ–ˆ\n     â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆ",
  "         â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆ\n      â–ˆâ–ˆâ–ˆâ–ˆâ–‘â–‘â–‘â–‘â–‘â–ˆâ–ˆâ–ˆ\n     â–ˆâ–ˆâ–‘â–‘â–‘â–‘â–‘â–‘â–‘â–‘â–‘â–ˆâ–ˆâ–ˆ\n    â–ˆâ–ˆâ–‘â–‘â–‘â–‘â–‘â–‘â–‘â–‘â–‘â–‘â–‘â–ˆâ–ˆ\n   â–ˆâ–ˆâ–‘â–‘â–‘â–ˆâ–ˆâ–‘â–‘â–‘â–ˆâ–ˆâ–‘â–‘â–ˆâ–ˆ\n   â–ˆâ–‘â–‘â–‘â–‘â–ˆâ–‘â–‘â–‘â–‘â–‘â–ˆâ–‘â–‘â–‘â–ˆ\n   â–ˆâ–‘â–‘â–‘â–‘â–’â–‘â–‘â–‘â–‘â–‘â–’â–‘â–‘â–‘â–ˆ\n   â–ˆâ–‘â–‘â–‘â–‘â–‘â–‘â–‘â–‘â–‘â–‘â–‘â–‘â–‘â–‘â–ˆâ–ˆ\n   â–ˆâ–‘â–‘â–‘â–‘â–‘â–‘â–‘â–‘â–‘â–‘â–‘â–‘â–‘â–‘â–ˆâ–ˆ\n   â–ˆâ–ˆâ–ˆâ–‘â–‘â–‘â–‘â–‘â–‘â–‘â–‘â–‘â–‘â–‘â–ˆâ–ˆ\n     â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆ",
  "         â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆ\n      â–ˆâ–ˆâ–ˆâ–ˆâ–‘â–‘â–‘â–‘â–‘â–ˆâ–ˆâ–ˆ\n     â–ˆâ–ˆâ–‘â–‘â–‘â–‘â–‘â–‘â–‘â–‘â–‘â–ˆâ–ˆâ–ˆ\n    â–ˆâ–ˆâ–‘â–‘â–‘â–‘â–‘â–‘â–‘â–‘â–‘â–‘â–‘â–ˆâ–ˆ\n   â–ˆâ–ˆâ–‘â–‘â–ˆâ–‘â–ˆâ–‘â–‘â–‘â–ˆâ–‘â–ˆâ–‘â–ˆâ–ˆ\n   â–ˆâ–‘â–‘â–‘â–‘â–ˆâ–‘â–‘â–‘â–‘â–‘â–ˆâ–‘â–‘â–‘â–ˆ\n   â–ˆâ–‘â–‘â–‘â–ˆâ–‘â–ˆâ–‘â–‘â–‘â–ˆâ–‘â–ˆâ–‘â–‘â–ˆ\n   â–ˆâ–‘â–‘â–‘â–‘â–‘â–‘â–‘â–‘â–‘â–‘â–‘â–‘â–‘â–‘â–ˆâ–ˆ\n   â–ˆâ–‘â–‘â–‘â–‘â–‘â–‘â–‘â–‘â–‘â–‘â–‘â–‘â–‘â–‘â–ˆâ–ˆ\n   â–ˆâ–ˆâ–ˆâ–‘â–‘â–‘â–‘â–‘â–‘â–‘â–‘â–‘â–‘â–‘â–ˆâ–ˆ\n     â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆ"
]
goblinDisplay = [
  "      â–ˆâ–ˆâ–ˆâ–ˆâ–ˆ        \n    â–ˆâ–ˆâ–ˆâ–‘â–‘â–‘â–‘â–ˆâ–ˆ     â–ˆ\nâ–ˆ  â–ˆâ–ˆâ–‘â–‘â–‘â–‘â–‘â–‘â–‘â–‘â–ˆ   â–ˆâ–ˆ\nâ–ˆâ–ˆ â–ˆâ–ˆâ–‘â–‘â–„â–‘â–„â–‘â–‘â–‘â–ˆ  â–ˆ  \n â–ˆ â–ˆâ–ˆâ–‘â–‘â–‘â–‘â–‘â–‘â–‘â–‘â–ˆâ–ˆâ–ˆâ–ˆ  \n â–ˆâ–ˆâ–ˆâ–ˆâ–‘â–‘â–‘â–‘â–‘â–‘â–‘â–‘â–ˆâ–ˆâ–ˆ   \n   â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆ   \n      â–ˆâ–ˆâ–ˆ  â–ˆâ–ˆ      \n     â–ˆâ–ˆâ–ˆ    â–ˆ      \n     â–ˆâ–ˆ     â–ˆâ–ˆ     \n     â–ˆ       â–ˆ     \n     â–ˆ             ",
  "       â–ˆâ–ˆâ–ˆâ–ˆâ–ˆ        \n     â–ˆâ–ˆâ–ˆâ–‘â–‘â–‘â–‘â–ˆâ–ˆ     â–ˆ\n â–ˆ  â–ˆâ–ˆâ–‘â–„â–‘â–‘â–‘â–„â–‘â–‘â–ˆ   â–ˆâ–ˆ\n â–ˆâ–ˆ â–ˆâ–ˆâ–‘â–‘â–ˆâ–‘â–ˆâ–‘â–‘â–‘â–ˆ  â–ˆ  \n  â–ˆ â–ˆâ–ˆâ–‘â–‘â–‘â–‘â–‘â–‘â–‘â–‘â–ˆâ–ˆâ–ˆâ–ˆ  \n  â–ˆâ–ˆâ–ˆâ–ˆâ–‘â–‘â–‘â–‘â–‘â–‘â–‘â–‘â–ˆâ–ˆâ–ˆ   \n    â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆ   \n       â–ˆâ–ˆâ–ˆ  â–ˆâ–ˆ      \n      â–ˆâ–ˆâ–ˆ    â–ˆ      \n      â–ˆâ–ˆ     â–ˆâ–ˆ     \n      â–ˆ       â–ˆ     \n      â–ˆ             ",
  "       â–ˆâ–ˆâ–ˆâ–ˆâ–ˆ        \n     â–ˆâ–ˆâ–ˆâ–‘â–‘â–‘â–‘â–ˆâ–ˆ     â–ˆ\nâ–ˆ  â–ˆâ–ˆâ–‘â–‘â–‘â–‘â–‘â–‘â–‘â–‘â–ˆ   â–ˆâ–ˆ\n â–ˆâ–ˆ â–ˆâ–ˆâ–‘â–‘â–„â–‘â–‘â–„â–‘â–‘â–ˆ  â–ˆ  \n  â–ˆ â–ˆâ–ˆâ–‘â–‘â–’â–‘â–‘â–’â–‘â–‘â–ˆâ–ˆâ–ˆâ–ˆ  \n  â–ˆâ–ˆâ–ˆâ–ˆâ–‘â–‘â–‘â–‘â–‘â–‘â–‘â–‘â–ˆâ–ˆâ–ˆ   \n    â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆ   \n       â–ˆâ–ˆâ–ˆ  â–ˆâ–ˆ      \n      â–ˆâ–ˆâ–ˆ    â–ˆ      \n      â–ˆâ–ˆ     â–ˆâ–ˆ     \n      â–ˆ       â–ˆ     \n      â–ˆ             ",
  "      â–ˆâ–ˆâ–ˆâ–ˆâ–ˆ        \n    â–ˆâ–ˆâ–‘â–‘â–‘â–‘â–‘â–ˆâ–ˆ     â–ˆ\nâ–ˆ  â–ˆâ–ˆâ–‘â–„â–‘â–„â–‘â–„â–‘â–„â–ˆ   â–ˆâ–ˆ\nâ–ˆâ–ˆ â–ˆâ–ˆâ–‘â–‘â–ˆâ–‘â–‘â–‘â–ˆâ–‘â–ˆ  â–ˆ  \n â–ˆ â–ˆâ–ˆâ–‘â–€â–’â–€â–‘â–€â–‘â–€â–ˆâ–ˆâ–ˆâ–ˆ  \n â–ˆâ–ˆâ–ˆâ–ˆâ–‘â–‘â–‘â–‘â–‘â–‘â–‘â–‘â–ˆâ–ˆâ–ˆ   \n   â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆ   \n      â–ˆâ–ˆâ–ˆ  â–ˆâ–ˆ      \n     â–ˆâ–ˆâ–ˆ    â–ˆ      \n     â–ˆâ–ˆ     â–ˆâ–ˆ     \n     â–ˆ       â–ˆ     \n     â–ˆ             "
]
mimicDisplay = [
  "â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆ  \nâ–ˆâ–ˆ    â—¾  â—¾   â–ˆâ–ˆ \n  â–ˆâ–ˆ          â–ˆâ–ˆ\n   â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆ \n  â–ˆâ–“â–“â–“â–“â–“â–“â–“â–“â–“â–“â–“â–ˆ \n â–ˆâ–“â–“â–“â–“â–“â–“â–“â–“â–“â–“â–“â–ˆâ–ˆ \n â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–’â–ˆ \n â–ˆâ–’â–’â–’â–’â–’â–’â–’â–’â–ˆâ–ˆâ–’â–’â–ˆ \n â–ˆâ–’â–’â–’â–’â–’â–’â–’â–’â–ˆâ–ˆâ–’â–ˆ  \n â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆ   ",
  "   â–€â–„      â–„â–€   \n    â–€â–ˆâ–„  â–„â–ˆâ–€    \nâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆ  \nâ–ˆâ–ˆ    â—¾  â—¾   â–ˆâ–ˆ \n  â–ˆâ–ˆ          â–ˆâ–ˆ\n   â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆ \n  â–ˆâ–“â–“â–“â–“â–“â–“â–“â–“â–“â–“â–“â–ˆ \n â–ˆâ–“â–“â–“â–“â–“â–“â–“â–“â–“â–“â–“â–ˆâ–ˆ \n â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–’â–ˆ \n â–ˆâ–’â–’â–’â–’â–’â–’â–’â–’â–ˆâ–ˆâ–’â–’â–ˆ \n â–ˆâ–’â–’â–’â–’â–’â–’â–’â–’â–ˆâ–ˆâ–’â–ˆ  \n â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆ   ",
  " â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆ  \n â–ˆâ–ˆ     â–„  â–„  â–ˆâ–ˆ \n   â–ˆâ–ˆ  â–€â–€  â–€â–€  â–ˆâ–ˆ\n    â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆ \n   â–ˆâ–“â–“â–“â–“â–“â–“â–“â–“â–“â–“â–“â–ˆ \n  â–ˆâ–“â–“â–“â–“â–“â–“â–“â–“â–“â–“â–“â–ˆâ–ˆ \n  â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–’â–ˆ \n  â–ˆâ–’â–’â–’â–’â–’â–’â–’â–’â–ˆâ–ˆâ–’â–’â–ˆ \n  â–ˆâ–’â–’â–’â–’â–’â–’â–’â–’â–ˆâ–ˆâ–’â–ˆ  \n  â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆ   ",
  "â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆ  \nâ–ˆâ–ˆ   â–„ â–„  â–„ â–„â–€â–ˆ \n  â–ˆâ–ˆ â–„â–€â–„  â–„â–€â–„ â–ˆâ–ˆ\n   â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆ \n  â–ˆâ–“â–“â–“â–“â–“â–“â–“â–“â–“â–“â–“â–ˆ \n â–ˆâ–“â–“â–“â–“â–“â–“â–“â–“â–“â–“â–“â–ˆâ–ˆ \n â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–’â–ˆ \n â–ˆâ–’â–’â–’â–’â–’â–’â–’â–’â–ˆâ–ˆâ–’â–’â–ˆ \n â–ˆâ–’â–’â–’â–’â–’â–’â–’â–’â–ˆâ–ˆâ–’â–ˆ  \n â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆ   "
]
bossDisplay = [
  "â–„              â–ˆ\nâ–ˆ             â–ˆâ–ˆ\nâ–ˆâ–ˆ     â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆ \n â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆ    â–ˆâ–ˆâ–ˆ \n  â–ˆâ–ˆ          â–ˆâ–ˆ\n  â–ˆ   â–ˆâ–ˆ  â–ˆâ–ˆ   â–ˆ\n  â–ˆâ–ˆ          â–ˆâ–ˆ\n   â–ˆâ–ˆ        â–ˆâ–ˆ \n    â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆ  \n        â–ˆâ–ˆ      \n      â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆ    \n    â–ˆâ–ˆ   â–ˆ  â–ˆâ–ˆ  \n   â–ˆâ–ˆ    â–ˆ   â–ˆâ–ˆ \n  â–ˆâ–ˆ     â–ˆ    â–ˆ \n  â–ˆ      â–ˆ    â–ˆ ",
  " â–„              â–ˆ\n â–ˆ             â–ˆâ–ˆ\n â–ˆâ–ˆ     â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆ \n  â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆ    â–ˆâ–ˆâ–ˆ \n   â–ˆâ–ˆ â–„     â–„  â–ˆâ–ˆ\n   â–ˆ  â–€â–ˆâ–„ â–„â–ˆâ–€   â–ˆ\n   â–ˆâ–ˆ          â–ˆâ–ˆ\n    â–ˆâ–ˆ        â–ˆâ–ˆ \n     â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆ  \n         â–ˆâ–ˆ      \n       â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆ    \n     â–ˆâ–ˆ   â–ˆ  â–ˆâ–ˆ  \n    â–ˆâ–ˆ    â–ˆ   â–ˆâ–ˆ \n   â–ˆâ–ˆ     â–ˆ    â–ˆ \n   â–ˆ      â–ˆ    â–ˆ ",
  "â–„              â–ˆ\nâ–ˆ             â–ˆâ–ˆ\nâ–ˆâ–ˆ     â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆ \n â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆ    â–ˆâ–ˆâ–ˆ \n  â–ˆâ–ˆ          â–ˆâ–ˆ\n  â–ˆ   â–„â–ˆ  â–ˆâ–„   â–ˆ\n  â–ˆâ–ˆ  â–€â–ˆ  â–ˆâ–€  â–ˆâ–ˆ\n   â–ˆâ–ˆ        â–ˆâ–ˆ \n    â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆ  \n        â–ˆâ–ˆ      \n      â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆ    \n    â–ˆâ–ˆ   â–ˆ  â–ˆâ–ˆ  \n   â–ˆâ–ˆ    â–ˆ   â–ˆâ–ˆ \n  â–ˆâ–ˆ     â–ˆ    â–ˆ \n  â–ˆ      â–ˆ    â–ˆ ",
  "â–„              â–ˆ\nâ–ˆ             â–ˆâ–ˆ\nâ–ˆâ–ˆ     â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆ \n â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆ    â–ˆâ–ˆâ–ˆ \n  â–ˆâ–ˆ â–„ â–„  â–„ â–„ â–ˆâ–ˆ\n  â–ˆ   â–ˆ    â–ˆ   â–ˆ\n  â–ˆâ–ˆ â–€ â–€  â–€ â–€ â–ˆâ–ˆ\n   â–ˆâ–ˆ        â–ˆâ–ˆ \n    â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆ  \n        â–ˆâ–ˆ      \n      â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆ    \n    â–ˆâ–ˆ   â–ˆ  â–ˆâ–ˆ  \n   â–ˆâ–ˆ    â–ˆ   â–ˆâ–ˆ \n  â–ˆâ–ˆ     â–ˆ    â–ˆ \n  â–ˆ      â–ˆ    â–ˆ "
]
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
  titleColour = green
  speed = 3

  while startgame != True:

    if speed == 4:
      speed = 0

    if speed == 0:
      speedColour = green + "fast" + white
      speedModifier = 1
    elif speed == 1:
      speedColour = yellow + "medium" + white
      speedModifier = 1.5
    elif speed == 2:
      speedColour = red + "slow" + white
      speedModifier = 2
    elif speed == 3:
      speedColour = blue + "V fast" + white
      speedModifier = 0.5

    if difficulty == 4:
      difficulty = 0

    if difficulty == 0:
      diffcolour = green + "easy" + white
      titleColour = green
      difficultyModifier = 1
    elif difficulty == 1:
      diffcolour = yellow + "medium" + white
      titleColour = yellow
      difficultyModifier = 1.5
    elif difficulty == 2:
      diffcolour = red + "hard" + white
      titleColour = red
      difficultyModifier = 2
    elif difficulty == 3:
      diffcolour = magenta + "baby" + white
      titleColour = magenta
      difficultyModifier = 0.5

    print(
      titleColour +
      "â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•—â–ˆâ–ˆâ•—â–‘â–‘â–ˆâ–ˆâ•—â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•—â€ƒâ€ƒâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•—â–‘â–ˆâ–ˆâ•—â–‘â–‘â–‘â–ˆâ–ˆâ•—â–ˆâ–ˆâ–ˆâ•—â–‘â–‘â–ˆâ–ˆâ•—â–‘â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•—â–‘â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•—â–‘â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•—â–‘â–ˆâ–ˆâ–ˆâ•—â–‘â–‘â–ˆâ–ˆâ•—\nâ•šâ•â•â–ˆâ–ˆâ•”â•â•â•â–ˆâ–ˆâ•‘â–‘â–‘â–ˆâ–ˆâ•‘â–ˆâ–ˆâ•”â•â•â•â•â•â€ƒâ€ƒâ–ˆâ–ˆâ•”â•â•â–ˆâ–ˆâ•—â–ˆâ–ˆâ•‘â–‘â–‘â–‘â–ˆâ–ˆâ•‘â–ˆâ–ˆâ–ˆâ–ˆâ•—â–‘â–ˆâ–ˆâ•‘â–ˆâ–ˆâ•”â•â•â•â•â•â–‘â–ˆâ–ˆâ•”â•â•â•â•â•â–ˆâ–ˆâ•”â•â•â–ˆâ–ˆâ•—â–ˆâ–ˆâ–ˆâ–ˆâ•—â–‘â–ˆâ–ˆâ•‘\nâ–‘â–‘â–‘â–ˆâ–ˆâ•‘â–‘â–‘â–‘â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•‘â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•—â–‘â–‘â€ƒâ€ƒâ–ˆâ–ˆâ•‘â–‘â–‘â–ˆâ–ˆâ•‘â–ˆâ–ˆâ•‘â–‘â–‘â–‘â–ˆâ–ˆâ•‘â–ˆâ–ˆâ•”â–ˆâ–ˆâ•—â–ˆâ–ˆâ•‘â–ˆâ–ˆâ•‘â–‘â–‘â–ˆâ–ˆâ•—â–‘â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•—â–‘â–‘â–ˆâ–ˆâ•‘â–‘â–‘â–ˆâ–ˆâ•‘â–ˆâ–ˆâ•”â–ˆâ–ˆâ•—â–ˆâ–ˆâ•‘\nâ–‘â–‘â–‘â–ˆâ–ˆâ•‘â–‘â–‘â–‘â–ˆâ–ˆâ•”â•â•â–ˆâ–ˆâ•‘â–ˆâ–ˆâ•”â•â•â•â–‘â–‘â€ƒâ€ƒâ–ˆâ–ˆâ•‘â–‘â–‘â–ˆâ–ˆâ•‘â–ˆâ–ˆâ•‘â–‘â–‘â–‘â–ˆâ–ˆâ•‘â–ˆâ–ˆâ•‘â•šâ–ˆâ–ˆâ–ˆâ–ˆâ•‘â–ˆâ–ˆâ•‘â–‘â–‘â•šâ–ˆâ–ˆâ•—â–ˆâ–ˆâ•”â•â•â•â–‘â–‘â–ˆâ–ˆâ•‘â–‘â–‘â–ˆâ–ˆâ•‘â–ˆâ–ˆâ•‘â•šâ–ˆâ–ˆâ–ˆâ–ˆâ•‘\nâ–‘â–‘â–‘â–ˆâ–ˆâ•‘â–‘â–‘â–‘â–ˆâ–ˆâ•‘â–‘â–‘â–ˆâ–ˆâ•‘â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•—â€ƒâ€ƒâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•”â•â•šâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•”â•â–ˆâ–ˆâ•‘â–‘â•šâ–ˆâ–ˆâ–ˆâ•‘â•šâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•”â•â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•—â•šâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•”â•â–ˆâ–ˆâ•‘â–‘â•šâ–ˆâ–ˆâ–ˆâ•‘\nâ–‘â–‘â–‘â•šâ•â•â–‘â–‘â–‘â•šâ•â•â–‘â–‘â•šâ•â•â•šâ•â•â•â•â•â•â•â€ƒâ€ƒâ•šâ•â•â•â•â•â•â–‘â–‘â•šâ•â•â•â•â•â•â–‘â•šâ•â•â–‘â–‘â•šâ•â•â•â–‘â•šâ•â•â•â•â•â•â–‘â•šâ•â•â•â•â•â•â•â–‘â•šâ•â•â•â•â•â–‘â•šâ•â•â–‘â–‘â•šâ•â•â•"
      + white)

    print(white + "\n1.) Difficulty = " + diffcolour + "\n2.) Game speed = " +
          speedColour + " \n3.) Start" + "\n4.) Cheats ")
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
      coins = 0

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
        os.system('clear')
        print(
          "â–‘â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•—â–‘â–ˆâ–ˆâ•—â–‘â–‘â–ˆâ–ˆâ•—â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•—â–‘â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•—â–‘â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•—â–‘â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•—\nâ–ˆâ–ˆâ•”â•â•â–ˆâ–ˆâ•—â–ˆâ–ˆâ•‘â–‘â–‘â–ˆâ–ˆâ•‘â–ˆâ–ˆâ•”â•â•â•â•â•â–ˆâ–ˆâ•”â•â•â–ˆâ–ˆâ•—â•šâ•â•â–ˆâ–ˆâ•”â•â•â•â–ˆâ–ˆâ•”â•â•â•â•â•\nâ–ˆâ–ˆâ•‘â–‘â–‘â•šâ•â•â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•‘â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•—â–‘â–‘â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•‘â–‘â–‘â–‘â–ˆâ–ˆâ•‘â–‘â–‘â–‘â•šâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•—â–‘\nâ–ˆâ–ˆâ•‘â–‘â–‘â–ˆâ–ˆâ•—â–ˆâ–ˆâ•”â•â•â–ˆâ–ˆâ•‘â–ˆâ–ˆâ•”â•â•â•â–‘â–‘â–ˆâ–ˆâ•”â•â•â–ˆâ–ˆâ•‘â–‘â–‘â–‘â–ˆâ–ˆâ•‘â–‘â–‘â–‘â–‘â•šâ•â•â•â–ˆâ–ˆâ•—\nâ•šâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•”â•â–ˆâ–ˆâ•‘â–‘â–‘â–ˆâ–ˆâ•‘â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•—â–ˆâ–ˆâ•‘â–‘â–‘â–ˆâ–ˆâ•‘â–‘â–‘â–‘â–ˆâ–ˆâ•‘â–‘â–‘â–‘â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•”â•\nâ–‘â•šâ•â•â•â•â•â–‘â•šâ•â•â–‘â–‘â•šâ•â•â•šâ•â•â•â•â•â•â•â•šâ•â•â–‘â–‘â•šâ•â•â–‘â–‘â–‘â•šâ•â•â–‘â–‘â–‘â•šâ•â•â•â•â•â•â–‘"
        )
        z = 0
        z = input("1.) Max Health = " + red + str(pmaxhealth) + white +
                  "\n2.) Health = " + red + str(phealth) + white +
                  "\n3.) Damage = " + blue + str(pdamage) + white +
                  "\n4.) Potion Size = " + green + str(potionSize) + white +
                  "\n5.) Coins = " + yellow + str(coins) + white +
                  "\n6.) Score = " + magenta + str(score) + white +
                  "\n7.) Done \n")
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
    os.system('clear')


def HC():
  global phealth
  global pmaxhealth

  if phealth <= 0:
    GameOver()
  if phealth > pmaxhealth:
    phealth = pmaxhealth


def Fight():
  global slimeDisplay
  global goblinDisplay
  global bossDisplay
  global mimicDisplay
  global BoundGodDisplay
  global edisplay
  global Cheats
  global isBoss
  global isMimic
  global isBoundGod
  global speedModifier
  global pdamage
  global score
  global phealth
  global difficultyModifier
  global potionSize
  global coins
  global difficulty
  global ename
  global enamedisplay
  global ehealth
  global emaxhealth
  global edamage
  ecoins = 0

  ecoins = ehealth

  while ehealth > 1:

    emove = random.randint(1, 4)

    # display manager #

    if difficulty == 0:
      eColour = green
    elif difficulty == 1:
      eColour = yellow
    elif difficulty == 2:
      eColour = red

    if emove != 4:
      eExpression = edisplay[0]
      if ehealth < emaxhealth * 0.5:
        eExpression = edisplay[1]
    if emove == 4:
      eExpression = edisplay[2]

    # display manager #

    print(enamedisplay + "\n\n" + eColour + eExpression + "\n" + white +
          " Health = " + str(ehealth) + "/" + str(emaxhealth) +
          "\n Damage = " + str(edamage))

    if emove != 4:
      print("\nThe " + ename + " Attcked! " + red + "(-" + str(edamage) +
            " HP)" + white)
      phealth = phealth - edamage
      HC()
    elif emove == 4:
      print("\nThe " + ename + " missed!")
    print("_________________________________________________\n")

    print(Cheats + name + white + " \n Health = " + red + str(phealth) +
          white + "/" + red + str(pmaxhealth) + white)
    ncols = 25
    print(f"\033[F\033[{ncols}G What do you do?")
    print(" Damage = " + blue + str(pdamage) + white)
    ncols = 26
    print(f"\033[F\033[{ncols}G 1.) Heal ")
    print(" Potion size = " + green + str(potionSize) + white)
    print(f"\033[F\033[{ncols}G 2.) Attack ")
    print(" Coins = " + yellow + str(coins) + white + "\n Score = " + magenta +
          str(score) + white + "\n")

    choice = input()
    if choice == "1":
      HealChance = random.randint(1, 4)
      if HealChance == 4:
        print("You failed to heal! ")
      else:
        phealth = phealth + potionSize
        print("You healed " + yellow + str(potionSize) + " HP" + white)
      HC()
    elif choice == "2":
      print("You attacked the " + ename + green + " (-" + str(pdamage) +
            " HP)" + white)
      ehealth = ehealth - pdamage
    time.sleep(speedModifier)

    if ehealth <= 0:
      isMimic = 1
      isBoss = 0
      isBoundGod = False
      os.system('clear')

      print(eColour + edisplay[3] + "\n\n" + white + enamedisplay +
            "\n\n Health = " + str(ehealth) + "/" + str(emaxhealth) +
            "\n Damage = " + str(edamage))
      time.sleep(speedModifier)
      print("\n You killed the " + ename + "!")
      time.sleep(speedModifier)
      print("The " + ename + " dropped " + yellow + str(ecoins) + " coins! " +
            white)

      coins = coins + ecoins
      time.sleep(speedModifier + 0.5)
    os.system('clear')


def pool():
  global speed
  global pdamage
  global phealth

  print("â–ˆâ–€â–ˆâ€ƒâ–ˆâ–€â–ˆâ€ƒâ–ˆâ–€â–ˆâ€ƒâ–ˆâ–‘â–‘\nâ–ˆâ–€â–€â€ƒâ–ˆâ–„â–ˆâ€ƒâ–ˆâ–„â–ˆâ€ƒâ–ˆâ–„â–„\n")
  print(
    "you see a glowing orb at the bottom of a lake?\nDo you swim to get it?\n1.) No\n2.) Yes"
  )
  choice = input()
  x = random.randint(1, 2)
  if choice == "2":
    if x == 1:
      print("You found a " + blue + " whetstone (+20 ATK)" + white)
      pdamage = pdamage + 20
      time.sleep(speedModifier)

    elif x == 2:
      print("It was a " + red + " trap (-15 HP) " + white)
      phealth = phealth - 15
      time.sleep(speedModifier)

      HC()
  os.system('cls||clear')


def Chest():
  global score
  global ename
  global edisplay
  global enamedisplay
  global ehealth
  global emaxhealth
  global edamage
  global score
  global potionSize

  isMimic = 1
  print("â–ˆâ–€â–€â€ƒâ–ˆâ–‘â–ˆâ€ƒâ–ˆâ–€â–€â€ƒâ–ˆâ–€â€ƒâ–€â–ˆâ–€\nâ–ˆâ–„â–„â€ƒâ–ˆâ–€â–ˆâ€ƒâ–ˆâ–ˆâ–„â€ƒâ–„â–ˆâ€ƒâ–‘â–ˆâ–‘\n")
  print("you see a strange chest ahead \n Do you open it?\n1.) No\n2.) Yes\n")
  x = input()
  if x == "1":
    print("You leave the chest alone... ")
    score = score - 1
  elif x == "2":
    isMimic = random.randint(1, 2)
    if isMimic == 1:
      print("You found a " + green + "potion upgrade! " + white)
      potionSize = potionSize + 5
      time.sleep(speedModifier + 0.5)
      os.system('clear')
    elif isMimic == 2:
      os.system('clear')

      print("It was a mimic! ")

      ename = green + "Mimic" + white
      edisplay = mimicDisplay
      enamedisplay = green + "â–ˆâ–€â–„â–€â–ˆâ€ƒâ–ˆâ€ƒâ–ˆâ–€â–„â–€â–ˆâ€ƒâ–ˆâ€ƒâ–ˆâ–€â–€\nâ–ˆâ–‘â–€â–‘â–ˆâ€ƒâ–ˆâ€ƒâ–ˆâ–‘â–€â–‘â–ˆâ€ƒâ–ˆâ€ƒâ–ˆâ–„â–„" + white
      emaxhealth = int(60 * difficultyModifier)
      ehealth = emaxhealth
      edamage = int(pdamage)
      if edamage > 30:
        edamage = 30

      Fight()

  os.system('clear')


def altar():
  global speedModifier
  global ename
  global edisplay
  global enamedisplay
  global ehealth
  global emaxhealth
  global edamage
  global score
  global speedModifier
  global pmaxhealth
  global phealth
  global pdamage
  global isBoss
  isBoss = 0

  x = ""
  print("â–„â–€â–ˆâ€ƒâ–ˆâ–‘â–‘â€ƒâ–€â–ˆâ–€â€ƒâ–„â–€â–ˆâ€ƒâ–ˆâ–€â–ˆ\nâ–ˆâ–€â–ˆâ€ƒâ–ˆâ–„â–„â€ƒâ–‘â–ˆâ–‘â€ƒâ–ˆâ–€â–ˆâ€ƒâ–ˆâ–€â–„\n")
  x = input(
    " You see an ominious altar...\n It glows with a powerfull energy \n\n  1.) Leave it alone \n  2.) Apparoch the altar "
  )
  if x == "2":
    y = random.randint(1, 4)
    if y == 1:
      print("\nThe altar glows and you feel stronger! " + red +
            "(+20 Max HP)" + white)
      pmaxhealth = pmaxhealth + 20
      time.sleep(speedModifier + 0.5)
      os.system('clear')
    else:
      ename = green + "The punisher" + white
      edisplay = bossDisplay
      enamedisplay = green + "â–€â–ˆâ–€â€ƒâ–ˆâ–‘â–ˆâ€ƒâ–ˆâ–€â–€â€ƒ â€ƒâ–ˆâ–€â–ˆâ€ƒâ–ˆâ–‘â–ˆâ€ƒâ–ˆâ–„â–‘â–ˆâ€ƒâ–ˆâ€ƒâ–ˆâ–€â€ƒâ–ˆâ–‘â–ˆâ€ƒâ–ˆâ–€â–€â€ƒâ–ˆâ–€â–ˆ\nâ–‘â–ˆâ–‘â€ƒâ–ˆâ–€â–ˆâ€ƒâ–ˆâ–ˆâ–„â€ƒ â€ƒâ–ˆâ–€â–€â€ƒâ–ˆâ–„â–ˆâ€ƒâ–ˆâ–‘â–€â–ˆâ€ƒâ–ˆâ€ƒâ–„â–ˆâ€ƒâ–ˆâ–€â–ˆâ€ƒâ–ˆâ–ˆâ–„â€ƒâ–ˆâ–€â–„" + white
      emaxhealth = int(250 * difficultyModifier)
      ehealth = emaxhealth
      edamage = 30
      Fight()
      print("The boss dropped a supply bag! ")

      print("You were " + red + "healed to full" + white +
            " and you found a " + blue + "whetstone! (+20 ATK)" + white)
      time.sleep(13 * speedModifier)
      os.system('clear')
      phealth = pmaxhealth
      pdamage = pdamage + 20
      time.sleep(3 * speedModifier)
  else:
    print("You leave the altar alone... ")
    time.sleep(2 * speedModifier)
    os.system('clear')
    score = score - 1


def FloorManager():
  global coins
  global name
  global score
  global Quit

  name = input("what is your name adventurer? ")
  os.system('clear')

  en = 0
  prevEn = 0

  while Quit != True:

    while prevEn == en:
      en = random.randint(1, 5)
    prevEn = en

    if score != 0:
      if score % 25 == 0 and score % 50 == 0:
        BoundGod()
      elif score % 25 == 0 and score % 50 != 0:
        CoinToss()

    if en == 1:
      DefaultEnemy()

    elif en == 2:
      pool()

    elif en == 3:
      Chest()

    elif en == 4:
      if coins > 100:
        Shop()
      else:
        score = score - 1

    elif en == 5:
      altar()

    score = score + 1


def GameOver():
  time.sleep(2)
  print("You died! ")
  os.system('clear')
  print("You died! ")

  DisplayStats()

  print("_______________________________\nScore = " + green + str(score) +
        white + "\n\n What now?\n1.) Play again\n2.) Quit")
  x = input()
  if x == "2":
    sys.exit("")
  else:
    os.system('clear')
    StartMenu()


def DisplayStats():
  global Cheats
  global name
  global phealth
  global pmaxhealth
  global pdamage
  global potionSize
  global coins

  print(Cheats + name + white + "\n Health = " + red + str(phealth) + white +
        "/" + red + str(pmaxhealth) + white + "\n Damage = " + blue +
        str(pdamage) + white + "\n Potion size = " + green + str(potionSize) +
        white + "\n Coins = " + yellow + str(coins) + white + "\n Score = " +
        magenta + str(score) + white + "\n")


def Shop():
  global pmaxhealth
  global pdamage
  global phealth
  global coins
  Exit = False
  cost = 0

  while Exit != True:
    print("â–ˆâ–€â€ƒâ–ˆâ–‘â–ˆâ€ƒâ–ˆâ–€â–ˆâ€ƒâ–ˆâ–€â–ˆ\nâ–„â–ˆâ€ƒâ–ˆâ–€â–ˆâ€ƒâ–ˆâ–„â–ˆâ€ƒâ–ˆâ–€â–€\n")
    x = ""
    print("You found a shop! ")
    print("You have " + yellow + str(coins) + " Coins\n" + white + "1.) " +
          red + "Max heal " + yellow + "(100 coins)\n" + white + "2.) " +
          blue + "Whetstone " + yellow + "(250 coins)\n" + white + "3.) " +
          red + "Max Health " + yellow + "(500 coins)\n" + white + "5.) Leave")
    print("\n")
    DisplayStats()
    x = input()
    os.system('clear')

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


def BoundGod():

  global BossModifier
  global phealth
  global pdamage
  global score
  global ename
  global edisplay
  global enamedisplay
  global ehealth
  global emaxhealth
  global edamage

  global difficultyModifier

  print("You hear terrible footsteps appraching from the shadows... ")
  time.sleep(1)
  print("The shadows mass together as one... ")

  ename = red + "The Bound God" + white
  edisplay = BoundGodDisplay
  emaxhealth = int(1000 * difficultyModifier * BossModifier)
  ehealth = int(emaxhealth)
  edamage = int(40 * difficultyModifier * BossModifier)

  Fight()

  BossModifier = BossModifier * 1.2


def CoinToss():
  global pmaxhealth
  global pdamage

  x = "1"
  print("â–ˆâ–€â–€â€ƒâ–ˆâ–€â–ˆâ€ƒâ–ˆâ€ƒâ–ˆâ–„â–‘â–ˆ\nâ–ˆâ–„â–„â€ƒâ–ˆâ–„â–ˆâ€ƒâ–ˆâ€ƒâ–ˆâ–‘â–€â–ˆ\n")
  x = input(
    "A stranger walks up to you with a coin \n'Do you want this high stake coin toss? '\nOne side has a "
    + red + "Ã·2" + white + "\nthe other has a " + blue + "X2" + white +
    " written on the back\n1.) Refuse 2.) Accept\n")

  if x == "1":
    print("The stranger looks at you dispointed and walks away. ")
  if x == "2":
    print("The coin flies high in the air...")
    time.sleep(3)

  y = random.randint(1, 2)
  if y == 1:
    print("It landed on the Ã·2! ")
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
    enamedisplay = green + "â–ˆâ–€â€ƒâ–ˆâ–‘â–‘â€ƒâ–ˆâ€ƒâ–ˆâ–€â–„â–€â–ˆâ€ƒâ–ˆâ–€â–€\nâ–„â–ˆâ€ƒâ–ˆâ–„â–„â€ƒâ–ˆâ€ƒâ–ˆâ–‘â–€â–‘â–ˆâ€ƒâ–ˆâ–ˆâ–„" + white
    emaxhealth = int(50 * difficultyModifier)
    ehealth = int(emaxhealth)
    edamage = 5
  elif enemy == 1:
    ename = green + "Goblin" + white
    edisplay = goblinDisplay
    enamedisplay = green + "â–ˆâ–€â–€â€ƒâ–ˆâ–€â–ˆâ€ƒâ–ˆâ–„â–„â€ƒâ–ˆâ–‘â–‘â€ƒâ–ˆâ€ƒâ–ˆâ–„â–‘â–ˆ\nâ–ˆâ–„â–ˆâ€ƒâ–ˆâ–„â–ˆâ€ƒâ–ˆâ–„â–ˆâ€ƒâ–ˆâ–„â–„â€ƒâ–ˆâ€ƒâ–ˆâ–‘â–€â–ˆ" + white
    emaxhealth = int(70 * difficultyModifier)
    ehealth = int(emaxhealth)
    edamage = 15

  Fight()


def ChickenSwarm():
  print("A swarm of chicked approches! ")


StartMenu()