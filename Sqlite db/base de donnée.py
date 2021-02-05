import sqlite3
import time
import random
import datetime
connect = sqlite3.connect("fichier.db")
cursor = connect.cursor()
def create_table():

    cursor.execute('CREATE TABLE IF NOT EXISTS stuffToplot(unix TEXT, datestamp TEXT, keyworld REAL, value REAL)')  # pour les colonnes

def table():
    cursor.execute("INSERT INTO stuffToplot VALUES('guillaume', '0802', 'python', 5)")#ou avec dictionnaire
    connect.commit()#sauvegarder modifications
    cursor.close()
    connect.close()

def nouvelles_valeurs():
     unix = time.time()
     date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
     keyworld = "python"
     value = random.randrange(0, 11)
     cursor.execute("INSERT INTO stuffToplot (unix, datestamp, keyworld, value) VALUES(?, ?, ?, ?)", (unix, date, keyworld, value)) #ordre colonnes
     connect.commit()

create_table()
nouvelles_valeurs()
for i in range(1, 10):
    nouvelles_valeurs()
    time.sleep(1)
    connect.close()
    cursor.close()

#a partir d'un dichier exisitant
try:
    connect = sqlite3.connect("basedonnée.db")
    cursor = connect.cursor()
    req = cursor.execute("SELECT * FROM tt_users")
    for row in req.fetchall():
        print(row[1])
except Exception as e:
    print("ERREUR", e)
    connect = sqlite3.connect("basedonnée.db")
    connect.rollback() #ou .commit()
finally:
    connect = sqlite3.connect("basedonnée.db")
    connect.close()
