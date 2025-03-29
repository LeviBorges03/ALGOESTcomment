# Este código calcula o valor final de uma compra com base em diferentes faixas de desconto.
# Dependendo do valor da compra, é aplicado um desconto específico e o valor final é mostrado.

# Solicitando ao usuário o valor da compra em reais
valor = int(input("Insira o valor da compra"))  # A função input exibe uma mensagem e
                                              # aguarda a entrada do valor da compra.
                                              # O valor inserido é convertido para
                                              # um número inteiro usando a função int()
                                              # e armazenado na variável 'valor'.

# Calculando os descontos com base no valor da compra
descont10 = valor - valor * 0.1  # Calcula um desconto de 10% sobre o valor da compra.
                                 # Para isso, multiplica o valor por 0.1 (10%) e subtrai
                                 # esse valor do total da compra.

descont20 = valor - valor * 0.2  # Calcula um desconto de 20% sobre o valor da compra.
                                 # Multiplica o valor por 0.2 (20%) e subtrai esse valor
                                 # do total da compra.

descont25 = valor - valor * 0.25  # Calcula um desconto de 25% sobre o valor da compra.
                                   # Multiplica o valor por 0.25 (25%) e subtrai esse
                                   # valor do total da compra.

# Estrutura condicional para aplicar o desconto adequado conforme o valor da compra
if valor < 100:  # A instrução 'if' verifica se o valor da compra é menor que 100.
                 # Se a condição for verdadeira, o código dentro deste bloco será
                 # executado e o valor original será impresso sem desconto.
    print(valor)  # Exibe o valor da compra sem desconto, caso o valor seja menor que 100.

# Se a primeira condição não for verdadeira, verifica-se a condição do 'elif'
elif valor >= 100 and valor < 500:  # O 'elif' verifica se o valor da compra é maior ou
                                    # igual a 100 e menor que 500. Se for verdadeira,
                                    # o código dentro deste bloco será executado e o
                                    # valor com o desconto de 10% será mostrado.
    print(descont10)  # Exibe o valor com 10% de desconto aplicado, caso a compra esteja
                      # na faixa de 100 até 499.

# Se as duas condições anteriores não forem verdadeiras, verifica-se a próxima faixa de valores
elif valor >= 500 and valor < 1000:  # O 'elif' verifica se o valor da compra é maior ou
                                      # igual a 500 e menor que 1000. Se for verdadeira,
                                      # o código dentro deste bloco será executado e o
                                      # valor com o desconto de 20% será mostrado.
    print(descont20)  # Exibe o valor com 20% de desconto aplicado, caso a compra esteja
                      # na faixa de 500 até 999.

# Caso nenhuma das condições anteriores seja verdadeira (ou seja, valor >= 1000)
else:  # O 'else' é executado quando todas as condições anteriores (if e elif) não
       # foram verdadeiras. Neste caso, a compra tem um valor igual ou superior a 1000.
    print(descont25)  # Exibe o valor com 25% de desconto aplicado, caso a compra seja
                      # maior ou igual a 1000.

# Entrada de Dados:

# valor = int(input("Insira o valor da compra")): O programa solicita ao usuário que insira o valor da compra. A função input() coleta esse valor em formato de texto e, em seguida, a função int() converte esse valor em um número inteiro. O valor é armazenado na variável valor.

# Cálculo dos Descontos:

# descont10 = valor - valor * 0.1: O programa calcula o valor com 10% de desconto. Ele faz isso multiplicando o valor da compra por 0.1 (representando 10%), e subtraindo esse valor do valor original.

# descont20 = valor - valor * 0.2: O cálculo do desconto de 20% é feito da mesma forma, multiplicando o valor da compra por 0.2 (representando 20%).

# descont25 = valor - valor * 0.25: O cálculo do desconto de 25% segue a mesma lógica, multiplicando o valor da compra por 0.25 (representando 25%).

# Estrutura Condicional:

# if: A primeira condição if valor < 100: verifica se o valor da compra é inferior a 100. Se for verdade, o valor da compra é exibido sem nenhum desconto.

# elif: O primeiro elif verifica se o valor da compra está entre 100 e 499. Caso seja verdadeiro, o programa aplica o desconto de 10% e exibe o valor com desconto.

# elif: O segundo elif verifica se o valor da compra está entre 500 e 999. Se verdadeiro, o programa aplica o desconto de 20% e exibe o valor com desconto.

# else: O else é executado quando o valor da compra é 1000 ou mais. Nesse caso, o programa aplica o desconto de 25% e exibe o valor final com esse desconto.