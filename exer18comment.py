# CÁLCULO DE SALÁRIO COM HORAS EXTRAS
# Este programa solicita o salário base de um trabalhador e o número de horas extras trabalhadas.
# Depois calcula o valor adicional das horas extras e soma ao salário base, mostrando tudo detalhado.

# Solicita ao usuário que digite o salário base (sem horas extras) e armazena na variável 'salario_base'
salario_base = float(input("Digite o salário base: R$ "))  
# input() exibe a mensagem e espera o usuário digitar.
# float() converte o valor digitado (que é texto por padrão) em número decimal (com vírgulas).
# Exemplo: R$ 2000.00 ou R$ 1850.75

# Solicita o número de horas extras que o funcionário trabalhou
horas_extras = int(input("Digite o número de horas extras trabalhadas: "))  
# int() converte o valor digitado em número inteiro (sem vírgula), porque horas são contadas como números inteiros.
# Exemplo: 5 horas extras

# Define o valor fixo pago por cada hora extra
valor_hora_extra = 23.10  
# Aqui atribuímos um valor fixo de R$ 23,10 por cada hora extra trabalhada.
# Esse valor pode mudar conforme o salário ou acordo de trabalho, mas está fixo neste exemplo.

# Calcula o total a receber só pelas horas extras
total_horas_extras = horas_extras * valor_hora_extra  
# Multiplicamos o número de horas extras pelo valor de cada uma para saber quanto será pago no total por elas.
# Exemplo: 5 horas * R$ 23,10 = R$ 115,50

# Soma o salário base com o valor total das horas extras para obter o salário total do mês
salario_total = salario_base + total_horas_extras  
# Aqui somamos o salário fixo com o valor das horas extras para saber quanto o funcionário irá receber no total.

# Exibe o salário base digitado
print(f"Salário base: R$ {salario_base}")  
# f"" é uma f-string, permite colocar variáveis dentro do texto entre chaves { }.
# Mostra quanto era o salário sem considerar horas extras.

# Exibe quantas horas extras foram trabalhadas
print(f"Total de horas extras: {horas_extras} horas")  
# Mostra na tela quantas horas extras foram informadas.

# Exibe o valor total que será recebido só pelas horas extras
print(f"Valor total das horas extras: R$ {total_horas_extras}")  
# Mostra o resultado do cálculo: valor das horas extras.

# Exibe o salário total, que é a soma do salário base com as horas extras
print(f"Salário total (com horas extras): R$ {salario_total}")  
# Mostra o valor final que o trabalhador vai receber.

