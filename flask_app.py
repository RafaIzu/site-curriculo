from flask import Flask, render_template 
app = Flask(__name__)

@app.route('/inicio')
@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/curriculo')
def pagina_curriculo():
    return render_template('curriculo.html')

@app.route('/contato')
def pagina_contato():
    return render_template('contato.html')


## Para rodar o projeto em desenvolvimento

if __name__ == '__main__':
    app.run(debug= True, host='0.0.0.0')