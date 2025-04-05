# SISTEMA DE CADASTRO DE ALUNOS - VERIFICAÇÃO DE IDADE MÍNIMA
# Este código solicita os dados de um estudante (nome, idade e turma),
# verifica se ele tem idade suficiente para estudar na escola (mínimo de 6 anos)
# e exibe uma mensagem de cadastro bem-sucedido ou não.

# Solicita o nome do estudante e armazena na variável 'aluno'
aluno = input("insira seu nome ESTUDANTE:")  # A função input() mostra essa mensagem na tela e espera o usuário digitar.
                                             # O texto digitado será armazenado como string (texto) na variável 'aluno'.

# Solicita a idade do estudante e armazena como número inteiro na variável 'idade'
idade = int(input("insira sua idade ESTUDANTE:"))  # input() sempre retorna texto, por isso usamos int() para converter em número inteiro.
                                                   # Assim, podemos comparar a idade numericamente depois.

# Solicita a turma do estudante e armazena na variável 'turma'
turma = input("insira sua turma ESTUDANTE:")  # Mais uma vez, usamos input() para receber uma informação do usuário,
                                              # agora sobre a turma que ele faz parte (ex: "1A", "2B", etc.).

# Agora vamos verificar se o estudante tem idade suficiente para se cadastrar
if idade >= 6:  # A estrutura if verifica se a idade digitada é maior ou igual a 6.
                # Se for verdadeiro, o código dentro desse bloco será executado.
    print(f"Aluno cadastrado com sucesso: {aluno}, {idade}, {turma}.")  
    # Se o aluno tem 6 anos ou mais, essa mensagem aparece informando que ele foi cadastrado.
    # Usamos f-strings para inserir o nome, idade e turma dentro do texto de forma dinâmica.

else:  # Caso o if não seja verdadeiro (ou seja, idade menor que 6), o programa executa o else.
    print(f"Aluno nao tem pra estudar conosco: {aluno}, {idade}, {turma}.")  
    # Aqui o programa informa que o aluno é muito novo para estudar na escola.
    # A f-string também é usada para mostrar os dados digitados.
