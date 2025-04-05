# SISTEMA DE CÁLCULO DE VALOR TOTAL DE COMPRA COM DESCONTO
# Este programa pede o nome de um produto, a quantidade e o preço unitário.
# Depois calcula o valor total da compra.
# Se o valor total for igual ou maior que 100 reais, aplica um desconto de 5%.

# Solicita o nome do produto e armazena em uma variável chamada 'nome'
nome = str(input("digitar o nome do produto"))  # A função input() exibe o texto na tela e espera o usuário digitar algo.
                                                # str() garante que o valor será tratado como texto (string), embora o input já retorne string por padrão.
                                                # Esse valor será usado só para exibir no final.

# Solicita a quantidade desejada do produto e armazena como número inteiro na variável 'qaunt'
qaunt = int(input("digitar a quantidade desejada do poduto"))  # input() pega o texto digitado e int() converte para número inteiro.
                                                                # Isso é importante para poder fazer cálculos depois (ex: 2, 10, 50 produtos...).

# Solicita o valor unitário do produto e armazena como número decimal (float) na variável 'preco'
preco = float(input("digitar o valor unitario do produto"))  # input() pega o texto digitado e float() converte para número com casas decimais.
                                                             # Ex: R$ 3.50, R$ 12.99... o tipo float permite esse tipo de valor.

# Calcula o valor total da compra multiplicando quantidade x preço
valor = qaunt * preco  # Aqui multiplicamos o número de unidades do produto pelo preço de cada unidade.
                       # Exemplo: 3 unidades de R$ 10,00 = valor total de R$ 30,00.
                       # O resultado fica armazenado na variável 'valor'.

# Verifica se o valor total da compra é maior ou igual a R$ 100,00 para aplicar desconto
if valor >= 100:  # Essa estrutura if avalia a condição: o valor total é maior ou igual a 100?
                  # Se for verdadeiro, o cliente receberá desconto.
    
    desconto = valor * 0.05  # Calculamos o valor do desconto, que é 5% do valor total (0.05 = 5/100).
                             # Por exemplo, se a compra deu R$ 200, o desconto será R$ 10.

    print(f"Parabens vc recebeu 5% de desconto o valor total é: {nome} --> {desconto}")  
    # Exibe a mensagem de parabéns, mostrando o nome do produto e o valor do desconto.
    # f"" é uma f-string, usada para inserir variáveis dentro do texto automaticamente.

else:  # Se a condição do if não for verdadeira (ou seja, valor < 100), este bloco será executado.
    
    print(f"Parabens sua compra foi realizada com sucesso o valor total é: {valor}")  
    # Exibe a mensagem confirmando a compra e mostra o valor total sem desconto.
