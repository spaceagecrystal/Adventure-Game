import sqlite3

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

display_inventory()
