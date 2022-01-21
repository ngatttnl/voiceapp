# DB
import sqlite3
from sqlite3 import Error
# Functions
from urllib.request import pathname2url


_DBPATH = 'languageDB.db'

def connect():
	conn = sqlite3.connect(_DBPATH)
	cursor = conn.cursor()
	return conn, cursor

#Topic
def add_topic(name):
	try:
		conn, c = connect()
		c.execute('INSERT INTO topic(name, description) VALUES (?, ?)',(name, name))
		conn.commit()
		c.close()
	except:
		print("Can't insert to the database")

def create_table_topic():
	conn, c = connect()
	c.execute('CREATE TABLE IF NOT EXISTS topic(ID INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, description text)')
	c.close()

def view_all_topic():
	conn, c = connect()
	data = ""
	try:
		c.execute('SELECT * FROM topic')
		data = c.fetchall()
	except:
		create_table_topic()
		print("Can't open database")
	c.close()
	return data

def get_by_id_topic(id):
	conn, c = connect()
	c.execute('SELECT * FROM topic WHERE id="{}"'.format(id))
	data = c.fetchall()
	c.close()
	return data

def delete_topic(id):
	conn, c = connect()
	c.execute('DELETE FROM topic WHERE id="{}"'.format(id))
	conn.commit()
	c.close()

def edit_topic(name, id):
	conn, c = connect()
	c.execute('UPDATE topic set name = ? WHERE id=?', (name, id))
	conn.commit()
	c.close()

#Vocab
def create_table_vocab():
	conn, c = connect()
	c.execute('CREATE TABLE IF NOT EXISTS vocab(word text, spelling TEXT, meaning TEXT, topic text, language text)')
	c.close()

def add_vocab(word, spelling, meaning, topic, language):
	conn, c = connect()
	c.execute('INSERT INTO vocab(word, spelling, meaning, topic, language) VALUES (?,?,?,?,?)',(word, spelling, meaning, topic, language))
	conn.commit()
	c.close()

def view_all_vocab():
	conn, c = connect()
	data = ""
	try:
		c.execute('SELECT word, spelling, meaning, name FROM VOCAB inner join TOPIC on VOCAB.topic = TOPIC.id')
		data = c.fetchall()
	except:
		create_table_vocab()
		print("Can't open database")
	c.close()
	return data

def get_by_id_vocab(id):
	conn, c = connect()
	c.execute('SELECT * FROM vocab WHERE id="{}"'.format(id))
	data = c.fetchall()
	c.close()
	return data

def delete_vocab(id):
	conn, c = connect()
	c.execute('DELETE FROM vocab WHERE name="{}"'.format(id))
	conn.commit()
	c.close()

def edit_vocab(content, topic, id):
	conn, c = connect()
	c.execute('UPDATE vocab set content =?, topic = ? WHERE id=?', (content, topic, id))
	conn.commit()
	c.close()


