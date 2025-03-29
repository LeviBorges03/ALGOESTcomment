# Este código recebe uma temperatura do usuário e, dependendo do valor inserido,
# ele classifica a temperatura em três categorias: frio, agradável ou quente.

# Solicitando ao usuário que insira a temperatura em graus Celsius.
temperatura = int(input("Insira a temperatura"))  # A função input exibe uma mensagem
                                                 # para o usuário e aguarda a entrada
                                                 # de dados. O valor inserido será
                                                 # convertido para um número inteiro
                                                 # usando a função int() e armazenado
                                                 # na variável 'temperatura'.

# Estrutura condicional para verificar em qual faixa de temperatura a entrada se encaixa
if temperatura < 20:  # A instrução 'if' verifica se a temperatura é menor que 20.
                       # Se for verdadeira, o código dentro deste bloco será executado.
    print("Está frio")  # Caso a temperatura seja menor que 20, o programa exibe a mensagem
                         # "Está frio" para o usuário.

# Caso a primeira condição não seja verdadeira (temperatura >= 20), vamos para a próxima condição
elif temperatura >= 20 and temperatura <= 26:  # 'elif' é uma abreviação para "else if",
                                               # ou seja, ele verifica uma nova condição
                                               # se a condição do 'if' anterior não foi
                                               # satisfeita. Aqui, verificamos se a
                                               # temperatura está entre 20 e 26, inclusive.
    print("Está agradável")  # Se a temperatura estiver nessa faixa, o programa exibe
                              # a mensagem "Está agradável" para o usuário.

# Caso nenhuma das condições anteriores seja verdadeira (ou seja, temperatura > 26)
else:  # O 'else' é uma instrução que executa o bloco de código abaixo dele caso
       # todas as condições anteriores (if e elif) não sejam verdadeiras.
    print("Está quente")  # Caso a temperatura seja maior que 26, o programa exibe
                          # a mensagem "Está quente" para o usuário.

# Entrada de Dados:

# temperatura = int(input("Insira a temperatura")): O programa solicita que o usuário insira a temperatura. A função input() recebe a entrada do usuário em formato de texto, que é convertida para um número inteiro com a função int(), e o valor é armazenado na variável temperatura.

# Estruturas Condicionais:

# if: A primeira condição if temperatura < 20: verifica se a temperatura inserida pelo usuário é menor que 20. Se for verdadeira, o programa executa o bloco de código dentro do if, que é a impressão de "Está frio".

# elif: Se a primeira condição não for verdadeira (ou seja, a temperatura não for menor que 20), o programa verifica a condição do elif. A expressão temperatura >= 20 and temperatura <= 26 testa se a temperatura está entre 20 e 26 (inclusive). Se for verdadeira, ele executa o código dentro do bloco elif, que imprime "Está agradável".

# else: Se nenhuma das condições anteriores for verdadeira (ou seja, a temperatura é maior que 26), o bloco else será executado, e o programa exibirá "Está quente".