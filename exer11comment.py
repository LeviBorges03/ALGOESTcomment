# Este código permite que o usuário crie um nome de usuário e senha, com algumas verificações.
# O código valida se a senha tem pelo menos 8 caracteres e, depois, permite a verificação do nome de usuário e senha.

# Solicitando ao usuário um nome de usuário
usuario = input("Insira um nome de usuário.")  # A função 'input()' exibe uma mensagem para o usuário
                                               # e espera que ele insira um valor. O valor digitado
                                               # será armazenado na variável 'usuario'.

# Convertendo o nome de usuário para minúsculas para garantir que a comparação seja feita de forma consistente
usuario = str.lower(usuario)  # O método 'lower()' converte todos os caracteres do nome de usuário
                               # para minúsculas. Isso é útil para evitar problemas com letras maiúsculas
                               # e minúsculas na hora da comparação do nome de usuário posteriormente.

# Solicitando ao usuário que insira uma senha
senha = input("Insira uma senha com pelo menos 8 caractere.")  # A função 'input()' solicita que o usuário insira
                                                             # uma senha, que será armazenada na variável 'senha'.

# Verificando se a senha tem 8 ou mais caracteres
if len(senha) >= 8:  # A função 'len()' retorna o comprimento (número de caracteres) da senha. Aqui, estamos verificando
                     # se a senha tem 8 ou mais caracteres. Se a condição for verdadeira, o bloco abaixo é executado.
    print("Usuário e senha criados.")  # Exibe uma mensagem informando que o usuário e a senha foram criados com sucesso.

# Caso a senha seja menor que 8 caracteres, o código entra no 'else' e solicita uma nova senha
else:  # Caso a senha tenha menos de 8 caracteres, o programa executa o código dentro do bloco 'else'.
    print("Senha fraca")  # Exibe uma mensagem informando que a senha é fraca e não atende ao requisito de comprimento.

    # Solicitando ao usuário uma nova senha
    senha = input("Insira uma senha com pelo menos 8 caractere.")  # O programa solicita ao usuário uma nova senha.

    # Verificando se a nova senha tem 8 ou mais caracteres
    if len(senha) >= 8:  # Novamente, verifica se a nova senha tem 8 ou mais caracteres.
        print("Usuário e senha criados.")  # Se a nova senha for válida, a criação do usuário e senha é confirmada.
    else:  # Caso a nova senha ainda não atenda ao requisito de comprimento mínimo
        print("Senha fraca, você não tem salvação e eu não tenho while. Reinicie o sistema.")  # Exibe uma mensagem engraçada
                                                                                              # informando que o usuário falhou em fornecer uma senha
                                                                                              # válida duas vezes.

# Solicitando ao usuário o nome de usuário e senha para login
verificaUsuario = input("Insira seu usuário.")  # O programa solicita que o usuário insira seu nome de usuário novamente.
verificaSenha = input("Insira sua senha.")  # O programa solicita que o usuário insira sua senha.

# Verificando se o nome de usuário e a senha inseridos correspondem aos valores cadastrados
if usuario == verificaUsuario and senha == verificaSenha:  # Aqui, o código verifica se o nome de usuário e a senha
                                                           # fornecidos pelo usuário para login são iguais aos valores
                                                           # cadastrados anteriormente. Se ambos forem verdadeiros,
                                                           # o bloco abaixo é executado.
    print(f"Bem vindo, {usuario}!")  # Se a verificação for bem-sucedida, o programa exibe uma mensagem de boas-vindas,
                                     # incluindo o nome do usuário (a variável 'usuario' será inserida no lugar de {usuario}).

# Caso o nome de usuário ou a senha estejam incorretos, o acesso é negado
else:  # Se qualquer uma das condições (nome de usuário ou senha) não for verdadeira, o código executa o bloco 'else'.
    print("Acesso negado!")  # Exibe uma mensagem informando que o acesso foi negado, pois as credenciais estavam incorretas.




# Entrada de Dados:

# usuario = input("Insira um nome de usuário."): Solicita ao usuário que insira um nome de usuário. O valor digitado será armazenado na variável usuario.

# usuario = str.lower(usuario): Converte o nome de usuário para letras minúsculas, garantindo que a comparação com o nome de usuário posterior seja consistente, independentemente de maiúsculas ou minúsculas.

# senha = input("Insira uma senha com pelo menos 8 caractere."): Solicita ao usuário que insira uma senha. A senha inserida será armazenada na variável senha.

# Validação da Senha:

# O código verifica se a senha tem 8 ou mais caracteres usando if len(senha) >= 8. Caso a senha seja válida, o programa informa que o usuário e a senha foram criados.

# Se a senha for menor que 8 caracteres, o programa solicita uma nova senha. Se a segunda senha também não for válida, o programa exibe uma mensagem engraçada e sugere que o sistema seja reiniciado.

# Verificação de Login:

# Após a criação da conta, o código solicita ao usuário que insira o nome de usuário e senha novamente para fazer o login.

# O if compara o nome de usuário e senha fornecidos com os valores armazenados anteriormente. Se ambos forem válidos, o login é bem-sucedido e o programa exibe uma mensagem de boas-vindas. Caso contrário, exibe "Acesso negado".