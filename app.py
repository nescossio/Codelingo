from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

def conectar_db():
    return sqlite3.connect("database.db")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/aulas")
def aulas():
    return render_template("aulas.html")

@app.route("/exercicios")
def exercicios():
    return render_template("exercicios.html")

@app.route("/duvidas", methods=["GET", "POST"])
def duvidas():
    if request.method == "POST":
        texto = request.form["duvida"]
        conn = conectar_db()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO duvidas (texto) VALUES (?)", (texto,))
        conn.commit()
        conn.close()
        return "Dúvida enviada com sucesso!"
    return render_template("duvidas.html")

@app.route("/verificar", methods=["POST"])
def verificar():
    resposta = request.json["resposta"]
    correta = "print('Olá, Mundo!')"

    if resposta.strip() == correta:
        return jsonify({"resultado": "Correto! Parabéns."})
    return jsonify({"resultado": "Resposta incorreta. Tente novamente."})

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)

