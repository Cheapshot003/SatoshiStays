import sqlite3


def create_table():
  con = sqlite3.connect('satDB.db')
  cur = con.cursor()
  # Corrected CREATE TABLE statement with a closing parenthesis
  cur.execute('''
  CREATE TABLE IF NOT EXISTS listings(
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      name TEXT,
      location TEXT,
      price TEXT)
  ''')
  insert_dummy_data()
  con.commit()
  con.close()


def insert_dummy_data():
  # Connect to the SQLite database
  con = sqlite3.connect('satDB.db')
  cur = con.cursor()

  # Dummy data to insert
  dummy_data = [('Lovely Cottage', '40.7128,-74.0060', '200'),
                ('Beachside House', '34.0522,-118.2437', '350'),
                ('Mountain Cabin', '39.7392,-104.9903', '150')]

  # Insert each listing into the listings table
  cur.executemany(
      '''
  INSERT INTO listings (name, location, price)
  VALUES (?, ?, ?)
  ''', dummy_data)

  # Commit the transaction and close the connection
  con.commit()
  con.close()


def getListings(name):
  listings = []
  con = sqlite3.connect('satDB.db')
  con.row_factory = sqlite3.Row  # This allows access to data by column name
  cur = con.cursor()

  # Use parameterized queries to prevent SQL injection
  cur.execute("SELECT * FROM listings WHERE name LIKE ?", ('%' + name + '%', ))
  rows = cur.fetchall()

  for row in rows:
    listings.append({
        'id': row['id'],
        'name': row['name'],
        'location': row['location'],
        'price': row['price']
    })

  con.close()
  return listings
