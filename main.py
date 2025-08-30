from flask import Flask, request,render_template,redirect,url_for
import sqlite3 as sql
import subprocess


#need to create a way to add new loc to list6 of current locations

app=Flask(__name__)

con=sql.connect("invoice_details.db")
c=con.cursor()
c.execute("CREATE TABLE IF NOT EXISTS invoice_details(date INTEGER, pic BLOB, loc TEXT, amt REAL,inv_id INTEGER)")
con.commit()
con.close()


@app.route('/', methods=["GET","POST"])
def home():
    if request.method=="POST":
        date=request.form.get("date")
        pic=request.form.get("pic")
        loc=request.form.get("locations")
        new_loc=request.form.get("new-loc")
        amt=request.form.get("amt") 
        inv_id=request.form.get("invoice")
        columns=[date,pic,loc,amt, inv_id]
        
        con=sql.connect("invoice_details.db")
        c=con.cursor()
        c.execute("INSERT INTO invoice_details(date,pic,loc,amt,inv_id) VALUES(?,?,?,?,?)",(date,pic,loc,amt,inv_id))
        con.commit()
        con.close()
        return redirect('/submitted')
    else:
        return render_template("main.html")


@app.route('/submitted', methods=['get'])
def submitted():
    return render_template('submitted.html')

if __name__=="__main__":
    app.run()
    