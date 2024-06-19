<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <h1>Portfólio digital de João Vítor</h1>
</head>
<body>

<img src="mgt/ft.jpg" alt="fotogit" style="display:block; margin:auto; width:50%;"/>

<h3> Orientador: Fabrício Galende Marques de Carvalho </h3>

<h3>Tecnologias utilizadas:</h3>
<ol>
	<li>Git</li>
	<li>GitHub</li>
	<li>HTML</li>
	<li>CSS</li>
	<li>Markdown</li>
	<li>Python</li>
	<li>JavaScript</li>
</ol>

<h1>Instalação do Python e Flask para a execução do portfólio</h1>

<h2>1. Instalando o Python</h2>
<p>Primeiro, você precisa instalar o Python em seu computador. Você pode baixar o instalador do Python no <a href="https://www.python.org/downloads/">site oficial do Python</a>. Siga as instruções de instalação fornecidas no site.</p>

<h2>2. Criando um ambiente virtual</h2>
<p>Após instalar o Python, abra o terminal ou prompt de comando e navegue até o diretório API. Em seguida, execute os seguintes comandos para criar e ativar um ambiente virtual:</p>

<pre>python -m venv myenv
myenv\Scripts\activate</pre>

<h2>3. Instalando o Flask</h2>
<p>Com o ambiente virtual ativado, você pode instalar o Flask usando o pip. Execute o seguinte comando:</p>
<code>pip install Flask</code>

<h2>4. Criando um aplicativo Flask</h2>
<p>Crie um arquivo chamado <code>app.py</code> no diretório do projeto e adicione o seguinte código:</p>

<pre>from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
return 'Olá, Flask!'

if __name__ == '__main__':
app.run(debug=True)
</pre>


<h2>5. Executando o servidor Flask</h2>
<p>Com o arquivo <code>app.py</code> criado, execute o seguinte comando para iniciar o servidor Flask:</p>

<code>python app.py</code>

<p>Agora você pode abrir um navegador da web e acessar <code>http://localhost:5000/</code> para ver o resultado.</p>

<p>Pronto! Você agora tem um servidor Flask em execução em seu ambiente virtual.</p>

</body>
</html>
