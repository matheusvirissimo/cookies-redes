from flask import Flask, request, make_response, render_template, session
from datetime import datetime
import time, string, random, json

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
    criacao_cookie = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    referencia = request.headers.get("Referer")
    idioma = request.headers.get("Accept-Language")
    timestamp = str(time.time())

    #cookie em dicionário para compactar

    dados_cookies = {
        "nome_salvo": nome_usuario,
        "id_sessao": id_sessao,
        "timestamp": timestamp,
        "criacao_cookie": criacao_cookie,
        "referencia": referencia,
        "idioma": idioma,
    }

    dados_compactados = json.dumps(dados_cookies)

    # cookie
    resposta = make_response("Cookie foi criado") # pode retornar qualquer coisa dentro desse parâmetro
    resposta.set_cookie("cookie_temporário", "tempo de 30 segundos", max_age=10)
    resposta.set_cookie("info_usuario", dados_compactados)

    return resposta

@app.route("/ver_cookie")
def ver_cookie(): 
    cookies = request.cookies.get("info_usuario") # vem em formato de dicionário   
    dados = json.loads(cookies)

    return render_template("view_cookie.html", dados=dados)

@app.route("/deletar_cookie")
def deletar_cookie():
    resposta = make_response("Deletando cookie")
    resposta.set_cookie("info_usuario", "", expires=0)
    session.clear()
    return resposta

if __name__ == "__main__":
    app.run(debug=True)
