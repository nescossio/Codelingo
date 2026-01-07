from flask import Flask, render_template, request, jsonify
import sqlite3
import os
from exercicios import EXERCICIOS, buscar_exercicio_por_id, buscar_exercicios_por_capitulo

app = Flask(__name__)

def conectar_db():
    return sqlite3.connect("database.db", check_same_thread=False)

def inicializar_db():
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS duvidas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            texto TEXT
        )
    """)
    conn.commit()
    conn.close()

# CHAMADA APÓS DEFINIR AS FUNÇÕES
inicializar_db()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/aulas")
def aulas():
    return render_template("aulas.html")

@app.route("/exercicios")
def exercicios():
    return render_template("exercicios.html")

@app.route("/api/exercicios")
def get_todos_exercicios():
    capitulo = request.args.get("capitulo")
    
    if capitulo:
        try:
            capitulo_id = int(capitulo)
            lista = buscar_exercicios_por_capitulo(capitulo_id)
        except ValueError:
            return jsonify({"error": "ID do capítulo inválido"}), 400
    else:
        lista = EXERCICIOS

    return jsonify([
        {"id": ex["id"], "titulo": ex["titulo"], "capitulo": ex["capitulo"]} 
        for ex in lista
    ])

@app.route("/api/exercicio/<int:id>")
def get_exercicio(id):
    exercicio = buscar_exercicio_por_id(id)
    if exercicio:
        return jsonify({
            "id": exercicio["id"],
            "titulo": exercicio["titulo"],
            "enunciado": exercicio["enunciado"],
            "total": len(EXERCICIOS)
        })
    return jsonify({"error": "Exercício não encontrado"}), 404

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
    dados = request.json
    saida_usuario = dados.get("saida_usuario", "").strip()
    codigo_usuario = dados.get("codigo_usuario", "")
    exercicio_id = dados.get("exercicio_id")

    exercicio = buscar_exercicio_por_id(exercicio_id)
    
    if not exercicio:
        return jsonify({"resultado": "Erro: Exercício não encontrado."})

    # 1. Validação da Saída (Output)
    saida_esperada = exercicio["saida_esperada"].strip()
    saida_usuario_norm = saida_usuario.replace("\r\n", "\n").strip()
    saida_esperada_norm = saida_esperada.replace("\r\n", "\n").strip()
    
    # Lógica flexível:
    # 1. Exato
    # 2. Contém (para casos com input prompt sujando o output)
    
    passou = False
    if saida_usuario_norm == saida_esperada_norm:
        passou = True
    elif saida_esperada_norm in saida_usuario_norm:
        # Se a resposta esperada está contida na saída do usuário, consideramos certo
        # (Útil para exercícios com input() que imprimem o prompt junto)
        passou = True

    if passou:
        
        # 2. Validação Estática (Opcional - verifica se usou o conceito pedido)
        dica = exercicio.get("dica_validacao")
        if dica and dica not in codigo_usuario:
             return jsonify({
                "resultado": f"A saída está correta, mas você precisa usar '{dica}' no seu código!",
                "sucesso": False
            })

        return jsonify({"resultado": "Correto! Parabéns.", "sucesso": True})
    
    return jsonify({
        "resultado": f"Resposta incorreta.\nEsperado: {saida_esperada}\nSeu resultado: {saida_usuario if saida_usuario else '(vazio)'}", 
        "sucesso": False
    })

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)

