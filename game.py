#initial procedural version test of a game in progress. 

#needs for game:

#need to expand to a class based version with a map and inventory system.
#need to add more commands and a way to win the game.
#need to add a way to lose the game.
#need to add a way to save the game.
#need to add a way to load the game.
#need to add a way to get help.
#need to add a way to get a list of commands.
#need to add a way to get a list of items.
#need to add a way to get a list of locations.
#need to add a way to get a list of characters.
#need to add a way to get a list of jobs.
#need to add a way to get a list of monsters.
#need to add a way to get a list of weapons.
#need to add a way to get a list of armor.
#need to add a way to get a list of spells.

#Dice rolling system

import dice
import sql
import sys

cursor = sql.get_cursor()
sql.select_using_like(cursor, text='Python')

#character creation

class character:
    hitpoints = 10
    def __init__(self, name, job):
        self.name = name
        self.job = job
    def printname(self):
        print(self.name)
    def printjob(self):
        print(self.job)

############ class version of character creation


name = input("Enter name:")
job = input("Enter job:")
profile = character(name, job)
profile.printname()
profile.printjob()

#class version of enemy creation


class enemy:
    def __init__(self, hp, description, attackkNum, defense, enemyname):
        self.hp = hp
        self.name = enemyname
        self.description = description
        self.attackNum = attackkNum
        self.defense = defense

    def attack(self):
        print(self.name  + " attacks!")
        newRoll = dice.D4()
        if newRoll == 1:
            print(self.name + " hits!")
    def defend(self):
        newRoll = dice.D4()
        if newRoll != 1:
            print("You miss!")

enemy1 = enemy(10, "Groat,a small rat", 1, 1, "Groat")

battleState = False

########### list version of character creation

#username = input("Enter username:")
#character = []
#print("Username is: " + username)
#job =input("Enter job:")
#character.append(job)

#location creation
room = "first room"

#game loop

#functions

def battle():
    global battleState
  
    newRoll = dice.D4()
    if newRoll == 1:
       battleState = True
       enemy1.attack()
       command = input("Enter command:")
       if command == "quit":
          exit(0)
       if command == "attack":
            newRoll = dice.D4()
            enemy1.hp = enemy1.hp - 5
            print("You hit" + enemy1.name + " for 5 damage!")
            if enemy1.hp <= 0:
                print(enemy1.name + " is deafeted! It runs away!")
                battleState = False
                first_level()
            else: 
                battle()

def first_level():
    global room
    room = "first room"
    battle()
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
        print("You got the cat! " + profile.name + " adds cat to inventory.")
       else:
        print("You failed to get the cat.Try again")
        first_level()
    if command == "quit":
        exit(0)
    else:
        print("I don't understand that.")
        first_level()

def second_level():
    global room
    command = input("Enter command:")
    if room == "second room" and command == "look room":
        print("You are in a cathedral. There is a path to the south.")
        second_level()
    if room == "second room" and command == "go south":
        print("You go south to the Village Center.")
        first_level()
    if command == "quit":
        exit(0)
    else:
        print("I don't understand that.")
        second_level()

 
#start game
first_level()