#initial procedural version test of a game in progress. 

#needs for game: See Jira board

import dice
import sys
from crud_functions import mainConnect, create_connection, create_record


#cursor = sql.get_cursor()
#sql.select_using_like(cursor, text='Python')

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

def battleTest():
    newRoll = dice.D4()
    if newRoll == 1:
        battle()
    else:
        print("The air is gentle and the sun is shining. You are not in battle.")

def battle():
    
    global battleState

    newRoll = dice.D4()

    if newRoll == 2 and battleState != True:

        battleState = True
        enemy1.attack()
        command = input("You are in battle! Enter command:")
       
        if command == "defend":
           
           print("You defend!")
           battle()

        if command == "quit":
            exit(0)

        if command == "attack":

            newRoll = dice.D4()
            enemy1.hp = enemy1.hp - 5
            print("You hit" + enemy1.name + " for 5 damage!")
            print(enemy1.name + " has " + str(enemy1.hp) + " hitpoints left!")

            if enemy1.hp <= 5:
                print(enemy1.name + " is defeated! It runs away!")
                battleState = False
            else: 
                battle()
    else:
            first_level()

#first level

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
        print("You failed to get the cat.Try again")
        print("This is difficult! But be perisistent!")
        first_level()

    ## maincontrols

    if command == "help":
        print("Commands are: look room, go north, go south, go east, go west, get item, use item, attack, defend, quit, help")
        first_level()
    if command == "quit":
        exit(0)
    else:
        print("I don't understand that.")
        first_level()

#second level

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

    ## maincontrols

    if command == "help":
        print("Commands are: look room, go north, go south, go east, go west, get item, use item, attack, defend, quit, help")
        second_level()
    if command == "quit":
        exit(0)

#start game

def start_game():  

    conn = create_connection()
    conn2 = mainConnect()
    print("Welcome to the game!")
    print("In the land of Ravinia, you find yourself on the outskirts of the village, which sang with the openfolds of sporefloweres. As a fairy warrior, you are returning after a long journey, and you have heard that still a few Groats, ancient")
    print("from beyond the hills. You walk thorugh the gates and into the garden city, the air is cool and peaceful.")
    print("Type help for a list of commands.")

    first_level()


start_game()