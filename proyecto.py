import requests
import json
from flask import Flask, render_template, jsonify, request , redirect
from flaskext.mysql import MySQL
import pymysql
import pymysql.cursors


app = Flask(__name__)
app.config["MYSQL_DATABASE_USER"] = "root"
app.config["MYSQL_DATABASE_DB"]  = "vacunatorio"

mysql = MySQL(app)
mysql.connect_args["autocommit"] = True 
mysql.connect_args["cursorclass"] = pymysql.cursors.DictCursor

@app.route('/') 
def pacientes():
	cursor = mysql.get_db().cursor()

	cursor.execute("SELECT * FROM Paciente")

	paciente=cursor.fetchall()
	return render_template('pacientes.html',pacient = paciente)

@app.route('/pacientes/add', methods=["GET","POST"])
def padd():
	cursor = mysql.get_db().cursor()

	if request.method == "GET":
		nombre = request.args.get('nombre', default = "", type = str)

	if request.method == "POST":
		nombre = request.form["nombre"]
		run = request.form["run"]
		nac = request.form["nacimiento"] 
		try:	
			sql = "INSERT INTO Paciente (id,nombre_paciente,rut,fecha_nacimiento)"
			sql += " VALUES(default,%s,%s,%s)"
			cursor.execute(sql,(nombre,run,nac))
		except Exception as e:
			print(e)
		return redirect('/')

	return render_template('nuevopaciente.html')

@app.route('/vacunas')
def vacunas():
	cursor = mysql.get_db().cursor()
	cursor.execute("SELECT * FROM Vacuna")

	vacunas=cursor.fetchall()
	return render_template('vacunas.html',vac = vacunas)

@app.route('/vacunas/add',  methods=["GET","POST"])
def vadd():
	cursor = mysql.get_db().cursor()

	if request.method == "GET":
		enfermedad = request.args.get('vacuna', default = "", type = str)

	if request.method == "POST":
		enfermedad = request.form["vacuna"]
		try:	
			sql = "INSERT INTO Vacuna (id,nombre_enfermedad)"
			sql += " VALUES(default,%s)"
			cursor.execute(sql,(enfermedad))
		except Exception as e:
			print(e)
		return redirect('/vacunas')
	return render_template('nuevavacuna.html')

@app.route('/pacientes/vacunar', methods=["GET","POST"])
def pvac():
	cursor = mysql.get_db().cursor()

	if request.method == "GET":
		idp = request.args.get('id', default = "", type = str)

	if request.method == "POST":
		idp = request.form['id']

	select = "SELECT * FROM Paciente"
	select += " WHERE id = %s"

	cursor.execute(select,(idp))

	pacivac = cursor.fetchall()

	cursor.execute("SELECT * FROM Vacuna")

	vac = cursor.fetchall()

	return render_template('vacunarpaciente.html', vacp= pacivac, vaco=vac)

@app.route('/pacientes/vacunar/listo', methods=["GET","POST"])
def pvl():
	cursor = mysql.get_db().cursor()

	if request.method == "GET":
		idp = request.args.get('idp', default = "", type = str)
		vac = request.args.get('vacunas', default="",type = int)

	if request.method == "POST":
		idp = request.form['idp']
		vac = request.form['vacunas']

	sql = "INSERT INTO recibe (id,idpaciente,idvacuna)"
	sql += " VALUES(default,%s,%s)"

	cursor.execute(sql,(idp,vac))

	return redirect('/')

@app.route('/vacunas/pacientes', methods=["GET","POST"])
def vacp():
	cursor = mysql.get_db().cursor()

	if request.method == "GET":
		idv = request.args.get('id', default = "", type = str)

	if request.method == "POST":
		idv = request.form['id']

	select = "SELECT v.nombre_enfermedad,p.nombre_paciente,p.rut,r.fechavacuna FROM Vacuna as v, Paciente as p, recibe as r "
	select += " WHERE r.idvacuna=v.id AND p.id=r.idpaciente AND v.id=%s"

	cursor.execute(select,(idv))

	vacupaci = cursor.fetchall()

	select2 = "SELECT nombre_enfermedad FROM Vacuna"
	select2 += " WHERE id=%s"

	cursor.execute(select2,(idv))

	nombre = cursor.fetchall()

	return render_template('vacuna.html', vacuna=vacupaci, n=nombre)

@app.route('/pacientes/vacunas', methods=["GET","POST"])
def pc():
	cursor = mysql.get_db().cursor()

	if request.method == "GET":
		idp = request.args.get('id', default = "", type = str)

	if request.method == "POST":
		idp = request.form['id']

	select = "SELECT v.nombre_enfermedad,r.fechavacuna FROM Vacuna as v,recibe as r"
	select += " WHERE r.idvacuna = v.id AND r.idpaciente = %s"

	cursor.execute(select,(idp))

	pacivacuna = cursor.fetchall()

	select = "SELECT nombre_paciente FROM Paciente"
	select += " WHERE id = %s"

	cursor.execute(select,(idp))

	npaci = cursor.fetchall()

	return render_template('vacunapaciente.html', pacvacuna = pacivacuna, n=npaci)

if __name__ == "__main__":
	app.run(debug=True)