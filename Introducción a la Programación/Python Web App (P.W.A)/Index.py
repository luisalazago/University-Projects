from flask import Flask, render_template # Se importó la librería de FLask//

app= Flask(__name__)

@app.route("/") # Se usa esto para indicar cual es la ruta principal, este caso el registro o logueo para continuar//

def Home():
	return render_template("Home Page.html")

@app.route("/Help") # Se presenta los grupos de eventos para discutir sobre ellos y organizarlos de mejor manera//

def eventos():
	return "Help"

@app.route("/About")

def about():
	return render_template("About.html")

@app.route("/Register")

def register():
	return render_template("Register.html")

@app.route("/SoventNetwork")

def sovent():
	return render_template("Pagina principal.html")

if __name__ == "__main__":
	app.run(debug= True) # De forma ya corregida//
