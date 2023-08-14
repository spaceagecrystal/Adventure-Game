import dice
import sys
import random
import sqlite3

#####: This is a work in progress. I am currently working on the database and inventory system.#####
##### Add ability to look at monsters #####
### reset hp after battle ###

global room

# Connect to the SQLite database
def create_connection():
    conn = None
    try:
        conn = sqlite3.connect("gamedata.db")
    except sqlite3.Error as e:
        print(e)
    return conn


# Create a table
def create_table(conn):
    try:
        cursor = conn.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL,
                job TEXT
            )
        """
        )
        conn.commit()
        print("Table created successfully")

    except sqlite3.Error as e:
        print(e)


# Insert a new record
def create_record(conn, table_name, **kwargs):
    cursor = conn.cursor()

    # Generate the SQL statement
    columns = ", ".join(kwargs.keys())
    placeholders = ":" + ", :".join(kwargs.keys())
    sql = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
    # Execute the query with the provided values
    cursor.execute(sql, kwargs)
    # Commit the changes
    conn.commit()

    # Close the cursor
    cursor.close()

# Update a record
def update_record(conn, table_name, record_id, **kwargs):
    cursor = conn.cursor()

    # Generate the SQL statement
    set_clause = ", ".join([f"{column} = :{column}" for column in kwargs.keys()])
    sql = f"UPDATE {table_name} SET {set_clause} WHERE id = :id"
    kwargs["id"] = record_id

    # Execute the query with the provided values
    cursor.execute(sql, kwargs)

    # Commit the changes
    conn.commit()

    # Close the cursor
    cursor.close()

# Main function to demonstrate the usage
def mainConnect():
    conn = create_connection()
    create_table(conn)

    choice = "1"

    if choice == "1":
        username = input("Enter username: ")
        job = input("Are you a Warrior, Mage, Healer, or Palladin:  ")
        create_record(
            conn,
            "users",
            username=username,
            job=job,
        )

    return conn


# Inventory functions
def display_inventory():
    # Connect to the database
    conn = sqlite3.connect("gamedata.db")
    cursor = conn.cursor()

    # Execute the query
    cursor.execute("SELECT * FROM Inventory WHERE in_inventory >= 1")

    # Fetch all the rows
    rows = cursor.fetchall()

    # Iterate through the rows and print the desired columns
    for row in rows:
        item_id, name, attack_level, item_type, description, in_inventory = row
        print(f"Item ID: {item_id}")
        print(f"Name: {name}")
        print(f"Attack Level: {attack_level}")
        print(f"Type: {item_type}")
        print(f"Description: {description}")
        print(f"In Inventory: {in_inventory}")
        print("-----------------------")

    # Close the cursor and connection
    cursor.close()
    conn.close()


# Example usage
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


def randomEnemy():
    if monsters:
        newRoll = random.randint(0, len(monsters) - 1)
        return newRoll
    else:
        print("No monsters available.")
        return None


# Character creation
atFirst = True


class Character:
    hitpoints = 10

    def __init__(self, name, job):
        self.name = name
        self.job = job

    def printname(self):
        print(self.name)

    def printjob(self):
        print(self.job)


# Class version of enemy creation
class Enemy:
    def __init__(self, hp, description, attackNum, defense, enemyname):
        self.hp = hp
        self.name = enemyname
        self.description = description
        self.attackNum = attackNum
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
    global monsters  # Add this line to access the monsters list

    if atFirst:
        newRoll = randomEnemy()
        monster = monsters[newRoll]
        monsterName = monster["name"]
        print("You are attacked by a " + monsterName + ".")
        battleState = True
        print("Oh my god what now, you think. You are in battle again!")

    if battleState:
        command = input("You are in battle! Enter attack or defend:")

        if command == "defend":
            print("You defend!")
            battle()

        elif command == "quit":
            sys.exit(0)

        elif command == "attack":
            monsterName = monster["name"]
            monster["hp"] -= 5
            print("You hit " + monsterName + " for 5 damage!")
            print(monsterName + " has " + str(monster["hp"]) + " hitpoints left!")

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
        print(
            "There is a well in the middle of the village. There is a path to the north."
        )
        first_level()

    elif room == "first room" and command == "go north":
        print("You go north to the Cathedral.")
        room = "second room"
        second_level()

    elif room == "first room" and command == "look well":
        print("You look down the well and see a lost cat.")
        first_level()

    if command == "get cat":
        newRoll = dice.D4()
        if newRoll == 1:
            print("You got the cat! You add cat to inventory.")
            print(
                "The cat purrs happily. You return the cat to its owner. The owner gives you a reward."
            )
            print("You gain 10 gold!")

            # Update the item ID in the database
            ##item_id_to_update = 1  # ID of the cat item in the Inventory table
            ##update_record(conn, "Inventory", item_id_to_update, in_inventory=1)

            first_level()
        else:
            print("You failed to get the cat. Try again")
            print("This is difficult! But be persistent!")
            first_level()

    elif command == "inventory":
        display_inventory()
        first_level()

    elif command == "help":
        print(
            "Commands are: look room, go north, go south, go east, go west, get item, use item, attack, defend, quit, help"
        )
        first_level()

    elif command == "quit":
        sys.exit(0)

    elif room == "first room" and command == "save game":
        print("You save the game.")
        saveGame("town")

    else:
        print("I don't understand that.")
        first_level()


# Second level
def second_level():
    room = "second room"
    command = input("Enter command:")

    if room == "second room" and command == "look room":
        print(
            "You are outside a cathedral. There is a path to the south and east. Something seems strange, as if the wind itself cried for something lost."
        )
        second_level()

    elif room == "second room" and command == "go south":
        print("You go south to the Village Center.")
        first_level()
    
    elif room == "second room" and command == "go east":
        print("You go east to the base of a mountain")
        room = "third room"
        third_level()
    
    elif room == "second room" and command == "save game":
        print("You save the game.")
        saveGame("cathedral")
        second_level()

    elif command == "quit":
        sys.exit(0)

    else:
        print("I'm sorry, I don't understand that.")
        second_level()

    # Main controls
    if command == "help":
        print(
            "Commands are: look room, go north, go south, go east, go west, get item, use item, attack, defend, rest, quit, help"
        )
        second_level()
    elif command == "quit":
        sys.exit(0)

# Third Level
def third_level():
    room = "third room"
    command = input("Enter command:")

    if room == "third room" and command == "look room":
        print(
            "At the base of a mountainside, a small river flows throughout an ancient castle ruin."
        )
        third_level()
    
    elif room == "third room" and command == "go west":
        print("You go west to the cathedral.")        
        room = "second room"
        second_level()

    elif room == "third room" and command == "look ruins":
        print("You see something bright and shimmering ammidst the broken forms.")
        third_level()

    elif room == "third room" and command == "save game":
        print("You save the game.")
        saveGame("mountain")
        third_level()

    elif command == "quit":
        sys.exit(0)

    else:
        print("I'm sorry, I don't understand that.")
        third_level()

    # Main controls
    if command == "help":
        print(
            "Commands are: look room, go north, go south, go east, go west, get item, use item, attack, defend, rest, quit, help"
        )
        third_level()
    
    elif command == "quit":
        sys.exit(0)


# Start game
def start_game():
    conn = mainConnect()
    print("Welcome to the Ravinia!")
    print(
        "In the land of Ravinia, you find yourself on the outskirts of the village, which sang with the open folds of spore flowers. As a fairy warrior, you are returning after a long journey, and you have heard that still a few Groats, ancient"
    )
    print(
        "from beyond the hills. You walk through the gates and into the garden city, the air is cool and peaceful."
    )
    print("Type help for a list of commands.")

def load_game():
    connection = sqlite3.connect('gamedata.db')
    cursor = connection.cursor()
    print("Table created successfully")
    cursor.execute('SELECT location FROM savepoint ORDER BY number_save DESC LIMIT 1')
    location = cursor.fetchone()
    if location:
        print("Looks like the last place you were was " + location[0] + " taking you there now.")

        if location[0] == "cathedral":
            print("you go to the cathedral.")
            second_level()

        elif location[0] == "mountain":
            print("you go to the mountain.")

            room = "third room"

            third_level()

        else:
            print("you go to the city center.")

            first_level()

    connection.close()

def saveGame(saveGameLoc):
        conn = create_connection()
        cursor = conn.cursor()

        cursor.execute('SELECT number_save FROM savepoint ORDER BY number_save DESC LIMIT 1')
        lastSaved  = cursor.fetchone()
        create_record(
            conn, "savepoint", location=saveGameLoc, quest="The shiny object", number_save=lastSaved[0]+1
        )

start_game()
load_game()
conn = create_connection()

cursor = conn.cursor()
cursor.execute('''
            CREATE TABLE IF NOT EXISTS savepoint (
                location TEXT,
                quest TEXT,
                number_save INTEGER)
        ''')