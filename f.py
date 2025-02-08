import sqlite3

# Connect to the SQLite database (it will be created if it doesn't exist)
conn = sqlite3.connect('food_requests.db')
c = conn.cursor()

# Create the table if it doesn't exist
c.execute('''
    CREATE TABLE IF NOT EXISTS food_requests (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        day TEXT,
        breakfast INTEGER,
        lunch INTEGER,
        dinner INTEGER
    )
''')

# Commit and close the connection
conn.commit()
conn.close()
