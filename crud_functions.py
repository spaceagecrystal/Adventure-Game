import sqlite3

# Connect to the SQLite database
def create_connection():
    conn = None
    try:
        conn = sqlite3.connect('gamedata.db')
        print("Connected to SQLite database")
    except sqlite3.Error as e:
        print(e)
    return conn

# Create a table
def create_table(conn):
    try:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL,
                email TEXT NOT NULL,
                name TEXT NOT NULL,
                namelast TEXT NOT NULL,
                job TEXT
            )
        ''')
        conn.commit()
        print("Table created successfully")
    except sqlite3.Error as e:
        print(e)

# Insert a new record
def create_record(conn, username, email, name, namelast, job):
    try:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (username, email, name, namelast, job) VALUES (?, ?, ?, ?, ?)",
                       (username, email, name, namelast, job))
        conn.commit()
        print("Record created successfully")
    except sqlite3.Error as e:
        print(e)

# Read all records
def read_records(conn):
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users")
        rows = cursor.fetchall()
        for row in rows:
            print(f"ID: {row[0]}, Username: {row[1]}, Email: {row[2]}, Name: {row[3]}, Last Name: {row[4]}, Job: {row[5]}")
    except sqlite3.Error as e:
        print(e)

# Update a record
def update_record(conn, record_id, username, email, name, namelast, job):
    try:
        cursor = conn.cursor()
        cursor.execute("UPDATE users SET username = ?, email = ?, name = ?, namelast = ?, job = ? WHERE id = ?",
                       (username, email, name, namelast, job, record_id))
        conn.commit()
        print("Record updated successfully")
    except sqlite3.Error as e:
        print(e)

# Delete a record
def delete_record(conn, record_id):
    try:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM users WHERE id = ?", (record_id,))
        conn.commit()
        print("Record deleted successfully")
    except sqlite3.Error as e:
        print(e)

# Main function to demonstrate the usage
def mainConnect():
    conn = create_connection()
    create_table(conn)

    choice = "1"

    if choice == '1':
            username = input("Enter username: ")
            email = input("Enter email: ")
            name = input("Enter name: ")
            namelast = input("Enter last name: ")
            job = input("Enter job: ")
            create_record(conn, username, email, name, namelast, job)
    elif choice == '2':
            read_records(conn)
    elif choice == '3':
            record_id = int(input("Enter ID of the record to update: "))
            username = input("Enter new username: ")
            email = input("Enter new email: ")
            name = input("Enter new name:")