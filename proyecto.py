import requests
import json
from flask import Flask, render_template, jsonify, request
from flaskext.mysql import MySQL
import pymysql
import pymysql.cursors


app = Flask(__name__)
app.config["MYSQL_DATABASE_USER"] = "root"
app.config["MYSQL_DATABASE_DB"]  = "vacunatorio"

mysql = MySQL(app)
mysql.connect_args["autocommit"] = True 
mysql.connect_args["cursorclass"] = pymysql.cursors.DictCursor

@app.route('/pacientes')
def pacientes():
	cursor = mysql.get_db().cursor()
	cursor.execute("SELECT * FROM Paciente")

	paciente=cursor.fetchall()
	return render_template('pacientes.html',pacient = paciente)

@app.route('/pacientes/add')
def padd():
	return render_template('nuevopaciente.html')

@app.route('/vacunas')
def vacunas():
	cursor = mysql.get_db().cursor()
	cursor.execute("SELECT * FROM Vacuna")

	vacunas=cursor.fetchall()
	return render_template('vacunas.html',vac = vacunas)

@app.route('/vacunas/add')
def vadd():
	return render_template('nuevavacuna.html')



if __name__ == "__main__":
	app.run(debug=True)