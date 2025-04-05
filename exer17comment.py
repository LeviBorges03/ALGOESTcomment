# VERIFICADOR DE MAIORIDADE
# Este programa solicita o ano de nascimento da pessoa, calcula sua idade
# e informa se ela é maior de idade (18 anos ou mais) ou não.

# Solicita o ano de nascimento do usuário
ano_nascimento = int(input("Insira o ano de nascimento: "))  
# A função input() mostra a mensagem entre aspas e espera o usuário digitar algo.
# Tudo que o usuário digita com input() vem como texto (string), então usamos int() para converter esse texto em número inteiro.
# O valor será armazenado na variável 'ano_nascimento' para usarmos no cálculo da idade.

# Calcula a idade subtraindo o ano de nascimento do ano atual (2025)
idade = 2025 - ano_nascimento  
# Aqui fazemos a conta: ano atual menos o ano que o usuário nasceu.
# Exemplo: se ele nasceu em 2000, 2025 - 2000 = 25 anos.
# O resultado é guardado na variável 'idade' para ser usado na verificação e na mensagem.

# Verifica se a idade é maior ou igual a 18
if idade >= 18:  
    # if é uma estrutura condicional que executa um bloco de código apenas se a condição for verdadeira.
    # O operador >= significa "maior ou igual a".
    # Se a idade for 18 ou mais, isso indica que a pessoa é maior de idade.

    print(f"Você tem {idade} anos. É maior de idade.")  
    # print() exibe a mensagem na tela.
    # f"" é uma f-string, que permite inserir valores de variáveis diretamente no texto usando {chaves}.
    # Ex: Se a idade for 20, o resultado será: "Você tem 20 anos. É maior de idade."

else:  
    # else é o "caso contrário" do if.
    # Se a condição do if não for verdadeira (ou seja, se idade < 18), o código dentro do else será executado.

    print(f"Você tem {idade} anos. Não é maior de idade.")  
    # Exibe a mensagem dizendo que a pessoa ainda não é maior de idade.
    # A idade aparece na frase com a mesma lógica explicada acima.
