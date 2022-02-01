# DB
import sqlite3
from sqlite3 import Error
# Functions
from urllib.request import pathname2url
from datetime import datetime

_DBPATH = 'languageDB.db'

def connect():
	conn = sqlite3.connect(_DBPATH)
	cursor = conn.cursor()
	return conn, cursor
#Phrase
def get_topic_for_phrase():
	conn, c = connect()
	data = ""
	try:
		c.execute('SELECT id, name FROM topic where isPhrase = 1 order by name')
		data = c.fetchall()
	except:
		create_table_topic()
		print("Can't open database")
	c.close()
	return data
	
def add_phrase(content, topic):
	try:
		conn, c = connect()
		c.execute('INSERT INTO phrase(content, topic) VALUES (?, ?)',(content, topic))
		conn.commit()
		c.close()
	except:
		print("Can't insert to the database")

def create_table_phrase():
	conn, c = connect()
	c.execute('CREATE TABLE IF NOT EXISTS phrase(ID INTEGER PRIMARY KEY AUTOINCREMENT, content TEXT, topic int)')
	c.close()

def get_phrase_by_topic(topic):
	conn, c = connect()
	data = ""
	try:
		c.execute('SELECT id, content FROM phrase where topic="{}" order by content'.format(topic))
		data = c.fetchall()
	except:
		create_table_phrase()
		print("Can't open database")
	c.close()
	return data

def get_phrase():
	conn, c = connect()
	data = ""
	try:
		c.execute('SELECT id, content FROM phrase order by content')
		data = c.fetchall()
	except:
		create_table_phrase()
		print("Can't open database")
	c.close()
	return data

def get_by_id_phrase(id):
	conn, c = connect()
	c.execute('SELECT * FROM phrase WHERE id="{}"'.format(id))
	data = c.fetchall()
	c.close()
	return data

def delete_phrase(id):
	conn, c = connect()
	c.execute('DELETE FROM phrase WHERE id="{}"'.format(id))
	conn.commit()
	c.close()

def edit_phrase(content, topic, id):
	conn, c = connect()
	c.execute('UPDATE phrase set content = ?, topic = ? WHERE id=?', (content, topic, id))
	conn.commit()
	c.close()

#Topic
def add_topic(name, phrase):
	try:
		conn, c = connect()
		c.execute('INSERT INTO topic(name, isPhrase) VALUES (?, ?)',(name, phrase))
		conn.commit()
		c.close()
	except:
		print("Can't insert to the database")

def create_table_topic():
	conn, c = connect()
	c.execute('CREATE TABLE IF NOT EXISTS topic(ID INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, isPhrase int)')
	c.close()
def get_topics():
	conn, c = connect()
	data = ""
	try:
		c.execute('SELECT id, name FROM topic where isPhrase!=1 order by name')
		data = c.fetchall()
	except:
		create_table_topic()
		print("Can't open database")
	c.close()
	return data

def view_all_topic():
	conn, c = connect()
	data = ""
	try:
		c.execute('SELECT id, name, isPhrase FROM topic')
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

def edit_topic(name, phrase, id):
	conn, c = connect()
	c.execute('UPDATE topic set name = ?, isPhrase = ? WHERE id=?', (name, phrase, id))
	conn.commit()
	c.close()
#Contact
def create_table_contact():
	conn, c = connect()
	c.execute('CREATE TABLE IF NOT EXISTS contact(id INTEGER PRIMARY KEY AUTOINCREMENT, content TEXT, time text)')
	c.close()

def add_contact(content):
	try:
		conn, c = connect()
		now = datetime.now()
		current_time = now.strftime("%H:%M:%S")
		c.execute('INSERT INTO contact(content, time) VALUES (?, ?)',(content, current_time))
		conn.commit()
		c.close()
	except:
		print("Can't insert to the database")

def get_contacts():
	conn, c = connect()
	data = ""
	try:
		c.execute('SELECT id, content FROM contact order by content')
		data = c.fetchall()
	except:
		create_table_contact()
		print("Can't open database")
	c.close()
	return data


#Vocab
def create_table_vocab():
	conn, c = connect()
	c.execute('CREATE TABLE IF NOT EXISTS vocab(ID INTEGER PRIMARY KEY AUTOINCREMENT, word text, spelling text, topic int)')
	c.close()

def add_vocab(word, spelling, topic):
	conn, c = connect()
	c.execute('INSERT INTO vocab(word, spelling, topic) VALUES (?,?,?)',(word, spelling, topic))
	conn.commit()
	c.close()

def get_vocab_by_topic(id_topic):
	conn, c = connect()
	data = ""
	try:
		c.execute('SELECT id, word FROM VOCAB where topic = "{}" order by word'.format(id_topic))
		data = c.fetchall()
	except:
		print("Can't open database")
	c.close()
	return data

def view_all_vocab():
	conn, c = connect()
	data = ""
	try:
		c.execute('SELECT id, word, name FROM VOCAB inner join TOPIC on VOCAB.topic = TOPIC.id order by word')
		data = c.fetchall()
	except:
		create_table_vocab()
		print("Can't open database")
	c.close()
	return data

def view_vocab_by_topic(id_topic):
	conn, c = connect()
	data = ""
	try:
		c.execute('SELECT word, spelling FROM VOCAB where topic = "{}" order by word'.format(id_topic))
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

def edit_vocab(old_word, new_word, spelling, topic):
	conn, c = connect()
	c.execute('UPDATE vocab set word = ?, spelling = ?, topic = ? WHERE word=?', (new_word, spelling, topic, old_word))
	conn.commit()
	c.close()


