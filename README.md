PROYECTO DE PYTHON INTEGRANTES:
	NICOLAS CASTRO VILLA
	JAVIER DE LA ROSA VITAR
	ALFREDO QUINTANA CARIAGA


---INSTALACIONES NECESARIAS---


Instalar python desde la version 3 en adelante  

	https://www.python.org/downloads/windows/ 

Luego de instalar buscar la carpeta en donde instaló python. En el buscador escribir python y hacer click derecho, seleccionar abrir ubicacion de archivo en python 3."vesion instalada" realizar el mismo (hacer click derecho y seleccionar ubicacionde archivo).
Al estar dentro de la carpeta de python; procederemos a agregar python y pip como variables de entorno(agregando las rutas de la instalacion en path).

En la carpeta en donde se encuentra python copiar la ruta de instalacion 

	Ejemplo de ruta C:\Users\Usuario\AppData\Local\Programs\Python\Python38-32   

Luego en el buscador escribir "variables de entorno" y seleccionar. Nos abrirá una ventana en la cual debemos hacer click en variables de entorno,abrira otra ventana en la cual dentro de "variables de usuario" hacer doble clic en donde diga Path. seleccionar nuevo y pegar la ruta de python (la cual copiamos en el paso anterior). con eso agregamos python como variable de entorno, ahora lo haremos agregaremos pip. 
En la carpeta en donde esta python seleccionamos la carpeta scripts dentro de ella copiamos la ruta y realizamos el paso anterio dentro de la ventana de variables de entorno creando una nueva y pegando la ruta 

	Ejemplo de ruta C:\Users\Usuario\AppData\Local\Programs\Python\Python38-32\Scripts

con eso agregamos pip como variable de entorno.

Descargar mysql mariaDB 

	https://downloads.mariadb.org/mariadb/10.4.12/
	mariadb-10.4.12-winx64.msi o mariadb-10.4.12-win32.msi

una vez instalado debemos agregar mysql como variable de entorno realizando los mismos pasos que para python. por lo que debemos ir a la ubicacion del archivo copiar la ruta y agregarla como variable de entorno.
Para copiar la ruta nos dirijimos a el disco local, luego archivos de programa y buscar la carpeta donde esta instalado mariadb. Dentro de la carpeta de mariadb ingresamos a la carpeta bin, en esta carpeta copiamos la ruta para agregarla como variable de entorno

	Ejemplo de ruta: C:\Program Files\MariaDB 10.4\bin

Descargar git 

	https://git-scm.com/downloads

---------------------------------------------------------------------------------------------------------------------------------------------------------------------

CLONAR PROYECTO DESDE GITHUB

	https://github.com/ncastrovilla/Proyecto-python/

Nos posicionamos en el escritorio hacemos click derecho y abrimos una consolda de git (git bash) e introducimos los siguientes comando

1) git clone https://github.com/ncastrovilla/Proyecto-python/


Ejecutar una cmd, ir a la ruta del proyecto clonado dentro del escritorio
	
	ejecutar el comando: pip install -r requirements.txt

luego crearemos una basededatos 

1) mysql -u root -p 

2) create database con el nombre vacunatorio, luego poner exit 
	
	create database vacunatorio;

3) estando dentro de la consola procedemos a recuperar la base de datos del proyecto 

	 mysql -u root -p vacunatorio<python.sql

4) ejecutamos el proyecto 

	python proyecto.py



