from flask import(
    Flask,
    render_template,
)

app = Flask(__name__)

@app.route('/home')
def index ():
    return render_template('index.html')

@app.route('/contacto')
def indexContacto():
    return render_template('contacto.html')


