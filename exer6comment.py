
# ==============================
# VERIFICADOR DE MAIORIDADE
# ==============================

# SOLICITANDO A IDADE DO USUÁRIO
# A função input() pede que o usuário digite um número
# O valor digitado é recebido como texto (string), então usamos int() para converter para número inteiro
idade = int(input("Insira sua idade: "))

# ESTRUTURA CONDICIONAL PARA VERIFICAR A MAIORIDADE
# O comando if verifica se uma condição é verdadeira e executa um bloco de código se for

# PRIMEIRA CONDIÇÃO: VERIFICANDO SE O USUÁRIO É MENOR DE IDADE
# O operador "<" significa "menor que"
# Se a idade for menor que 18, a pessoa é considerada menor de idade
if idade < 18:
    print("Você é menor de idade.")  # Exibe a mensagem informando que a pessoa é menor de idade

# SEGUNDA CONDIÇÃO: VERIFICANDO SE O USUÁRIO É MAIOR DE IDADE
# O comando "else" significa "caso contrário" (ou seja, se a idade não for menor que 18, então é 18 ou mais)
else:
    print("Você é maior de idade.")  # Exibe a mensagem informando que a pessoa é maior de idade
```

### Explicação das estruturas:
# - input(): Solicita um valor do usuário e retorna como texto.
# - int(): Converte o valor de texto para número inteiro.
# - if: Avalia uma condição e executa um bloco de código se for verdadeira.
# - else: Executa um bloco de código caso a condição do `if` seja falsa.
# - print(): Exibe informações na tela.
