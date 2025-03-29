
# ==============================
# VERIFICADOR DE NÚMERO POSITIVO, NEGATIVO OU ZERO
# ==============================

# SOLICITANDO UM NÚMERO DO USUÁRIO
# A função input() solicita que o usuário digite um número
# O valor digitado sempre é recebido como texto (string), por isso usamos int() para converter para um número inteiro
num = int(input("Insira um número: "))

# ESTRUTURA CONDICIONAL PARA VERIFICAR O TIPO DO NÚMERO
# O comando if verifica condições e executa um bloco de código se a condição for verdadeira

# PRIMEIRA CONDIÇÃO: VERIFICANDO SE O NÚMERO É POSITIVO
# O operador ">" significa "maior que"
# Se a condição num > 0 for verdadeira, significa que o número é maior que zero, ou seja, é positivo
if num > 0:
    print(f"O número {num} é positivo.")  # Exibe a mensagem informando que o número é positivo

# SEGUNDA CONDIÇÃO: VERIFICANDO SE O NÚMERO É NEGATIVO
# A palavra-chave "elif" significa "else if" (ou seja, outra condição alternativa)
# O operador "<" significa "menor que"
# Se num for menor que 0, significa que o número é negativo
elif num < 0:
    print(f"O número {num} é negativo.")  # Exibe a mensagem informando que o número é negativo

# TERCEIRA CONDIÇÃO: VERIFICANDO SE O NÚMERO É ZERO
# O comando "else" significa "caso nenhuma das condições anteriores seja verdadeira"
# Se o número não for maior que 0 e nem menor que 0, então ele só pode ser 0
else:
    print(f"O número {num} é zero.")  # Exibe a mensagem informando que o número é zero
```

### Explicação das estruturas:
# - input(): Solicita um valor do usuário e retorna como texto.
# - int(): Converte o valor de texto para número inteiro.
# - if Avalia uma condição e executa um bloco de código se a condição for verdadeira.
# - elif: Verifica outra condição caso a primeira seja falsa.
# - else: Executa um bloco de código caso nenhuma das condições anteriores seja verdadeira.
# - print(): Exibe informações na tela.
