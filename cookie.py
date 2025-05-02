from flask import Flask, request, make_response, render_template

app = Flask(__name__, template_folder="Template") ## nome do site é a variável

@app.route("/") ## a primeira rota do site é essa
def homepage(): 
    username = request.cookies.get("username")
    return render_template("index.html", username=username)


@app.route("/criar_cookie")
def criar_cookie():
    resposta = make_response("Cookie foi criado") # pode retornar qualquer coisa dentro desse parâmetro
    resposta.set_cookie("username", "mavinqueta", max_age=None) # é um dicionário do Python
    return resposta

@app.route("/ver_cookie")
def ver_cookie(): 
    cookies = request.cookies # vem em formato de dicionário    
    return cookies

@app.route("/deletar_cookie")
def deletar_cookie():
    resposta = make_response("Deletando cookie")
    resposta.set_cookie("username", "", expires=0)
    return resposta

if __name__ == "__main__":
    app.run(debug=True)