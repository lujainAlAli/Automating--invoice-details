from flask import Flask, render, redner_template, request
import sqlite3 as sql

#need to create a way to add new loc to list6 of current locations

app=Flask(__name__)

@app.route('/', methods=["GET","POST"])

def gfg():
    if request.method="POST":
        date=request.form.get("date")
        pic=request.form.get("pic")
        loc=request.form.get("locations")
        new_loc=request.form.get("new-loc")
        amt=request.form.get("amt")
        inv_id=request.form.get("inovice")
        columns=[date,pic,loc,amt, in_id]
        return columns




columns_list=gfg()
con=sqlite3.connect("invoice_database.db")
cur=con.cursor()
cur.execute("CREATE TABLE invoice_details(columns)")

        