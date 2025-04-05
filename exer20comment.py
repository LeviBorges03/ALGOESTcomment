# Este código verifica a idade do usuário, se ele é membro do clube ou se está acompanhado por um membro,
# e com base nessas informações, decide se o acesso ao clube será permitido e qual o valor do ingresso.

# Solicita ao usuário que informe sua idade e converte a entrada para um número inteiro (int)
idade = int(input("Informe sua idade: "))  
# input() exibe uma mensagem pedindo para o usuário digitar sua idade.
# A resposta vem como uma string, então usamos int() para converter essa string em um número inteiro (por exemplo, "25" se torna 25).

# Solicita ao usuário se ele é membro do clube. A resposta será convertida para minúscula para garantir consistência nas comparações.
membro = input("Você é membro do clube? (s/n): ").lower()  
# input() pede uma resposta "s" (sim) ou "n" (não).
# .lower() transforma a resposta para minúsculas, tornando a comparação insensível ao caso (exemplo: "S" ou "s" serão tratados igualmente).

# Solicita ao usuário se ele está acompanhado por um membro do clube. Também converte a resposta para minúscula.
acompanhado_por_membro = input("Você está acompanhado por um membro? (s/n): ").lower()  
# input() pede uma resposta "s" ou "n", e .lower() transforma a resposta em minúsculas para facilitar a comparação posterior.

# Início da verificação para decidir se o acesso será permitido com base na idade do usuário
if idade > 18:  
    # Se a idade do usuário for maior que 18 anos, a pessoa pode entrar no clube, mas ainda precisamos verificar se ela é membro ou se está acompanhada.
    
    if membro == 's':  
        # Se o usuário for membro do clube (membro == 's'), ele tem acesso completo ao clube sem restrições.
        print("Acesso permitido. Bem-vindo ao clube!")  
        # Exibe a mensagem confirmando que o acesso foi permitido e dá as boas-vindas ao clube.
    
    else:  # Caso o usuário não seja membro do clube (membro != 's'), verificamos se ele está acompanhado por um membro.
        if acompanhado_por_membro == 's':  
            # Se o usuário não for membro, mas estiver acompanhado por um membro (acompanhado_por_membro == 's'), ele pode entrar com o benefício de meia entrada.
            print("Acesso permitido. Você deve pagar meia entrada.")  
            # Exibe a mensagem informando que o acesso foi permitido, mas o ingresso será meia entrada devido à presença de um membro.
        
        else:  
            # Se o usuário não for membro e também não estiver acompanhado por um membro, ele deve pagar o ingresso completo.
            print("Acesso permitido. Você deve pagar o ingresso completo.")  
            # Exibe a mensagem informando que o acesso foi permitido, mas o ingresso será completo, já que ele não se encaixa em nenhuma das condições especiais.
            
else:  
    # Se a idade do usuário for 18 anos ou menos, ele não pode entrar no clube.
    print("Acesso negado. Você deve ter mais de 18 anos para entrar no clube.")  
    # Exibe a mensagem informando que o acesso foi negado devido à idade do usuário, que não cumpre o requisito mínimo de 18 anos.
