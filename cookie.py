from flask import Flask, request, make_response, render_template, session
from datetime import datetime
import time, string, random

app = Flask(__name__, template_folder="Template") ## nome do site é a variável
app.secret_key = "chave"

def criar_id(n):
    caracteres = string.ascii_letters + string.digits  # letras maiúsculas, minúsculas e números
    id_sessao = ''.join(random.choice(caracteres) for _ in range(n))
    return id_sessao


@app.route("/") ## a primeira rota do site é essa
def homepage(): 
    username = request.cookies.get("username")
    return render_template("homepage.html", username=username)


@app.route("/criar_cookie", methods=["POST"])
def criar_cookie():
    session["teste"] = "teste"

    # dados
    nome_usuario = request.form["nome"]
    id_sessao = criar_id(15)
    criacao_cookie = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    referencia = request.headers.get("Referer")
    idioma = request.headers.get("Accept-Language")
    timestamp = str(time.time())


    # cookie
    resposta = make_response("Cookie foi criado") # pode retornar qualquer coisa dentro desse parâmetro
    resposta.set_cookie("cookie temporário", "tempo de 30 segundos", max_age=10)
    resposta.set_cookie("usuario", nome_usuario, max_age=None) # é um dicionário do Python
    resposta.set_cookie("id_sessao", id_sessao)
    resposta.set_cookie("criacao_cookie", criacao_cookie)
    resposta.set_cookie("referencia", referencia)
    resposta.set_cookie("idioma", idioma)
    resposta.set_cookie("timestamp", timestamp)
    return resposta

@app.route("/ver_cookie")
def ver_cookie(): 
    cookies = request.cookies # vem em formato de dicionário   

    dados = {
        "nome_salvo": cookies.get("usuario"),
        "id_sessao": cookies.get("id_sessao"),
        "criacao_cookie": cookies.get("criacao_cookie"), 
        "referencia": cookies.get("referencia"),
        "idioma": cookies.get("idioma"),
        "timestamp": cookies.get("timestamp")
    }

    return render_template("view_cookie.html", dados=dados)

@app.route("/deletar_cookie")
def deletar_cookie():
    resposta = make_response("Deletando cookie")
    resposta.set_cookie("usuario", "", expires=0)
    session.clear()
    return resposta

if __name__ == "__main__":
    app.run(debug=True)
