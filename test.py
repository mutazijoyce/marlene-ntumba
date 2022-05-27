import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QMessageBox, QWidget, QLineEdit, QTableWidgetItem
from PyQt5.uic import loadUi
import mysql.connector

code = "0001CB01C"
montant_verse = 100000
mt_verse = int(montant_verse)      

dbcon = mysql.connector.connect(
    host = "localhost",
    port = 3306,
    user = "root",
    password = "",
    db = "db_compte"
)
myCursor = dbcon.cursor()
myCursor.execute("SELECT * FROM compte WHERE code = '"+code+"'")
result = myCursor.fetchall()

if result:
    print(result)
    solde = result[0][2]

    nx_sold = mt_verse + float(solde)

    myCursor.execute("UPDATE compte SET solde = '"+str(nx_sold)+"'")
    dbcon.commit()
    print("Votre compte a été alimenté, votre nouveau solde est '"+str(nx_sold)+"'")

else:
    print("compte non recounnu")


