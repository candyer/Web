import sqlite3

conn = sqlite3.connect('test.db')
c = conn.cursor()

def create_table():
	c.execute('CREATE TABLE IF NOT EXISTS books(id INTEGER PRIMARY KEY, name TEXT, price REAL)')

def data_entry(names, prices):
	for i in range(len(names)):
		c.execute("INSERT INTO books (name, price) VALUES (?, ?)", (names[i], prices[i]))
	conn.commit()
	c.close()

names = ['1984', 'The Three-Body Problem', 'A Christmas Carol', 'Pride And Prejudice', 'The Great Gatsby', 'Hamlet']
prices = [10, 15.5, 12.0, 9.5, 8.0, 11.0]
create_table()
data_entry(names, prices)
