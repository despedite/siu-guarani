# CHUPALASIU, de Erik Bianco Vera
# despedite.xyz

# No tomo responsabilidad por el uso de esta herramienta.
# Licenciado bajo GPL-3.0.

# COMO USAR:
# 1. Leer y modificar los valores en VARIABLES A MODIFICAR.
# 2. Correr en la ventana de comandos, con el DNI al lado. (python siu.py 42XXXXXX)
# 3. Introducir tu contraseña de SIU Guaraní cuando la solicite.
# 4. ¡Dejar correr en el fondo!

# TO-DO: Auto-inscripción,
# detectar cuando se abrió una nueva comisión que no existía antes,
# detectar si se deslogueó solo o está en mantenimiento en el loop,
# cambiar "time.sleep()" a una solución como la gente,
# cambiar valores a JSON.

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
import argparse
from getpass import getpass
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import re
import smtplib 
from email.message import EmailMessage
import sys
from selenium.common.exceptions import NoSuchElementException
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# -----------------------
#  VARIABLES A MODIFICAR
# -----------------------

# PATH AL WEBDRIVER:
# Para correr este código, necesitás descargar un "webdriver", una herramienta
# que deja a código acceder a un navegador como si fuese un usuario.
# Conseguí el de Google Chrome acá: https://sites.google.com/a/chromium.org/chromedriver/home,
# y escribí el path de donde está descargado.

webdriverPath = "/home/user/chupala-siu/chromedriver"

# INSTRUCCIONES:
# Cargá este diccionario con la llave del código de la materia (01234),
# y un array con códigos de las comisiones a las que te querés unir
# (123-1-A12), en orden de prioridad.
# Los siguientes están a modo de ejemplo. ¡Modificar!

subjects = {
	"00487": ["487-4-G14", "487-5-G14", "487-3-G14", "487-2-G14", "487-1-G14"],
	"01033": ["1033-2-G14", "1033-4-G14", "1033-3-G14", "1033-1-G14"]
}

usedSubjects = []

# OPCIONAL: Enviar notificaciones por correo electrónico.
# Si los valores son NULL, se desactiva - solo vás a ser notificado por la consola.
# Si te gustaría ser enviado correos, escribí el correo y contraseña de tu mail
# (recomendamos que crees uno para esto), y el mail del que va a recibir los correos.
# También activá esto: https://www.google.com/settings/security/lesssecureapps

emailId = None # Correo del enviador. (emailId = chupalasiu@gmail.com)
Pass = None # Contraseña del enviador. (Pass = "contraseña")
yourMail = None # Correo del que recibe el mail. (yourMail = tumail@gmail.com)

# URL: La URL del sitio web de login.
# DASHBOARD: La URL del sitio que aparece cuando iniciaste sesión.
# En este caso, el de la Universidad Nacional de Quilmes (la única testeada).
# YMMV en otros SIUs.

url = 'https://guarani.unq.edu.ar/grado/acceso'
dashboard = 'https://guarani.unq.edu.ar/grado/cursada'

# ---------------------
#      EL CÓDIGO
# ---------------------
# (¡Para usuarios avanzados!)

# "You go and search it through the Jello-net!"
# TO-DO: Enviar todas las materias aplicables en un solo mail.

def sendEmail(html, subjectName):
	msg = EmailMessage()
	msg['Subject'] = subjectName # Subject of Email
	msg['From'] = emailId
	msg['To'] = yourMail # Reciver of the Mail
	msg.set_content(MIMEText(html, 'html'))

	with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
		smtp.login(emailId,Pass)
		smtp.sendmail(emailId, yourMail, msg.as_string())
		print("¡Enviamos un email a " + yourMail + "!")

# El código para escanear las materias.
# TO-DO: Sistema de prioridad.
# ¿Auto-inscripción?

def scanSubjects(subjectKey, subjectName):
	commisions = driver.find_elements_by_class_name("comision")
	for commision in commisions:
		try:
			commissionCode = commision.find_element_by_tag_name("h4")
			subjectArray = subjects.get(subjectKey)
			if commissionCode.text in subjectArray:
				try:
					availability = commision.find_element_by_class_name("form_inscribir")
					if availability:
						if commissionCode.text in usedSubjects:
							print("Hay cupos en " + commissionCode.text + ", pero ya estaba notificado.")
						else:
							print("Encontramos cupos en " + commissionCode.text + "!")
							if emailId and Pass:
								message = """\
								<html>
								  <head></head>
								  <body>
								    <p><i>¡Buenas!</i><br>

										ChupalaSIU encontró un cupo en la materia <b>""" + subjectName + """</b>.<br>
										El número de comisión es <b>""" + commissionCode.text + """</b>.<br>
										<a href=\"""" + driver.current_url + """\">¡Agarralo antes de que sea tarde siguiendo este link!</a><br>

										- ChupalaSIU
								    </p>
								  </body>
								</html>
								"""
								
								sendEmail(message, "Encontamos cupos en " + subjectName + "!")
								usedSubjects.append(commissionCode.text)
				except NoSuchElementException:
					print("No hay cupos en " + commissionCode.text + ".")
		except:
			# Probablemente una en la que ya estás metido. Ups!
			print("Hubo un error tratando de conseguir una comisión. Ignorando...")

# TO-DO: Esto es HORRIBLE.
# Va a funcionar si tenes una buena conexión.
cooldown = 2

# Necesitamos conseguir el DNI y CONTRASEÑA del usuario en la consola.

parser = argparse.ArgumentParser(description="Scrapear las inscripciones en el sitio de la UNQ.")
parser.add_argument("dni")
args = parser.parse_args()

args.password = getpass("Ingresá la contraseña para loguearte en el SIU: ")

driver = webdriver.Chrome(webdriverPath)
pageAvailable = True

# Vamos al sitio web.
driver.get(url)

# Revisemos si la página está en mantenimiento.
# TO-DO: Chequear esto en el loop también.

leadElements = driver.find_elements_by_class_name("lead")
for leadElement in leadElements:
	if (leadElement.text == "Por favor, cerrá esta ventana y volvé a ingresar nuevamente en unos minutos."):
		print("La página SIU Guaraní está en mantenimiento! Volvé a intentarlo más tarde.")
		pageAvailable = False
		break

# ¡Dale, logueate de una vez!
if pageAvailable:
	time.sleep(cooldown)
	loginForm = driver.find_element_by_id("guarani_form_login")
	if loginForm:
		username = driver.find_element_by_id("usuario")
		password = driver.find_element_by_id("password")

		username.send_keys(args.dni)
		password.send_keys(args.password)
		
		driver.find_element_by_name("login").click()
		time.sleep(cooldown)

		try:
			time.sleep(cooldown)
			errorMessage = driver.find_element_by_id("error_login")
			if errorMessage:
				print("No pudimos iniciar sesión. ¿Nombre de usuario o contraseña incorrectos?")
		except:
			# (hacker voice) WE'RE IN.
			# Vayamos a la página de una vez.

			# Eliminá esta línea si solo querés correr el código una vez.
			while True:

        driver.get(dashboard)
				time.sleep(cooldown)

				# Escaneá la lista de materias.
				elem = driver.find_element_by_id("js-listado-materias")
				all_li = elem.find_elements_by_tag_name("li")
				for li in all_li:
					text = li.text
					parsedText = re.search(r"\(([A-Za-z0-9_]+)\)", text)
					for key, value in subjects.items():
						if key == parsedText.group(1):
							print ("Escaneándo en " + li.text + "...")
							li.click()
							time.sleep(cooldown)
							# Escaneá las comisiones.
							scanSubjects(parsedText.group(1), li.text)
							break


	else:
		print("No encuentro el login, por alguna razón. Puede ser que la página esté en mantenimiento o que no sea la hora para inscribirte.")
	
driver.close()
