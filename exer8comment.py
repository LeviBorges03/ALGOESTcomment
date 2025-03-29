# Este código realiza uma verificação simples de login, onde o usuário insere
# seu nome de usuário e senha. O programa valida se esses dados correspondem
# a um conjunto de valores predeterminados e exibe uma mensagem conforme o caso.

# Solicitando o nome de usuário ao usuário
usuario = input("Insira seu usuário")  # A função input exibe uma mensagem e espera
                                        # que o usuário insira um valor. Esse valor
                                        # será armazenado na variável 'usuario'.

# Solicitando a senha ao usuário
senha = input("Insira sua senha")  # Da mesma forma, a função input solicita e
                                    # armazena o valor inserido pelo usuário na
                                    # variável 'senha'.

# Condição para verificar se o usuário e a senha estão corretos
if usuario == "Levi" and senha == "1234":  # A instrução 'if' verifica se a condição
                                            # é verdadeira. Aqui estamos verificando
                                            # se o valor da variável 'usuario' é igual
                                            # a "Levi" E se o valor da variável 'senha'
                                            # é igual a "1234". Ambos os valores precisam
                                            # ser verdadeiros para que o bloco de código
                                            # dentro do 'if' seja executado.

    # Caso a condição seja verdadeira, ou seja, se o usuário e a senha estão corretos
    print(f"Bem vindo {usuario}!")  # A função 'print' exibe uma mensagem de boas-vindas.
                                     # A f-string é utilizada para incluir o nome do usuário
                                     # na mensagem (a variável 'usuario' será inserida
                                     # no lugar de {usuario}).

# Se a condição do 'if' não for verdadeira (ou seja, usuário ou senha incorretos)
else:
    # Caso o usuário ou a senha esteja errado, o bloco 'else' será executado
    print("Acesso negado!")  # A função 'print' exibe a mensagem "Acesso negado!"
                              # indicando que a autenticação falhou.

# Entrada do Usuário:

# usuario = input("Insira seu usuário"): Solicita que o usuário insira um nome de usuário. O que o usuário digitar será armazenado na variável usuario.

# senha = input("Insira sua senha"): Solicita que o usuário insira a senha. O que o usuário digitar será armazenado na variável senha.

# Estrutura Condicional:

# if usuario == "Levi" and senha == "1234"::

# A palavra-chave if é usada para testar uma condição. No caso, a condição é verificar se a variável usuario é igual a "Levi" e se a variável senha é igual a "1234". A palavra-chave and garante que ambas as condições sejam verdadeiras para o código dentro do bloco if ser executado.

# Se a condição for verdadeira (o nome de usuário e a senha estão corretos), o código dentro do bloco if será executado, e a mensagem de boas-vindas será exibida.

# Mensagem de Saída:

# print(f"Bem vindo {usuario}!"): Exibe uma mensagem de boas-vindas. O f antes das aspas indica que estamos utilizando uma f-string, o que permite inserir o valor de variáveis diretamente dentro da string. O valor de usuario será inserido no lugar de {usuario}.

# Bloco Else:

# else:: Se a condição do if não for verdadeira (ou seja, o nome de usuário ou a senha estão incorretos), o código dentro do bloco else será executado.

# print("Acesso negado!"): Exibe a mensagem de erro, indicando que o acesso foi negado.