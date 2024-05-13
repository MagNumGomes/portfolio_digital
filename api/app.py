from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/hobbies')
def contato():
    return render_template('hobbies.html')


@app.route('/projetos')
def quem_somos():
    return render_template('projetos.html')

if __name__ == '__main__':
    app.run(debug=True)
