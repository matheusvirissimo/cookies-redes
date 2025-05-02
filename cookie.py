from flask import Flask, request, make_response

app = Flask(__name__) ## nome do site é a variável

@app.route("/") ## a primeira rota do site é essa
def homepage(): 
    return "teste"


@app.route("/criar_cookie")
def criar_cookie():
    resposta = make_response("Cookie foi criado") # pode retornar qualquer coisa dentro desse parâmetro
    resposta.set_cookie("username", "mavinca") # é um dicionário do Python
    return resposta

@app.route("/ver_cookie")
def ver_cookie(): 
    cookies = request.cookies # vem em formato de dicionário    
    return cookies

if __name__ == "__main__":
    app.run(debug=True)