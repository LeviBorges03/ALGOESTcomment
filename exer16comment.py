# SISTEMA DE CÁLCULO DE MÉDIA ESCOLAR
# Este programa solicita três notas de um aluno, calcula a média
# e informa se o aluno está aprovado, em recuperação ou reprovado.

# Solicita a primeira nota e converte o valor digitado para inteiro (número sem casas decimais)
nun1 = int(input("inserir nota 1"))  
# input() mostra o texto na tela e espera o usuário digitar algo.
# int() transforma o valor digitado (que vem como texto) em número inteiro para que possamos fazer cálculos.

# Solicita a segunda nota e converte para inteiro
nun2 = int(input("inserir nota 2"))  
# Mesmo processo da primeira nota: o valor digitado vira número inteiro.

# Solicita a terceira nota e converte para inteiro
nun3 = int(input("inserir nota 3"))  
# Repetimos para a terceira nota.

# Calcula a soma das três notas
soma = nun1 + nun2 + nun3  
# Aqui usamos o operador de adição (+) para somar as três notas digitadas.
# O resultado fica armazenado na variável 'soma'.

# Calcula a média das três notas
media = soma / 3  
# Usamos o operador de divisão (/) para dividir a soma por 3, que é o número total de notas.
# O valor resultante (a média) é armazenado na variável 'media'.

# Verificamos se a média é maior ou igual a 7
if media >= 7:  
    # O operador >= significa "maior ou igual a".
    # Se a média for 7 ou mais, o aluno está aprovado.
    print("Aprovado")  # Exibe mensagem de aprovação.

# Caso a média não seja maior ou igual a 7, o programa verifica se está entre 5 e 6.9
elif media >= 5 and media < 7:  
    # Aqui usamos o operador 'and' que exige que as duas condições sejam verdadeiras ao mesmo tempo.
    # Ou seja, a média deve ser maior ou igual a 5 E menor que 7.
    # Se for esse o caso, o aluno está em recuperação.
    print("Recuperação")  # Exibe mensagem de recuperação.

# Se nenhuma das condições acima for verdadeira, significa que a média é menor que 5
else:
    # Portanto, o aluno está reprovado.
    print("Reprovado")  # Exibe mensagem de reprovação.
