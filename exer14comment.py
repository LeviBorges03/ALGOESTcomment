# SISTEMA DE LOGIN SIMPLES - VERIFICAÇÃO DE USUÁRIO E SENHA
# Este programa simula um sistema de login.
# Ele verifica se o nome de usuário e a senha digitados são iguais aos armazenados.
# Se ambos estiverem corretos, o login é feito com sucesso.
# Caso contrário, ele informa se o erro está no nome de usuário, na senha, ou em ambos.

# Armazenamos o nome de usuário correto esperado para o login
usuarioArmazenado = "admin"  # Aqui criamos uma variável chamada 'usuarioArmazenado' e guardamos o texto "admin".
                             # Esse é o nome de usuário que será considerado correto no sistema.
                             # Se o usuário digitar esse nome, estará certo.

# Armazenamos a senha correta esperada para o login
senhaArmazenada = "1234"  # Aqui criamos outra variável, agora chamada 'senhaArmazenada', com o valor "1234".
                          # Essa será a senha correta. Ela será comparada com a senha que o usuário digitar.

# Solicitamos ao usuário que digite o nome de usuário
usuario = input("Insira o nome de usuario: ")  # Usamos a função input() para pedir ao usuário que digite o nome de usuário.
                                               # O texto digitado será armazenado na variável 'usuario'.

# Solicitamos ao usuário que digite a senha
senha = input("Insira a senha: ")  # Novamente usamos input() para pedir a senha.
                                   # O valor digitado será armazenado na variável 'senha'.

# Verificamos se o nome de usuário e a senha estão corretos ao mesmo tempo
if usuario == usuarioArmazenado and senha == senhaArmazenada:
    # Esse if usa duas comparações com o operador 'and' (E lógico).
    # Significa que só será verdadeiro se as duas comparações forem verdadeiras ao mesmo tempo:
    # 1. O nome de usuário digitado deve ser igual ao armazenado
    # 2. A senha digitada deve ser igual à armazenada
    print("Login realizado com sucesso!")  # Se as duas informações estiverem certas, o login é aceito e mostramos essa mensagem.

# Se o nome ou a senha estiverem errados, o código entra no else
else:
    # Dentro do else, fazemos duas verificações separadas:
    
    if usuario != usuarioArmazenado:
        # Aqui usamos '!=' que significa "diferente de".
        # Verificamos se o nome de usuário digitado é diferente do correto.
        print("Nome de usuario incorreto!")  # Se for diferente, mostramos esta mensagem.

    if senha != senhaArmazenada:
        # Agora verificamos se a senha digitada é diferente da senha correta.
        print("Senha incorreta!")  # Se for diferente, mostramos esta mensagem.
