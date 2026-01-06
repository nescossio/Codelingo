EXERCICIOS = [
    {
        "id": 1,
        "titulo": "Exercício 1: Olá Mundo",
        "enunciado": "Escreva um código em Python que imprima <strong>Olá, Mundo!</strong>",
        "saida_esperada": "Olá, Mundo!",
        "dica_validacao": None
    },
    {
        "id": 2,
        "titulo": "Exercício 2: Matemática Básica",
        "enunciado": "Escreva um código que imprima o resultado da soma de <strong>10 + 5</strong>.",
        "saida_esperada": "15",
        "dica_validacao": "+"
    },
    {
        "id": 3,
        "titulo": "Exercício 3: Variáveis",
        "enunciado": "Crie uma variável chamada <code>nome</code> com o valor <strong>\"Codelingo\"</strong> e depois imprima essa variável.",
        "saida_esperada": "Codelingo",
        "dica_validacao": "nome"
    },
    {
        "id": 4,
        "titulo": "Exercício 4: Tipos de Dados",
        "enunciado": "Escreva um código que imprima o tipo (string, int, float) do número <strong>3.14</strong> usando a função <code>type()</code>.",
        "saida_esperada": "<class 'float'>",
        "dica_validacao": "type"
    },
    {
        "id": 5,
        "titulo": "Exercício 5: Operações com Strings",
        "enunciado": "Imprima a string <strong>\"python\"</strong> convertida para letras maiúsculas usando o método <code>.upper()</code>.",
        "saida_esperada": "PYTHON",
        "dica_validacao": "upper"
    },
    {
        "id": 6,
        "titulo": "Exercício 6: Concatenação",
        "enunciado": "Escreva um código que imprima a junção das palavras <strong>\"Code\"</strong> e <strong>\"Lingo\"</strong> (sem espaço entre elas).",
        "saida_esperada": "CodeLingo",
        "dica_validacao": "+"
    },
    {
        "id": 7,
        "titulo": "Exercício 7: Listas",
        "enunciado": "Crie uma lista contendo os números <strong>1, 2 e 3</strong> e imprima essa lista.",
        "saida_esperada": "[1, 2, 3]",
        "dica_validacao": "["
    },
    {
        "id": 8,
        "titulo": "Exercício 8: Acessando Listas",
        "enunciado": "Dada a lista <code>['A', 'B', 'C']</code>, imprima o primeiro item dessa lista.",
        "saida_esperada": "A",
        "dica_validacao": "["
    },
    {
        "id": 9,
        "titulo": "Exercício 9: Função Len",
        "enunciado": "Use a função <code>len()</code> para imprimir o tamanho da string <strong>\"Programação\"</strong>.",
        "saida_esperada": "11",
        "dica_validacao": "len"
    },
    {
        "id": 10,
        "titulo": "Exercício 10: Condicional Simples",
        "enunciado": "Escreva um <code>if</code> que verifique se <strong>10 é maior que 5</strong>. Se for, imprima <strong>\"Verdadeiro\"</strong>.",
        "saida_esperada": "Verdadeiro",
        "dica_validacao": "if"
    }
]

def buscar_exercicio_por_id(id_buscado):
    return next((ex for ex in EXERCICIOS if ex["id"] == id_buscado), None)