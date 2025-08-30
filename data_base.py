import sqlite3 as sql

con=sql.connect("invoice_details.db")
cursor=con.cursor()

def create_db():
    cursor.execute("CREATE TABLE IF NOT EXISTS invoice_details(date TEXT ,loc TEXT,amt REAL ,inv_id INTEGER)")


def data_entry(columns):
    date=columns[0]
    #pic=columns[1]
    loc=columns[2]
    amt=columns[3]
    inv_id=columns[4]
    cursor.execute("INSERT INTO invoice_details(date,pic,loc,amt,inv_id) VALUES(?,?,?,?,?)",(date,loc,amt,inv_id))
    con.commit()

#create_db()

#cursor.execute("""INSERT INTO invoice_details (date,loc,amt,inv_id) VALUES(?,?,?,?)""",("970-01-01 00:00:00",'hello',12346,123456))
#con.commit()