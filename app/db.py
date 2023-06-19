import sqlite3
import csv
import random as rng

db_file_name = "database.db"

db = sqlite3.connect(db_file_name, check_same_thread=False)
c = db.cursor()
c.executescript("""
    create table if not exists paintings(id int primary key, name text);
""")#file_name
db.commit()
c.close()


def add_new_painting(painting_name):
    c = db.cursor()
    try :
        id = rng.random()
        c.execute("insert into paintings values(?, ?)", (id, painting_name,))
        print("Log: new painting named "+painting_name+" added with id="+str(id))
    except sqlite3.IntegrityError :
        add_new_painting(painting_name)
    db.commit()
    c.close()

def get_painting(painting_name):
    c = db.cursor()
    painting = c.execute("select * from paintings where name=?", (painting_name,)).fetchall()
    c.close()
    return painting

def get_paintings():
    c = db.cursor()
    paintings = c.execute("select * from paintings").fetchall()
    c.close()
    return paintings

#     create TABLE if NOT EXISTS user(u_id int primary key, username varchar(20), password varchar(30));
