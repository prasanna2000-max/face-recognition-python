import sqlite3
conn = sqlite3.connect('database.db')
cur = conn.cursor()
c1=3
uname=input("Enter your name")
print(uname)
cur.execute("select * from users") 
  
  
print( cur.fetchall() )
conn.commit()
conn.close()