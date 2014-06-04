from flask import Flask , render_template

class templates():
	def nombre_sitio(title):
		return render_template('hello.html',title=title)

