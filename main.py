import time

def mainmenu():
    print("""

Welcome to the narrow.one Data Hub!

[1] - Calculate k/d
[2] - Calculate k/d ratio
[3] - Search for players' information
[4] - Help Menu

""")
    while True:
        userinput = input("> ")
        if userinput == "1":
            calculatekd()
        elif userinput == "2":
            calculatekdratio()
        elif userinput == "3":
            playerinfosearch()
        elif userinput == "4":
            helpmenu()
        else:
            print("Select a valid option.")


def calculatekd():
    value1 = input("Enter the number of kills: ")
    value2 = input("Enter the number of deaths: ")
    try:
        print(f"Your k/d is: {int(value1) / int(value2)}")
        time.sleep(3)
        mainmenu()
    except ValueError:
        print("Only numbers are accepted! Do not enter letters and/or characters!")
        calculatekd()



def calculatekdratio():
    num1 = input("Enter the number of kills: ")
    num2 = input("Enter the number of deaths: ")
    try:
        print(f"For every 1 kill you got, you died {int(num2) / int(num1)} times. Ratio -> 1:{int(num2) / int(num1)}")
        time.sleep(3)
        mainmenu()
    except ValueError:
        print("Only numbers are accepted! Do not enter letters and/or characters!")
        calculatekdratio()


def playerinfosearch():
    # database
    players = {

'bluey': 
"""Skill: 60
Discord: bluey#6431
Mouse Sensitivity: 1.2
fov: 140""",

'bye': 
"""Skill: 306
Discord: bye#5775""",

'skyzess': 
"""Skill: 186
Discord: skyzess#9196""",

'Aussua': 
"""Skill: 436.6
Discord: Aussua#3216""",

'The King': 
"""Skill: 307.2
Discord: The King#1814""",

'HerrBret': 
"""Skill: 472
Discord: HerrBret#0438""",

'N1 | Blackmill': 
"""Skill: 500+
Discord: SNADOWBLACKMILL#1066
YouTube: https://www.youtube.com/@snadowblackmill/videos""",

'Paradonium': 
"""Skill: 172
Discord: Paradonium#5119""",

'Hot Dog Man': 
"""Skill: 94.35
Discord: Hot dog man#6578""",

'Infurness': 
"""Skill: 2085
Discord: BowtoDaKing#6689""",


}
    player = input('Enter a player username to obtain data: ')
    if player in players:
        print(players[player])
        time.sleep(3)
        mainmenu()
    else:
        print('Player not found! Try again. You can submit your own data here: ')
        playerinfosearch()



def helpmenu():
    print("""
    
Welcome to the help menu!

*Calculate k/d
This module will calculate your k/d. Enter your number of kills first, then your number of deaths.
The program will print you your k/d.
If your k/d is less that 1, that means you had more deaths than kills.
Higher the k/d, better your score is.

*Calculate k/d ratio
This module will print your number of deaths per 1 kill.

*Search for players' information

Type "quit" so quit the help menu.

""")
    userinput = input("> ")
    if userinput.lower() == "quit":
        mainmenu()
    else:
        print("Please select a valid option.")
        time.sleep(2)
        helpmenu()


mainmenu()