import dice
import sys
from crud_functions import mainConnect, create_connection, create_record

# Random Enemy Generator

import random

monster1 = {
    "enemyID": 1,
    "name": "Silver Armored Albolor",
    "hp": 5,
    "description": "A mighty creature with scales and the ability to bore with didactic lectures.",
}

monster2 = {
    "enemyID": 2,
    "name": "Golowrath",
    "hp": 5,
    "description": "A fearsome beast with the ability to fly and breathe ice.",
}
monster3 = {
    "enemyID": 3,
    "name": "Hydra of the Deep",
    "hp": 5,
    "description": "A seductive creature that is made of slime and has many heads.",
}

monster4 = {
    "enemyID": 4,
    "name": "Demon of the Ghost of a Lost Cat",
    "hp": 5,
    "description": "Legend has it that every cat that is lost becomes a demon for all eternity.",
}

monsters = [monster1, monster2, monster3, monster4]

for monster in monsters:
    print(monster)
    print("-----------------------")


def randomEnemy():
    newRoll = random.randint(0, len(monsters) - 1)
    print("You encounter a " + monsters[newRoll]["name"] + ". It disdainfully attacks you!")


# Character creation
atFirst = True


class character:
    hitpoints = 10

    def __init__(self, name, job):
        self.name = name
        self.job = job

    def printname(self):
        print(self.name)

    def printjob(self):
        print(self.job)


# Class version of enemy creation
class enemy:
    def __init__(self, hp, description, attackkNum, defense, enemyname):
        self.hp = hp
        self.name = enemyname
        self.description = description
        self.attackNum = attackkNum
        self.defense = defense

    def attack(self):
        print(self.name + " attacks!")
        newRoll = dice.D4()
        if newRoll == 1:
            print(self.name + " hits!")

    def defend(self):
        newRoll = dice.D4()
        if newRoll != 1:
            print("You miss!")


print(enemy)

battleState = False

# Location creation
room = "first room"


# Game loop
def battleTest():
    newRoll = dice.D4()
    if newRoll == 1:
        battle()
    else:
        print("The air is gentle and the sun is shining. You are not in battle.")


def battle():
    global battleState
    global atFirst

    if atFirst == True:
        newRoll = random.randint(0, len(monsters) - 1)
        monsterName = monsters[newRoll]["name"]
        print("You encounter a " + monsterName + ".")
        battleState = True
        print("Oh my god what now, you think. You are in battle again!")

    if battleState == True:
        command = input("You are in battle! Enter attack or defend:")

        if command == "defend":
            print("You defend!")
            battle()

        if command == "quit":
            exit(0)

        if command == "attack":
            newRoll = dice.D4()
            monster = monsters[newRoll]
            monster["hp"] -= 5
            print("You hit " + monsterName + " for 5 damage!")
            print(monsterName+ " has " + str(monster["hp"]) + " hitpoints left!")

            if monster["hp"] <= 0:
                print(monsterName + " is defeated! It runs away!")
                battleState = False
                atFirst = True
            else:
                atFirst = False
                battle()
    else:
        first_level()


# First level
def first_level():
    global room
    room = "first room"
    battleTest()
    command = input("Enter command:")
    if room == "first room" and command == "look room":
        print("You are in a garden village, the air is fresh and the sun is shining.")
        print("There is a well in the middle of the village. There is a path to the north.")
        first_level()
    if room == "first room" and command == "go north":
        print("You go north to the Cathedral.")
        room = "second room"
        second_level()
    if room == "first room" and command == "look well":
        print("You look down the well and see a lost cat.")
        first_level()
    if command == "get cat":
        newRoll = dice.D4()
        if newRoll == 1:
            print("You got the cat! You add cat to inventory.")
            print("The cat purrs happily. You return the cat to its owner. The owner gives you a reward.")
            print("You gain 10 gold!")
            first_level()
        else:
            print("You failed to get the cat. Try again")
            print("This is difficult! But be persistent!")
            first_level()

    # Main controls
    if command == "help":
        print(
            "Commands are: look room, go north, go south, go east, go west, get item, use item, attack, defend, quit, help"
        )
        first_level()
    if command == "quit":
        exit(0)
    else:
        print("I don't understand that.")
        first_level()


# Second level
def second_level():
    global room
    command = input("Enter command:")
    if room == "second room" and command == "look room":
        print("You are outside a cathedral. There is a path to the south. Something seems strange, as if the wind itself cried for something lost.")
        second_level()
    if room == "second room" and command == "go south":
        print("You go south to the Village Center.")
        first_level()
    if command == "quit":
        exit(0)
    else:
        print("I don't understand that.")
        second_level()

    # Main controls
    if command == "help":
        print(
            "Commands are: look room, go north, go south, go east, go west, get item, use item, attack, defend, quit, help"
        )
        second_level()
    if command == "quit":
        exit(0)


# Start game
def start_game():
    conn = create_connection()
    conn2 = mainConnect()
    print("Welcome to the game!")
    print(
        "In the land of Ravinia, you find yourself on the outskirts of the village, which sang with the open folds of spore flowers. As a fairy warrior, you are returning after a long journey, and you have heard that still a few Groats, ancient"
    )
    print(
        "from beyond the hills. You walk through the gates and into the garden city, the air is cool and peaceful."
    )
    print("Type help for a list of commands.")
    first_level()


start_game()