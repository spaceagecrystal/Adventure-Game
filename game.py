#initial procedural version test of a game in progress. 
#need to expand to a class based version with a map and inventory system.
#need to add more commands and a way to win the game.
#need to add a way to lose the game.
#need to add a way to quit the game.
#need to add a way to save the game.
#need to add a way to load the game.
#need to add a way to restart the game.
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


username = input("Enter username:")

character = []

print("Username is: " + username)

character.append(username)

job =input("Enter job:")

character.append(job)

print("Job is: " + job)

print(character)

command = input("Enter command:")

if command == "look room":
    print("You are in a garden village, the air is fresh and the sun is shining.")
    print("There is a well in the middle of the village. There is a path to the north.")
else:
    print("I don't understand that.")

command = input("Enter command:")

if command == "look well":
    print("You look down the well and see a lost cat.")
else:
    print("I don't understand that.")   
   
command = input("What do you do:")
    
if command == "get cat":
    print("You got the cat! " + username + " wins!")
else:
    print("I don't understand that.")
