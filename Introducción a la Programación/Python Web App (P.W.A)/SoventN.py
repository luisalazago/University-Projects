from flask import Flask, render_template, url_for, redirect, request # Se importó la librería de FLask//
import datetime

app= Flask(__name__) # Con esto le asigna al archivo de que existe y se está sobre escribiendo el contenido de Flask.

# Usuario

users = ["Luis"]
passwords = ["gomez"]
nombres = []
apellidos = []
gustos = []
lastUser = ""
Mensajes = []
validacion = False

# Grupos

Grupo1 = ""
Grupo2 = ""
Grupo3 = ""
Grupo4 = ""
Grupo5 = ""
Grupo6 = ""
Grupo7 = ""
Grupos = [""]
Grupos_temporal=["grupo1", "grupo2", "grupo3", "grupo4", "grupo5", "grupo5", "grupo7"]
ultimoGrupo = []
descripcionGrupo = []
contador3 = 0
contador5 = 0
integrantes = [""] # Se inicia con un elemento de cero para que no tenga un error el índice de la lista no encontrada al momento de mandar un contador a Html.
solicitudes = []
SOLICITUD = None

# Eventos

Evento1 =[]
Evento2 =[]
Evento3 =[]
Evento4 =[]
Evento5 =[]
Evento6 =[]
Evento7 =[]
Evento8 =[]
eventos = []
Eventos_a_votacion = []
descripcionEventoTemp = []
Eventos_Temporal = ["evento1", "evento2", "evento3", "evento4", "evento5", "evento6", "evento7", "evento8"]
descripcionEvento = []
diaEventoTemp = []
votacionSi = 0
votacionNo = 0
diaEvento = []
lasEvento = []
contador4 = 0

@app.route("/", methods=["GET", "POST"]) # Se usa esto para indicar cual es la ruta principal, este caso el registro o logueo para continuar//
def Home():
	"""
	Esta función se encarga de retornar la página principal de la aplicación Web.
	Entradas: Ninguna.
	Salidas: Página principal.
	"""
	global users, passwords, Mensajes
	print(users)
	print(passwords)

	archivo = open("usuarios.txt", mode="r")
	datos = archivo.readlines()
	archivo.close()

	contador = 0
	while contador < len(datos):
		users.append(datos[contador][:-1])
		passwords.append(datos[contador+1][:-1])
		contador += 2
		temporal = []
		while datos[contador] != "\n":
			temporal.append(datos[contador][:-1])
			contador += 1
		Mensajes.append(temporal)
		contador += 1

	return render_template("Home Page.html")

@app.route("/Error", methods=["GET", "POST"])
def error():
	"""
	Función que muestra la página de error de la aplicación web.
	Entradas: Ninguna.
	Salidas: Error.
	"""
	error = "Lo siento tienes un error, por favor trata nuevamente."
	return render_template("error.html", datos={"error":error})

@app.route("/Login", methods=["GET", "POST"])
def login():
	"""
	Esta función se encarga de hacer correcto el login.
	Entradas: Ninguna. 
	Salidas: El login correcto.
	"""
	global users, passwords, lastUser, validacion

	ubicación = -1
	validacion = False

	if request.method == "POST":
		usuario = request.form["EntradaL"]
		contra = request.form["SalidaL"]

		indice = 0
		while indice < len(users):
			if usuario == users[indice] and contra == passwords[indice]:
				ubicación = indice
				print(users)
				print(passwords)
				print(Grupos)
				lastUser = usuario
				validacion = True
				Mensajes.append([lastUser, "", ""])
			indice = indice + 1
		if validacion:
			return render_template("Pagina principal2.html", datos={"login": users[ubicación],
																	"contraseña":passwords[ubicación],
																	"usuarios":users,
																	"usuario":lastUser,
																	"gruposAparecer":Grupos,
																	"integrantes":integrantes,
																	"integrantes1":integrantes[contador5]})
		else:
			return redirect(url_for('error'))


@app.route("/Help") # Esto redirecciona a las ayudas para los usuarios
def help():
	"""
	Esta función retorna a la página de ayudas para los usuarios de la aplicación.
	Entradas: Ninguna.
	Salidas: Retorna la página de ayudas.
	"""
	return render_template("Help.html")

@app.route("/About", methods=["GET", "POST"])
def about():
	"""
	Esta función se encarga se encarga de llevar a la persona a la página acerca de la página.
	Entradas: Ninguna.
	Salidas: El contenido acerca de la página.
	"""
	return render_template("About.html")

@app.route("/Register", methods=["GET", "POST"])
def registro():
	"""
	Esta función se encarga de ir al registro de la aplicación.
	Entradas: Ninguna.
	Salidas: Retorna la página del registro de la aplicación.
	"""
	global users, passwords, nombres, apellidos, gustos

	resultado = ""
	if request.method == "POST":
		usuario = request.form["EntradaR"]
		contra = request.form["SalidaR"]
		nombre = request.form["NombreR"]
		apellido = request.form["ApellidoR"]
		gusto = request.form["gusto"]

		if usuario in Grupos:
			error = "ya está registrado o le faltó llenar un campo, por favor intentelo nuevamente."
			return render_template("error2.html", datos={"error":error, "usuario":usuario})
		
		users.append(usuario)
		passwords.append(contra)
		nombres.append(nombre)
		apellidos.append(apellido)
		gustos.append(gusto)

		archivo = open("usuarios.txt", mode="a+")
		archivo.write(usuario + "\n")
		archivo.write(contra + "\n")
		archivo.write("\n")
		archivo.close()

		resultado = "Su registro ha sido exitoso!"
		return render_template("ExitosoR.html", datos={"resultado":resultado})
	return render_template("Registro.html", datos={})

@app.route("/SoventN", methods=["GET", "POST"])
def principal():
	"""
	Esta función se encarga de llevar al usuario a la página después del Login.
	Entradas: Ninguna
	Salidas: Llevar al usuario a la página principal.
	"""
	global Grupos, eventos, integrantes
	return render_template("Pagina principal.html", datos={"grupos":Grupos[contador3], "Grupos":len(Grupos),
														   "grupos1":Grupos_temporal[0], "grupos2":Grupos_temporal[1],
														   "grupos3":Grupos_temporal[2], "grupos4":Grupos_temporal[3],
														   "grupos5":Grupos_temporal[4], "grupos6":Grupos_temporal[5],
														   "grupos7":Grupos_temporal[6], "usuario":lastUser, 
														   "grupo1":Grupo1, "grupo2":Grupo2, "grupo3":Grupo3, 
														   "grupo4":Grupo4, "grupo5":Grupo5, "grupo6":Grupo6, 
														   "grupo7":Grupo7, "eventos1": Eventos_Temporal[0], 
														   "eventos2":Eventos_Temporal[1], "eventos3":Eventos_Temporal[2],
														   "eventos4":Eventos_Temporal[3], "eventos5":Eventos_Temporal[4],
														   "eventos6":Eventos_Temporal[5], "eventos7":Eventos_Temporal[6],
														   "eventos8":Eventos_Temporal[7], "Eventos":len(eventos), 
														   "evento1":Evento1, "evento2":Evento2,"evento3":Evento3, 
														   "evento4":Evento4, "evento5":Evento5, "evento6":Evento6, 
														   "evento7":Evento7, "gruposAparecer":Grupos, "integrantes":integrantes[contador5]})

@app.route("/SoventNetwork", methods=["GET", "POST"])
def principal2():
	"""
	Esta función se encarga de llevar al usuario a la página después del Login.
	Entradas: Ninguna.
	Salidas: Llevar al usuario a la página principal.
	"""
	global Grupos, eventos
	return render_template("Pagina principal.html", datos={"grupos":Grupos[contador3], "Grupos":len(Grupos),
														   "grupos1":Grupos_temporal[0], "grupos2":Grupos_temporal[1],
														   "grupos3":Grupos_temporal[2], "grupos4":Grupos_temporal[3],
														   "grupos5":Grupos_temporal[4], "grupos6":Grupos_temporal[5],
														   "grupos7":Grupos_temporal[6], "usuario":lastUser, 
														   "grupo1":Grupo1, "grupo2":Grupo2, "grupo3":Grupo3, 
														   "grupo4":Grupo4, "grupo5":Grupo5, "grupo6":Grupo6, 
														   "grupo7":Grupo7, "eventos1": Eventos_Temporal[0], 
														   "eventos2":Eventos_Temporal[1], "eventos3":Eventos_Temporal[2],
														   "eventos4":Eventos_Temporal[3], "eventos5":Eventos_Temporal[4],
														   "eventos6":Eventos_Temporal[5], "eventos7":Eventos_Temporal[6],
														   "eventos8":Eventos_Temporal[7], "Eventos":len(eventos), 
														   "evento1":Evento1, "evento2":Evento2,"evento3":Evento3, 
														   "evento4":Evento4, "evento5":Evento5, "evento6":Evento6, 
														   "evento7":Evento7, "gruposAparecer":Grupos, "evento":eventos,
														   "integrantes":integrantes[contador5]})


@app.route("/Mas_Grupos", methods=["GET", "POST"])
def grupos2():
	"""
	Esta función devuelve otra página de los grupos que está inscrito la persona.
	Entradas: Ninguna.
	Salidas: Devuelve todos los grupos del usuario.
	"""
	return render_template("MásGrupos.html", datos={})

@app.route("/Busquedas", methods=["GET", "POST"]) # Recuerda acomodarle los datos para enviar a la página.
def busqueda():
	"""
	Esta función permite ingresar a la búsqueda de grupos.
	Entradas: Ninguna.
	Salidas: Devuelve la página de búsquedas de todos los grupos.
	"""
	validoG = False
	if request.method == "POST":
		SearchG = request.form["GrupoBuscar"]

		if SearchG in Grupos:
			Mensaje = "Deseas Ingresear al grupo {} ?".format(SearchG)
			validoG = True
		else:
			Mensaje = "Lo siento, el grupo {} no sé encuentra registrado, por favor intentalo nuevamente".format(SearchG)
			return render_template("ErrorB.html", datos={"mensaje":Mensaje})

	return render_template("busqueda.html",datos={"grupos":SearchG, "mensaje":Mensaje, "valido":validoG,
												  "grupo1":Grupos[contador3], "grupos1":Grupos_temporal[0], 
												  "grupos2":Grupos_temporal[1], "grupos3":Grupos_temporal[2], 
												  "grupos4":Grupos_temporal[3], "grupos5":Grupos_temporal[4], 
												  "grupos6":Grupos_temporal[5], "grupos7":Grupos_temporal[6],
												  "Grupos":Grupos})

# Funciones para los grupos

@app.route("/Grupos", methods=["GET", "POST"])
def grupos():
	"""
	Función que se encarga de devolver la página de los grupos.
	Entradas: Ninguna.
	Salidas: Retorna la página de los grupos.
	"""
	print(Grupos)
	print(descripcionGrupo)
	return render_template("grupos.html", datos={})

@app.route("/Añadir_grupo", methods=["GET", "POST"])
def añadir_grupo():
	"""
	Esta función permite crear grupos con su propia descripción.
	Entadas: Ninguna.
	Salidas: Crea los grupos con su descripción y registra el grupo
			 si es nuevo y no ha estado registrado anteriormente, además
			 redirecciona a la función que confirma la creación del grupo.
	"""
	global Grupos, descripcionGrupo, ultimoGrupo, lista_contador, contador3, Grupo1, Grupo2, Grupo3, Grupo4, Grupo5, Grupo6, Grupo7, contador4, integrantes, contador5

	if request.method == "POST":
		grupo = request.form["Grupo"]
		descripción = request.form["Descripcion"]

		if "" in Grupos:
			Grupos.remove("")

		if grupo in Grupos:
			Error = "El grupo {}, ya está registrado por favor cree otro.".format(grupo)
			return render_template("ErrorG.html", datos={"error":Error})
		elif grupo == "":
			Error = "El grupo no tiene nombre, por favor cree uno con un nombre nuevamente"
			return render_template("ErrorG.html", datos={"error":Error})
		elif len(grupo) > 12:
			Error = "Lo siento el grupo solamente puede tener un máximo de 12 caracteres."
			return render_template("ErrorG.html", datos={"error":Error})

		if len(Grupos) == 0 and len(Grupo1) == 0:
			Grupo1 = grupo
		elif len(Grupos) > 0 and len(Grupo1) == 1 and len(Grupo2) == 0:
			Grupo2 = grupo
		elif len(Grupos) > 1 and len(Grupo1) == 1 and len(Grupo2) == 1 and len(Grupo3) == 0:
			Grupo3 = grupo
		elif len(Grupos) > 2 and len(Grupo1) == 1 and len(Grupo2) == 1 and len(Grupo3) == 1 and len(Grupo4) == 0:
			Grupo4 = grupo
		elif len(Grupos) > 3 and len(Grupo1) == 1 and len(Grupo2) == 1 and len(Grupo3) == 1 and len(Grupo4) == 1 and len(Grupo5) == 0:
			Grupo5 = grupo
		elif len(Grupos) > 4 and len(Grupo1) == 1 and len(Grupo2) == 1 and len(Grupo3) == 1 and len(Grupo4) == 1 and len(Grupo5) == 1 and len(Grupo6) == 0:
			Grupo6 = grupo
		elif len(Grupos) > 5 and len(Grupo1) == 1 and len(Grupo2) == 1 and len(Grupo3) == 1 and len(Grupo4) == 1 and len(Grupo5) == 1 and len(Grupo6) == 1 and len(Grupo7) == 0:
			Grupo7 = grupo

		Grupos.append(grupo)
		descripcionGrupo.append(descripción)
		ultimoGrupo.insert(0, grupo)
		integrantes.append([lastUser])

		archivo = open("Listas_Grupos.txt", mode="a+")
		archivo.write(grupo + "\n")
		archivo.write(descripción + "\n")
		archivo.write(integrantes + "\n")
		archivo.write("\n")
		archivo.close()

		if "" in integrantes:
			integrantes.remove("")

		contador = 0
		while contador < len(Grupos):
			if grupo == Grupos[contador]:
				contador2 = contador
				contador3 = contador2
			contador += 1

		contador = 0
		while contador < len(integrantes):
			if lastUser in integrantes[contador][contador]:
				contador5 = contador
			contador += 1
	print(contador5)
	print(contador3)
	return redirect(url_for('grupo_exitoso'))

@app.route("/Grupo_Exitoso", methods=["GET", "POST"])
def grupo_exitoso():
	"""
	Esta función retorna la verificación correcta del grupo creado anteriormente.
	Entradas: Ninguna.
	Salidas: Retorna la página de la verificación correcta del grupo.
	"""
	print(Grupos)
	print(descripcionGrupo)
	valido = "Felicidades su grupo: {}, ha sido registrado exitosamente ".format(ultimoGrupo[0]) 
	return render_template("ExitoG.html", datos={"validez":valido})

@app.route("/Aun_no_grupo", methods=["GET", "POST"])
def aúnNoGrupo():
	"""
	Esta función retorno la dirección de una página que permite ir a crear un grupo.
	Entradas: Ninguna.
	Salidas: Devuelve la página para ir a crear un grupo.
	"""
	ultimoUser = lastUser
	print(lastUser)
	return render_template("NoGrupoAun.html", datos={"usuario":ultimoUser})

# Calendario de la aplicación

def Calendario(mes, dia_de_laSemana):
	"""
	Procedimiento que permite calcular con una matriz el día en el que se encuentra.
	Entradas: Un mes y un día de la semana en que se encuentre el usuario.
	Salidas: El día correspondiente en el calendario.
	"""
	calendario = [[0, 0, 0, 0, 0, 0, 0],
				  [0, 0, 0, 0, 0, 0, 0],
				  [0, 0, 0, 0, 0, 0, 0],
				  [0, 0, 0, 0, 0, 0, 0],
				  [0, 0, 0, 0, 0, 0, 0]] # Con esto acomodamos la matriz de los días con las semanas.

	if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
		Udia = 31 # Ultimo día correpondiente al mes en el que se encuentre.
	elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
		Udia = 30
	else:
		Udia = 28

	dia = 1
	semana = 0

	while dia <= Udia: 
		while dia_de_laSemana < 7:
			calendario[semana][dia_de_laSemana] = dia # Aquí se muestra al día en el que está como corresponde a un día de la semana.
			dia_de_laSemana += 1
			dia += 1
			if dia == Udia + 1: # Con esta condición se le dice al programa que si llega al última día o el día después de ese acabe la iteración.
				break
		dia_de_laSemana = 0
		semana += 1

	return calendario


# Entrar Grupos

@app.route("/Solicitud", methods=["GET", "POST"])
def Solicitud():
	"""
	Función que permite añadir al usuario solicitante a las solicitudes.
	Entradas: Ninguna.
	Salidas: Añade al usuario al grupo solicitante
	"""
	global solicitudes
	if request.method == "POST":
		grupoS = request.form["grupoA"]

		solicitudes.append([grupoS, lastUser, 0, True])
		print("Estas son las solicitudes:")
		print("=================================")
		print(solicitudes)

	return redirect(url_for('procesoExitoso'))

@app.route("/EntrarGrupo", methods=["GET", "POST"])
def entrarGrupo():
	"""
	Función que permite asegurarse que un usuario entre a un grupo.
	Entradas: Ninguna.
	Salidas: Retorna la validación para poder entrar a un grupo en 
			 la aplicación.
	"""
	print(integrantes)
	return render_template ("entrargrupo.html", datos={"grupos":Grupos[contador3], "Grupos":len(Grupos),
													   "grupos1":Grupos_temporal[0], "grupos2":Grupos_temporal[1],
													   "grupos3":Grupos_temporal[2], "grupos4":Grupos_temporal[3],
													   "grupos5":Grupos_temporal[4], "grupos6":Grupos_temporal[5],
													   "grupos7":Grupos_temporal[6], "usuario":lastUser, 
													   "grupoA":ultimoGrupo[0], "grupo1":Grupo1, "grupo2":Grupo2, 
													   "grupo3":Grupo3, "grupo4":Grupo4, "grupo5":Grupo5, "grupo6":Grupo6, 
													   "grupo7":Grupo7, "gruposAparecer":Grupos})

@app.route("/ProcesoExitoso", methods=["GET", "POST"])
def procesoExitoso():
	"""
	Función que permite retornar la página del procedimiento exitoso.
	Entradas: Ninguna.
	Salidas: El proceso exitoso corroborado.
	"""
	return render_template("ProcesoExitoso.html", datos={"usuario":lastUser})

@app.route("/DecisionExitosa", methods=["GET", "POST"])
def decisionExitosa():
	"""
	Función que permite llevar al admin al la comprobación de la decisión exitosa.
	Entradas: Ninguna.
	Salidas: La página de corroboración.
	"""
	global solicitudes
	mensaje = "Felicidades {} has determinado una sabia desición sobre quien iba a entrar o entrará.".format(lastUser)
	solicitudes = []
	print(solicitudes)
	return render_template("DesicionExitosa.html", datos={"mensaje":mensaje})

@app.route("/Decision/<dato1>/<dato2>", methods=["GET", "POST"])
def decision(dato1, dato2):
	"""
	Función que permite determinar si un usuario entra o no al grupo.
	Entradas: Dos datos que corresponden 
	Salidas: El usuario aceptado o denegado
	"""
	global solicitudes, integrantes
	if request.method == "POST":
		novato = request.form["novato"]
		Respuesta = request.form["Desicion"]
		contador = 0
		while contador < len(solicitudes):
			if solicitudes[contador][0] == dato1 and solicitudes[contador][1] == dato2:
				if Respuesta == "si":
					solicitudes[contador][2] = solicitudes[contador][2] + 1
				else:
					solicitudes[contador][3] = False
					break
				if solicitudes[contador][2] == len(integrantes[contador]):
					integrantes[contador].insert(contador, novato)
					solicitudes = []
					break
				elif solicitudes[contador][3] == False:
					solicitudes = []
					break
			contador += 1

	return redirect(url_for('decisionExitosa'))

@app.route("/IntegranteVotación", methods=["GET", "POST"])
def integranteV():
	"""
	Función que permite redireccionar a la página de votación para
	una solicitud.
	Entradas: Ninguna.
	Salidas: La página para votar las solicitudes.
	"""
	global solicitudes, SOLICITUD
	return render_template("IntegranteVota.html", datos={"solicitud":len(SOLICITUD),
														 "Solicitud":SOLICITUD, 
														 "usuarios":USuario})

@app.route("/ActiveGruop", methods=["GET", "POST"])
def grupo_activo():
	"""
	Función que retorna la págino de los grupos activos del ususario
	Entradas: Ninguna.
	Salidas: Devuelve el grupo activo en el que está inmerso.
	"""
	global solicitudes, integrantes, lastUser, Grupos, SOLICITUD
	dia = datetime.date.today().day
	mes = datetime.date.today().month
	agno = datetime.date.today().year
	dia_de_laSemana = datetime.datetime(agno, mes, 1).weekday()

	calendario = Calendario(mes, dia_de_laSemana)
	print(calendario)
	print(solicitudes)

	solicitud = []
	for integrante in integrantes:
		for datoX in solicitudes:
			for group in Grupos:
				if lastUser in integrante and group == datoX[0] and datoX[3] == True:
					solicitud = datoX
					break
	print(solicitud)
	SOLICITUD = solicitud

	return render_template("grupoActivo.html", datos={"grupos":Grupos[contador3], "Grupos":len(Grupos),
													  "grupos1":Grupos_temporal[0], "grupos2":Grupos_temporal[1],
													  "grupos3":Grupos_temporal[2], "grupos4":Grupos_temporal[3],
													  "grupos5":Grupos_temporal[4], "grupos6":Grupos_temporal[5],
													  "grupos7":Grupos_temporal[6], "usuario":lastUser, 
													  "grupoA":ultimoGrupo[0], "calendario":calendario, "mes":mes,
													  "año":agno, "grupo1":Grupo1, "grupo2":Grupo2, "grupo3":Grupo3, 
													  "grupo4":Grupo4, "grupo5":Grupo5, "grupo6":Grupo6, "grupo7":Grupo7,
													  "dia":dia, "solicitud":len(solicitud), "EventosE":len(Eventos_a_votacion)})

@app.route("/MasGrupos", methods=["GET", "POST"])
def masGrupos():
	"""
	Función que permite mostrar más grupos de los que muestra principalmente para el usuario.
	Entradas: Ninguna.
	Salidas: Todos los grupos del usuario.
	"""
	return render_template("MasGrupos.html", datos={"grupos":Grupos, 
									                "Cgrupos":len(Grupos),
												    "usuario":lastUser})

# Eventos

@app.route("/EventosActivos", methods=["GET", "POST"])
def eventoActivo():
	"""
	Función que permite mostrar el día correspondiente a los eventos que hayan.
	Entradas: Ninguna.
	Salidas: Los eventos correspondientes al día.
	"""
	global eventos, descripcionEvento

	hayActividad = False

	if request.method == "POST":
		boton = request.form["algoDias"]
		if eventos != []:
			for dia in diaEvento:
				if dia == boton:
					for E in eventos:
						Cdia = diaEvento.index(dia)
						if E == eventos[Cdia]:
							EventoEnviar = E
							hayActividad = True
							diaActividad = dia
							mes = datetime.date.today().month
							agno = datetime.date.today().year
							descripcionEventoN = descripcionEvento[Cdia]
							print(descripcionEvento)
							return render_template("EventosActivos.html", datos={"eventos":eventos, "eventoE":EventoEnviar,
																				  "descripcion":descripcionEventoN, "dia":diaActividad,
																				  "grupos":Grupos[contador3], "Grupos":len(Grupos),
																				  "grupos1":Grupos_temporal[0], "grupos2":Grupos_temporal[1],
																				  "grupos3":Grupos_temporal[2], "grupos4":Grupos_temporal[3],
																				  "grupos5":Grupos_temporal[4], "grupos6":Grupos_temporal[5],
																				  "grupos7":Grupos_temporal[6], "usuario":lastUser, 
																				  "grupo1":Grupo1, "grupo2":Grupo2, "grupo3":Grupo3, 
																				  "grupo4":Grupo4, "grupo5":Grupo5, "grupo6":Grupo6, 
																				  "grupo7":Grupo7, "eventos1": Eventos_Temporal[0], 
																				  "eventos2":Eventos_Temporal[1], "eventos3":Eventos_Temporal[2],
																				  "eventos4":Eventos_Temporal[3], "eventos5":Eventos_Temporal[4],
																				  "eventos6":Eventos_Temporal[5], "eventos7":Eventos_Temporal[6],
																				  "eventos8":Eventos_Temporal[7], "Eventos":len(eventos), 
																				  "evento1":Evento1, "evento2":Evento2,"evento3":Evento3, 
																				  "evento4":Evento4, "evento5":Evento5, "evento6":Evento6, 
																				  "evento7":Evento7, "mes":mes, "año":agno, "EventoE":len(Eventos_a_votacion)})
	error = "Lo siento el evento tiene que estar creado para este día."
	return render_template("ErrorEA.html", datos={"error":error})

@app.route("/Eventos" , methods=["GET", "POST"])
def evento():
	"""
	Función que devuleve todo lo relacionado a la realización de un evento.
	Entradas: Ninguna.
	Salidas: La página de creación de eventos.
	"""
	dia = datetime.date.today().day
	mes = datetime.date.today().month
	agno = datetime.date.today().year
	dia_de_laSemana = datetime.datetime(agno, mes, 1).weekday()

	calendario = Calendario(mes, dia_de_laSemana)
	print(calendario)

	return render_template("Eventos.html", datos={"calendario":calendario, "usuario":lastUser})

@app.route("/Crear_Evento", methods=["GET", "POST"])
def crear_evento():
	"""
	Función que permite crear un evento para los grupos.
	Entradas: Ninguna.
	Salidas: El evento creado.
	"""
	global Evento1, Evento2, Evento3, Evento4, Evento5, Evento6, Evento7, Evento8, contador4, Eventos_a_votacion, descripcionEventoTemp, diaEventoTemp

	if request.method == "POST":
		event = request.form["CrearEvento"]
		description = request.form["CrearDescripcion"]
		diaE = request.form["diaE"]

	if event in eventos:
		error = "Lo sentimos el evento que trata de crear ya está registrado."
		return render_template("ErrorE2.html", datos={"error":error})
	elif len(event) > 12:
		error = "Lo sentimos el nombre de su evento debe ser menor a 13 cracteres"
		return render_template("ErrorE2.html", datos={"error":error})

	if len(eventos) == 0 and len(Evento1) == 0:
		Evento1.append(event)
	elif len(eventos) > 1 and len(Evento1) == 1 and len(Evento2) == 0:
		Evento2.append(event)
	elif len(eventos) > 2 and len(Evento1) == 1 and len(Evento2) == 1 and len(Evento3) == 0:
		Evento3.append(event)
	elif len(eventos) > 3 and len(Evento1) == 1 and len(Evento2) == 1 and len(Evento3) == 1 and len(Evento4) == 0:
		Evento4.append(event)
	elif len(eventos) > 4 and len(Evento1) == 1 and len(Evento2) == 1 and len(Evento3) == 1 and len(Evento4) == 1 and len(Evento5) == 0:
		Evento5.append(event)
	elif len(eventos) > 5 and len(Evento1) == 1 and len(Evento2) == 1 and len(Evento3) == 1 and len(Evento4) == 1 and len(Evento5) == 1 and len(Evento6) == 0:
		Evento6.append(event)
	elif len(eventos) > 6 and len(Evento1) == 1 and len(Evento2) == 1 and len(Evento3) == 1 and len(Evento4) == 1 and len(Evento5) == 1 and len(Evento6) == 1 and len(Evento7) == 0:
		Evento7.append(event)
	elif len(eventos) > 7 and len(Evento1) == 1 and len(Evento2) == 1 and len(Evento3) == 1 and len(Evento4) == 1 and len(Evento5) == 1 and len(Evento6) == 1 and len(Evento7) == 1 and len(Evento8) == 0:
		Evento8.append(event)

	Eventos_a_votacion.insert(0, event)
	descripcionEventoTemp.insert(0, description)
	lasEvento.insert(0, event)

	contador = 0
	while contador < len(diaEvento):
		if diaE[contador] == diaEvento[contador]:
			error = "Lo siento no puedes hacer un evento el mismo día que el otro."
			return render_template("ErrorDE.html", datos={"error":error})
		contador += 1

	diaEventoTemp.insert(0, diaE)

	contador = 0
	while contador < len(eventos):
		if event == eventos[contador]:
			contador4 = contador
		contador += 1

	return render_template("ExitoE.html", datos={"evento":lasEvento[0]})

@app.route("/Votación", methods=["GET", "POST"])
def votacion():
	"""
	Función que permite retornar un espacio de votación para los eventos.
	Entradas: Ninguna.
	Salidas: La página para poder votar el evento.
	"""
	return render_template("Votacion.html", datos={"eventos":Eventos_a_votacion, 
												   "Eventos":len(Eventos_a_votacion)})

@app.route("/VotacionEventos", methods=["GET", "POST"])
def votacion1():
	"""
	Función que permite guardar los votos de las personas en el evento.
	Entradas: Ninguna.
	Salidas: Los votos del evento.
	"""
	global votacionSi, votacionNo, eventos, descripcionEventoN, diaEvento
	if request.method == "POST":
		EventoSeleccionado = request.form["EVENTO"]
		Respuesta = request.form["Respuesta"]

		if Respuesta == "Si":
			votacionSi = votacionSi + 1
		elif Respuesta == "No":
			votacionNo = votacionNo + 1

		contador = 0
		while contador < len(integrantes):
			if votacionSi > len(integrantes[contador])//2 or votacionSi == len(integrantes[contador]):
				eventos.append(EventoSeleccionado)
				descripcionEvento.append(descripcionEventoTemp[contador])
				diaEvento.append(diaEventoTemp[contador])
				Eventos_a_votacion.remove(EventoSeleccionado)

				archivo = open("Listas_Eventos.txt", mode="a+")
				archivo.write(EventoSeleccionado + "\n")
				archivo.write(descripcionEventoTemp[contador] + "\n")
				archivo.write(diaEventoTemp[contador] + "\n")
				archivo.write("\n")
				archivo.close()

				mensaje = "La votación fue exitosa el evento {} ha sido colocado en la agenda del grupo".format(EventoSeleccionado)
				return render_template("Resultado.html", datos={"mensaje":mensaje})
			elif votacionNo == len(integrantes[contador])//2 or votacionNo == len(integrantes[contador]):
				Eventos_a_votacion.remove(EventoSeleccionado)
				mensaje = "Lo siento el evento fue sometido a votación, y ganó el no, por favor haga otro."
				return render_template("Resultado.html", datos={"mensaje":mensaje})
			contador += 1

		mensaje = "Tu voto ha sido registrado exitosamente "
		return render_template("Resultado.html", datos={"mensaje":mensaje})

@app.route("/MasEventos", methods=["GET", "POST"])
def masEventos():
	"""
	Funición que permite observar todos lo eventos que tenga el grupo.
	Entradas: Ninguna.
	Salidas: Todos los eventos.
	"""
	return render_template("MasEventos.html", datos={"eventos":eventos,
													 "Ceventos":len(eventos),
													 "usuario":lastUser})
# Mensajes

@app.route("/Mensajes", methods=["GET", "POST"])
def mensajes():
	"""
	Función que permite ver los mensajes que les llegan a los usuarios y también enviar mensajes.
	Entradas: Ninguna.
	Salidas: Página para ver los mensajes y enviarlos.
	"""
	global Mensajes, validacion

	autenticado = False
	mensajesPersona = []

	if request.method == "POST":
		if validacion:
			for mensaje in Mensajes:
				if mensaje[1] == lastUser:
					mensajesTemporales = [mensaje[0], mensaje[2]]
					autenticado = True
					mensajesPersona.append(mensajesTemporales)

	return render_template("Mensajes.html", datos={"mensajes":mensajesPersona,
												   "autenticado":autenticado})

@app.route("/ProcesarMensaje", methods=["GET", "POST"])
def ProcesarMensaje():
	"""
	Funición que permite procesar el mensaje que se quiera enviar al destinatrio.
	Entradas: Ninguna.
	Salidas: El mensaje enviado.
	"""
	global queMensaje, PersonaEnviada, Mensajes
	if request.method == "POST":
		if request.form["boton"] == "Enviar mensaje":
			quePersona = request.form["QuePersona"]
			MensajeEnviado = request.form["QueMensaje"]
			nuevoMensaje = [lastUser, quePersona, MensajeEnviado]
			Mensajes.append(nuevoMensaje)
			queMensaje = nuevoMensaje[2]
			PersonaEnviada = quePersona
			return redirect(url_for('mensajeExitoso'))	

@app.route("/MensajeExitoso", methods=["GET", "POST"])
def mensajeExitoso():
	"""
	Función que permite mostrarle al usuario que se envió su mesaje.
	Entradas: Ninguna.
	Salidas: Mensaje Exitoso.
	"""
	mensaje = "Gracias {} tu mensaje: '{}', ha sido enviado a {} ".format(lastUser, queMensaje, PersonaEnviada)
	return render_template("MensajeExitoso.html", datos={"mensaje":mensaje})

if __name__ == "__main__":
	app.run(debug= True) # De forma ya corregida//
