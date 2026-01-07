EXERCICIOS = [
    # --- Capítulo 1: Fundamentos ---
    # Ensinado: print(), strings
    {
        "id": 1,
        "capitulo": 1,
        "titulo": "Cap. 1 - Ex. 1: Olá Mundo",
        "enunciado": "Use o comando <code>print()</code> para escrever a frase <strong>Olá, mundo!</strong> na tela (exatamente como está escrito).",
        "saida_esperada": "Olá, mundo!",
        "dica_validacao": "print"
    },
    {
        "id": 2,
        "capitulo": 1,
        "titulo": "Cap. 1 - Ex. 2: Sua Jornada",
        "enunciado": "Escreva um código que imprima a frase: <strong>Estou aprendendo Python</strong>",
        "saida_esperada": "Estou aprendendo Python",
        "dica_validacao": "print"
    },
    {
        "id": 3,
        "capitulo": 1,
        "titulo": "Cap. 1 - Ex. 3: Números",
        "enunciado": "O comando print também funciona com números. Imprima o ano atual: <strong>2026</strong>",
        "saida_esperada": "2026",
        "dica_validacao": "print"
    },

    # --- Capítulo 2: Variáveis e Tipos ---
    # Ensinado: variáveis, tipos (int, float, str), input()
    {
        "id": 4,
        "capitulo": 2,
        "titulo": "Cap. 2 - Ex. 1: Variáveis",
        "enunciado": "Crie uma variável chamada <code>curso</code> e atribua o texto <strong>\"Python\"</strong> a ela. Em seguida, imprima essa variável.",
        "saida_esperada": "Python",
        "dica_validacao": "curso"
    },
    {
        "id": 5,
        "capitulo": 2,
        "titulo": "Cap. 2 - Ex. 2: Tipos Numéricos",
        "enunciado": "Crie uma variável <code>nota</code> com o valor decimal <strong>9.5</strong> e imprima o <strong>tipo</strong> dessa variável usando <code>type()</code>.",
        "saida_esperada": "<class 'float'>",
        "dica_validacao": "type"
    },
    {
        "id": 6,
        "capitulo": 2,
        "titulo": "Cap. 2 - Ex. 3: Entrada de Dados",
        "enunciado": "Use a função <code>input()</code> para perguntar <strong>\"Qual o nome do curso?\"</strong>. O programa deve pedir o nome e depois imprimir o que foi digitado. <br><small>(Ao rodar, digite 'Codelingo' na caixa que aparecer)</small>",
        "saida_esperada": "Qual o nome do curso?\nCodelingo",
        "dica_validacao": "input"
    },

    # --- Capítulo 3: Strings ---
    # Ensinado: len, upper, lower, capitalize, count, fatiamento
    {
        "id": 7,
        "capitulo": 3,
        "titulo": "Cap. 3 - Ex. 1: Tamanho",
        "enunciado": "Use a função <code>len()</code> para descobrir e imprimir quantos caracteres tem a palavra <strong>\"Programação\"</strong>.",
        "saida_esperada": "11",
        "dica_validacao": "len"
    },
    {
        "id": 8,
        "capitulo": 3,
        "titulo": "Cap. 3 - Ex. 2: Maiúsculas",
        "enunciado": "Converta a string <strong>\"python\"</strong> para letras maiúsculas usando o método <code>.upper()</code> e imprima o resultado.",
        "saida_esperada": "PYTHON",
        "dica_validacao": "upper"
    },
    {
        "id": 9,
        "capitulo": 3,
        "titulo": "Cap. 3 - Ex. 3: Fatiamento",
        "enunciado": "Use fatiamento (slicing) para imprimir apenas as 3 primeiras letras da palavra <strong>\"Python\"</strong> (que são 'Pyt').",
        "saida_esperada": "Pyt",
        "dica_validacao": "["
    },

    # --- Capítulo 4: Operadores ---
    # Ensinado: +, -, *, /, %, **, >, <, >=, ==
    {
        "id": 10,
        "capitulo": 4,
        "titulo": "Cap. 4 - Ex. 1: Multiplicação",
        "enunciado": "Vamos calcular a área de um quadrado. Crie uma variável <code>lado</code> com valor <strong>5</strong> e imprima o resultado da multiplicação de <code>lado</code> por ele mesmo.",
        "saida_esperada": "25",
        "dica_validacao": "*"
    },
    {
        "id": 11,
        "capitulo": 4,
        "titulo": "Cap. 4 - Ex. 2: Resto da Divisão",
        "enunciado": "O operador <code>%</code> (módulo) retorna o resto de uma divisão. Imprima o resto da divisão de <strong>10</strong> por <strong>3</strong>.",
        "saida_esperada": "1",
        "dica_validacao": "%"
    },
    {
        "id": 12,
        "capitulo": 4,
        "titulo": "Cap. 4 - Ex. 3: Comparação",
        "enunciado": "Crie uma variável <code>idade</code> com valor <strong>20</strong>. Em seguida, imprima o resultado da comparação se idade é <strong>maior ou igual a 18</strong> (deve retornar True).",
        "saida_esperada": "True",
        "dica_validacao": ">="
    },

    # --- Capítulo 5: Condicionais ---
    # Ensinado: if, else, elif
    {
        "id": 13,
        "capitulo": 5,
        "titulo": "Cap. 5 - Ex. 1: Decisão Simples",
        "enunciado": "Crie uma variável <code>temperatura</code> com valor <strong>30</strong>. Escreva um <code>if</code> que verifique se a temperatura é maior que 25. Se for, imprima <strong>\"Calor\"</strong>.",
        "saida_esperada": "Calor",
        "dica_validacao": "if"
    },
    {
        "id": 14,
        "capitulo": 5,
        "titulo": "Cap. 5 - Ex. 2: Par ou Ímpar",
        "enunciado": "Crie uma variável <code>numero</code> com valor <strong>7</strong>. Use <code>if/else</code> para verificar se ele é par ou ímpar. Se o resto da divisão por 2 for 0 imprima \"Par\", senão imprima <strong>\"Ímpar\"</strong>.",
        "saida_esperada": "Ímpar",
        "dica_validacao": "else"
    },
    {
        "id": 15,
        "capitulo": 5,
        "titulo": "Cap. 5 - Ex. 3: Notas Escolares",
        "enunciado": "Crie uma variável <code>nota</code> com valor <strong>6</strong>. Use <code>if/elif/else</code>: Se nota >= 7 imprima \"Aprovado\"; Se nota >= 5 imprima <strong>\"Recuperação\"</strong>; Senão imprima \"Reprovado\".",
        "saida_esperada": "Recuperação",
        "dica_validacao": "elif"
    },

    # --- Capítulo 6: Laços de Repetição ---
    # Ensinado: while, for, range, break, continue
    {
        "id": 16,
        "capitulo": 6,
        "titulo": "Cap. 6 - Ex. 1: While",
        "enunciado": "Use um laço <code>while</code> para criar uma contagem regressiva. Comece com <code>contador = 5</code> e imprima o valor enquanto for maior que 0. Não esqueça de diminuir 1 a cada volta! (Saída esperada: 5, 4, 3, 2, 1 em linhas separadas)",
        "saida_esperada": "5\n4\n3\n2\n1",
        "dica_validacao": "while"
    },
    {
        "id": 17,
        "capitulo": 6,
        "titulo": "Cap. 6 - Ex. 2: For Range",
        "enunciado": "Use um laço <code>for</code> junto com a função <code>range()</code> para imprimir os números de <strong>0 a 4</strong>.",
        "saida_esperada": "0\n1\n2\n3\n4",
        "dica_validacao": "for"
    },
    {
        "id": 18,
        "capitulo": 6,
        "titulo": "Cap. 6 - Ex. 3: Interrompendo",
        "enunciado": "Faça um laço <code>for</code> de 0 a 10. Porém, se o número for igual a <strong>5</strong>, use o comando <code>break</code> para parar o laço. Imprima os números antes de parar (0 a 4).",
        "saida_esperada": "0\n1\n2\n3\n4",
        "dica_validacao": "break"
    },

    # --- Capítulo 7: Listas ---
    # Ensinado: lista[], append(), acesso[i]
    {
        "id": 19,
        "capitulo": 7,
        "titulo": "Cap. 7 - Ex. 1: Criando Listas",
        "enunciado": "Crie uma lista chamada <code>frutas</code> contendo <strong>\"Maçã\", \"Banana\", \"Uva\"</strong> (nessa ordem) e imprima a lista completa.",
        "saida_esperada": "['Maçã', 'Banana', 'Uva']",
        "dica_validacao": "["
    },
    {
        "id": 20,
        "capitulo": 7,
        "titulo": "Cap. 7 - Ex. 2: Adicionando Itens",
        "enunciado": "Dada a lista <code>numeros = [1, 2, 3]</code>, use o método <code>.append()</code> para adicionar o número <strong>4</strong> ao final dela. Imprima a lista atualizada.",
        "saida_esperada": "[1, 2, 3, 4]",
        "dica_validacao": "append"
    },
    {
        "id": 21,
        "capitulo": 7,
        "titulo": "Cap. 7 - Ex. 3: Acessando Itens",
        "enunciado": "Dada a lista <code>cores = [\"Azul\", \"Vermelho\", \"Verde\"]</code>, imprima apenas o <strong>segundo</strong> item da lista (lembre-se que o índice começa em 0).",
        "saida_esperada": "Vermelho",
        "dica_validacao": "["
    },

    # --- Capítulo 8: Tuplas ---
    # Ensinado: tupla(), imutabilidade, desempacotamento
    {
        "id": 22,
        "capitulo": 8,
        "titulo": "Cap. 8 - Ex. 1: Tuplas",
        "enunciado": "Crie uma tupla chamada <code>pontos</code> com os valores <strong>(10, 20)</strong> e imprima essa tupla.",
        "saida_esperada": "(10, 20)",
        "dica_validacao": "("
    },
    {
        "id": 23,
        "capitulo": 8,
        "titulo": "Cap. 8 - Ex. 2: Acessando Tuplas",
        "enunciado": "Dada a tupla <code>vogais = ('a', 'e', 'i', 'o', 'u')</code>, imprima o primeiro item.",
        "saida_esperada": "a",
        "dica_validacao": "["
    },
    {
        "id": 24,
        "capitulo": 8,
        "titulo": "Cap. 8 - Ex. 3: Desempacotamento",
        "enunciado": "Temos a tupla <code>dimensoes = (800, 600)</code>. Desempacote esses valores nas variáveis <code>largura</code> e <code>altura</code>. Em seguida, imprima largura e altura (pode ser um print pra cada ou juntos).",
        "saida_esperada": "800\n600", # Aceita prints separados que é mais simples
        "dica_validacao": "="
    },

    # --- Capítulo 9: Dicionários ---
    # Ensinado: {chave:valor}, acesso[chave], alteração
    {
        "id": 25,
        "capitulo": 9,
        "titulo": "Cap. 9 - Ex. 1: Dicionários",
        "enunciado": "Crie um dicionário chamado <code>pessoa</code> com as chaves: <strong>\"nome\": \"Ana\"</strong> e <strong>\"idade\": 30</strong>. Imprima o dicionário.",
        "saida_esperada": "{'nome': 'Ana', 'idade': 30}",
        "dica_validacao": "{"
    },
    {
        "id": 26,
        "capitulo": 9,
        "titulo": "Cap. 9 - Ex. 2: Acessando Valor",
        "enunciado": "Dado o dicionário <code>carro = {\"marca\": \"Ford\", \"modelo\": \"Ka\"}</code>, imprima apenas o valor da chave <strong>\"marca\"</strong>.",
        "saida_esperada": "Ford",
        "dica_validacao": "["
    },
    {
        "id": 27,
        "capitulo": 9,
        "titulo": "Cap. 9 - Ex. 3: Modificando",
        "enunciado": "Temos <code>produto = {\"nome\": \"Caneta\", \"preco\": 2.00}</code>. Altere o valor da chave <strong>\"preco\"</strong> para <strong>2.50</strong> e imprima o dicionário atualizado.",
        "saida_esperada": "{'nome': 'Caneta', 'preco': 2.5}", # Python pode imprimir 2.5 em vez de 2.50
        "dica_validacao": "="
    },

    # --- Capítulo 10: Funções ---
    # Ensinado: def, parametros, return
    {
        "id": 28,
        "capitulo": 10,
        "titulo": "Cap. 10 - Ex. 1: Criando Função",
        "enunciado": "Defina uma função chamada <code>diga_oi()</code> que apenas imprime <strong>\"Oi!\"</strong>. Em seguida, chame essa função.",
        "saida_esperada": "Oi!",
        "dica_validacao": "def"
    },
    {
        "id": 29,
        "capitulo": 10,
        "titulo": "Cap. 10 - Ex. 2: Parâmetros",
        "enunciado": "Crie uma função <code>saudacao(nome)</code> que receba um nome e imprima <strong>\"Olá, [nome]\"</strong> (concatenando). Chame a função passando <strong>\"Dev\"</strong> como parâmetro.",
        "saida_esperada": "Olá, Dev",
        "dica_validacao": "def"
    },
    {
        "id": 30,
        "capitulo": 10,
        "titulo": "Cap. 10 - Ex. 3: Retorno",
        "enunciado": "Crie uma função <code>soma(a, b)</code> que <strong>retorne</strong> (use return) a soma de dois números. Chame a função com <strong>3</strong> e <strong>4</strong> e imprima o resultado devolvido.",
        "saida_esperada": "7",
        "dica_validacao": "return"
    }
]

def buscar_exercicio_por_id(id_buscado):
    return next((ex for ex in EXERCICIOS if ex["id"] == id_buscado), None)

def buscar_exercicios_por_capitulo(capitulo_id):
    return [ex for ex in EXERCICIOS if ex["capitulo"] == capitulo_id]