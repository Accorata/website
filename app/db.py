import sqlite3
import csv

db_file_name = "database.db"

db = sqlite3.connect(db_file_name, check_same_thread=False)
c = db.cursor()
c.executescript("""
    create table if not exists paintings(id int primary key, name text);
""")
db.commit()
c.close()


def add_new_painting(painting_name):
    c = db.cursor()
    c.execute("insert into paintings values(?, ?)", (1, painting_name,))
    db.commit()
    c.close()
    print("Log: new painting named "+painting_name+" added")

#     create TABLE if NOT EXISTS user(u_id int primary key, username varchar(20), password varchar(30));
