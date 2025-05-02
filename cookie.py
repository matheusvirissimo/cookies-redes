from flask import Flask, request, make_response

app = Flask(__name__) ## nome do site é a variável

@app.route("/") ## a primeira rota do site é essa
def homepage(): 
    return "teste"



if __name__ == "__main__":
    app.run(debug=True)