import sqlite3

con = sqlite3.connect('Application/todos.db')

def sql_insert(con, entities):

    cursorObj = con.cursor()
    
    cursorObj.execute('INSERT INTO todo(id, title, desc) VALUES(?, ?, ?)', entities)
    
    con.commit()

entities1 = (1, "Surprise Vegeta", "Have to surprise Vegeta with my new super cool super saiyan form.")

sql_insert(con, entities1)

entities2 = (2, "Go training", "Gotta go to Whis for training.")

sql_insert(con, entities2)