from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def inicio():
    return render_template("formulario.html")


@app.route('/procesar', methods=['POST'])
def procesar():
    palabra = request.form.get("palabra")
    significado = request.form.get("significado")
    return render_template("mostrar.html", palabra=palabra, significado=significado)


if __name__ == "__main__":
    app.run( port=8088, debug=True)