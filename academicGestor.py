from flask import Flask,jsonify,render_template, request, url_for, flash, redirect
from procuraDocente import procuraDocentes

app = Flask(__name__)
app.config['SECRET_KEY'] = '9455214A428C8137B01669B6F7CD2AF198E24D29'

@app.route('/')
def raiz():
    return 'Hello World!'

@app.route('/rota2')
def rota2():
    return '<h1>Esta é a rota 2!</h1>'

@app.route('/docente/<string:nome>')
def docente(nome):
    return jsonify({'nome':nome})

@app.route('/template')
def index():
    return render_template('index.html')

@app.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        # title = request.form['title']
        content = request.form['content']

        if not content:
            flash('Title is required!')
        else:
            flash('Deu certo!')
            print('Deu certo!'+ content)
            listaDeDocentes = content.split(',')
            print(listaDeDocentes)
            procuraDocentes(listaDeDocentes)
            flash('Deu certo!'+ content)
            # conn = get_db_connection()
            # conn.execute('INSERT INTO posts (title, content) VALUES (?, ?)',
            #              (title, content))
            # conn.commit()
            # conn.close()
            # return redirect(url_for('index'))

    return render_template('create.html')


app.run(debug=True)