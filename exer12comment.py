# Este código verifica o saldo de uma conta bancária para determinar se a conta está ativa ou desativada.
# Se o saldo for positivo, a conta está ativa; caso contrário, a conta é desativada.

# Inicializando uma variável de controle chamada 'acesso' que indica se a conta está ativa ou não.
acesso = True  # A variável 'acesso' é inicialmente definida como 'True', o que significa que a conta está ativa.
               # Se o saldo for negativo ou zero, essa variável será alterada para 'False' mais adiante.

# Solicitando ao usuário o saldo da conta e armazenando esse valor na variável 'saldo'.
saldo = int(input("Insira o saldo dessa conta."))  # A função 'input()' solicita que o usuário insira o saldo da conta.
                                                  # O valor inserido é convertido para inteiro pela função 'int()'
                                                  # e armazenado na variável 'saldo'.

# Verificando se o saldo é maior que zero
if saldo > 0:  # A estrutura condicional 'if' verifica se o valor da variável 'saldo' é maior que zero.
               # Se o saldo for maior que zero, o código dentro do bloco 'if' será executado.
    print("Conta ativa.")  # Se o saldo for positivo, imprime "Conta ativa", indicando que a conta está em funcionamento.

# Caso o saldo não seja maior que zero (saldo menor ou igual a zero), o código entra no 'else'
else:  # O 'else' é executado quando a condição do 'if' (saldo > 0) não é verdadeira. Ou seja, o saldo é zero ou negativo.
    acesso = False  # Se o saldo for menor ou igual a zero, a variável 'acesso' é definida como 'False',
                     # indicando que a conta não está ativa.
    print("Conta desativada.")  # Exibe a mensagem "Conta desativada", informando que a conta foi desativada devido ao saldo.



# Variável de Controle:

# acesso = True: A variável acesso é inicializada com o valor True, indicando que, por padrão, a conta começa como ativa. Caso o saldo seja negativo ou zero, essa variável será alterada para False para indicar que a conta está desativada.

# Entrada de Dados:

# saldo = int(input("Insira o saldo dessa conta.")): O programa pede ao usuário para inserir o saldo da conta. A função input() coleta essa informação como uma string (texto) e a função int() converte o valor para um número inteiro, armazenando-o na variável saldo.

# Estrutura Condicional (Verificação de Saldo):

# if saldo > 0:: O if verifica se o saldo é maior que zero. Caso o saldo seja positivo, a conta é considerada ativa e a mensagem "Conta ativa." é exibida.

# else:: Caso a condição do if não seja satisfeita (ou seja, o saldo é zero ou negativo), o bloco else é executado. Nesse caso, o acesso à conta é desativado, a variável acesso é alterada para False e a mensagem "Conta desativada." é exibida.