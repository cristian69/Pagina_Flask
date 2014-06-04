from flask import Flask,url_for
from flask import render_template
import servicios 


app = Flask(__name__)


@app.route('/')#define todo su esqueleto de vistas

def holapython():
	return render_template("pagina.html")

@app.route('/php')

def php():
	return '<h1>servidor php</h1>'

@app.route('/usuario/<username>')
 
def usuario(username):
 	return 'User %s' % username

@app.route('/sitio')
@app.route('/sitio/<title>')

def sitio(title):
	return servicios.nombre_sitio(title)

	



if __name__ == '__main__':
	app.run(host='192.168.0.76',debug=True)