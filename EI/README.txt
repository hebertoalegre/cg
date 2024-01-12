#############################################INSTRUCTIVO######################################
El proyecto consta de tres partes que son:
	-Extraccion de data 
  	-Armonizar y almacenar la data en SQL (sqlite)
	-Query de verificacion

En las siguientes secciones se describira como funciona cada sección y como se ejecuta cada una de ellas, además se mostrara como se instala el proyecto en una computadora que tenga instalado Pytho +3.10 y Visual Estudio Code. El proyecto se observa de la siguiente manera:

--Carpeta creada
	--EI
		--.venv (creado a partir de la seccion de instalación)
		--eipp 
		--instance
		--outputs
		app.py
		queries.py
		requirements.txt
		scrapy.cfg

#############################################INSTALACION######################################

Para poder instalar el proyecto debe realizar las siguientes instrucciones:
	1. Crear una carpeta con el nombre del proyecto 
	2. Pegar la carpeta EI dentro de la carpeta creada 
	3. Abrir Visual Estudio Code
	4. Dirigirse a File/Open Folder y seleccionar la carpeta creada.
	5. Crear un ambiente virtual (.venv), para ello debe de ejecutar el comando CTRL+SHIFT+p y se abrira una ventana auxiliar y selecccionar la opción Python:Create enviroment...,      	 	porsteriormente selecionar venv y luego seleccionar 	   python de su predileccion, de preferencia pythoh 3.10 o más.
	6. Se creara un archivo venv, dentro del proyecto. Ejecutar el comando CTRL+SHIFT+` dirigirse a la esquina inferior izquierda y selecionar el signo +, abrir CMD y copiar y ejecutar el 	siguiente instructivo:
		
		python -m pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org -r ./requirements.txt

Esperar a que se instalen todas las dependencias y listo!!!!!!.



########################################Extraccion de data ######################################

Para llevar a cabo la extraccion de la data se utilizo la dependencia SCRAPY que es una herramienta de extracción de datos de código abierto que tiene como principal objetivo extraer la información de determinado sitio web, scrapy web es un programa que te servirá para el desarrollo de crawler o arañas web. Se desarrolla como un proyecto bajo el nombre de eipp y consta de las siguientes partes:
	eipp--
		--spiders
			spider.py
		__init__.py
		items.py
		middlewares.py
		pipelines.py
		settings.py

Como se usa?

Para llevar a cabo la extraccion de data es ALTAMENTE RECOMENDABLE reiniciar el ordenador antes de ejecutar, debido a las limitaciones de internet donde se ha de correr. Posteriormente se debe de abrir CMD, copiar y ejecutar el siguiente comando:
		
	scrapy crawl cg -L WARN

Esta ejecución permitira al programa entrar a las siguientes páginas web.
	* https://banguat.gob.gt/es/page/comercio-general-version-xlsx
	* https://banguat.gob.gt/page/anios-2002-2017-comercio-general

Extrayendo unicamente de ellas las direccines URL de los archivos de formato excel que corresponden a los datos correspondientes de Comercio Exterior de Guatemala por Inciso Arancelario del Sistema Arancelario Centroamericano SAC (a 8 y 10 dígitos) del Banco Central de Guatemala. El mismo programa se encargara de leer cada una de las urls, extraer la data de ellas, armonizarlas y guardarlas dentro de la carpeta outputs. Esta ejecucion esta considerada en tardar un máximo de 8 minutos, para las condiciones de la computadora y servicio de internet donde fue desarrolla y el tiempo de ejecucion puede variar.

 
#######################Armonizar y almacenar la data en SQL (sqlite) ############################

Armonizar se hace referencia a limpiar data, ajustar de acuerdo a las necesidades de la misma informacion, recopilarlas almacenarlas en un formato de sqlite. Para ejecutar esta seccion se debe seleccionar dentro del proyecto el archivo app.py y correrlo presionando ejecutar (boton en forma de triangulo) en la esquina superior derecha del mismo y esperar a que el archivo sea almacendo en la base de datos previamente armada por Scrapy. Esta ejecución tarda aproximadamente 3 minutos, bajo los mismos supuestos de la sección anterior.


########################################Query de verificación ######################################	
El query de verificación sirve para observar si los resultados de los comandos anteriormente descritos, extrayeron de manera correcta la informacion. Este archivo consta de conectar el programa a la base de SQLITE y correr el siguiente query:

query = ''' SELECT fecha, var, sum(vol), sum(value) 
            FROM  cg_db
            GROUP BY  var, fecha
            ORDER BY  var, fecha
            '''

Este instructivo selecciona de la base de datos la fecha, el tipo de variable y las sumas de volumens y valores, las agrupa por variable y fecha, extrayendo los totales por mes por tipo de variable. 

Para poder ejecutar esta seccion se debe seleccionar dentro del proyecto el archivo queries.py y correrlo presionando ejecutar (boton en forma de triangulo) en la esquina superior derecha del mismo y esperar a que el archivo sea almacendo en la base de datos previamente armada por Scrapy. Esta ejecución tarda aproximadamente 3 minutos, bajo los mismos supuestos de la sección anterior.






