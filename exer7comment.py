# ====================================
# CALCULADORA SIMPLES COM QUATRO OPERAÇÕES
# ====================================

# SOLICITANDO DOIS NÚMEROS AO USUÁRIO
# A função input() pede que o usuário digite um número
# Como input() retorna um texto (string), usamos int() para converter para um número inteiro
num1 = int(input("Insira o primeiro número: "))
num2 = int(input("Insira o segundo número: "))

# SOLICITANDO A OPERAÇÃO DESEJADA
# Aqui, o usuário digita qual operação matemática deseja realizar
# Como a resposta será um texto, não precisa de conversão
opcao = input("Insira a operação desejada (soma, subtração, multiplicação, divisão): ")

# REALIZANDO OS CÁLCULOS DAS OPERAÇÕES
# Cada variável armazena o resultado de uma das quatro operações matemáticas possíveis
soma = num1 + num2  # Adição
sub = num1 - num2  # Subtração
mult = num1 * num2  # Multiplicação
div = num1 / num2  # Divisão (o resultado será um número decimal se necessário)

# ESTRUTURA CONDICIONAL PARA EXECUTAR A OPERAÇÃO ESCOLHIDA
# O comando if verifica qual operação o usuário escolheu e exibe o resultado correspondente

if opcao == "soma":  # Se o usuário digitou "soma", mostramos o resultado da soma
    print(f"Resultado: {soma}")

elif opcao == "subtração":  # Se o usuário digitou "subtração", mostramos o resultado da subtração
    print(f"Resultado: {sub}")

elif opcao == "multiplicação":  # Se o usuário digitou "multiplicação", mostramos o resultado da multiplicação
    print(f"Resultado: {mult}")

elif opcao == "divisão":  # Se o usuário digitou "divisão", mostramos o resultado da divisão
    print(f"Resultado: {div}")

else:  
    # Se o usuário digitou algo diferente das opções, exibimos uma mensagem de erro
    print("Operação inválida. Escolha entre: soma, subtração, multiplicação ou divisão.")
