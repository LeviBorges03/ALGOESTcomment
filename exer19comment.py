# CATEGORIZAÇÃO DE ANÚNCIOS BASEADO EM IDADE, GÊNERO E SE A PESSOA É ATLETA
# Este programa decide qual tipo de anúncio exibir para o usuário com base na sua idade, gênero e se ele é atleta.

# Solicita ao usuário que digite sua idade e converte a entrada para um número inteiro
idade = int(input("Digite sua idade: "))  
# input() solicita que o usuário insira sua idade.
# O valor digitado, que vem como texto, é convertido para inteiro usando int().
# Exemplo de entrada: 25, que será convertido para o número 25.

# Solicita ao usuário que digite seu gênero, converte para minúsculo e armazena na variável 'genero'
genero = input("Digite seu gênero (masculino/feminino): ").lower()  
# input() pede para o usuário digitar seu gênero.
# .lower() transforma qualquer entrada em letras minúsculas, garantindo que a comparação com 'masculino' ou 'feminino' seja precisa, independente de como o usuário digite (ex: 'Feminino' ou 'feminino').

# Solicita ao usuário se ele é atleta e converte a resposta para minúsculo
atleta = input("Você é atleta? (sim/não): ").lower()  
# input() pede para o usuário responder "sim" ou "não".
# .lower() converte a resposta para minúscula, garantindo que a comparação seja feita corretamente.

# Inicia a lógica de decisão com base na idade do usuário.
# Vamos verificar a faixa etária e determinar o tipo de anúncio a ser exibido.

# Caso o usuário tenha menos de 15 anos
if idade < 15:  
    # Se a idade for menor que 15, o anúncio será infantil.
    print("Anúncios infantis")  # Exibe mensagem informando que anúncios infantis serão mostrados.

# Caso o usuário tenha entre 15 e 21 anos, inclusive
elif 15 <= idade <= 21:  
    # Verifica se a idade está entre 15 e 21 anos, incluindo esses dois valores.
    
    # Se o gênero for feminino, exibe anúncios relacionados a maquiagem e moda feminina.
    if genero == "feminino":
        print("Anúncios de maquiagem e moda feminina")  # Exibe anúncios direcionados ao público feminino jovem.

    # Se o gênero for masculino e a pessoa for atleta, exibe anúncios de artigos esportivos.
    elif genero == "masculino" and atleta == "sim":  
        # A condição "and" significa que o usuário deve ser masculino E ser atleta.
        print("Anúncios de artigos esportivos")  # Exibe anúncios relacionados a esportes para homens atletas.

    # Caso não se enquadre nas condições acima, exibe anúncios de videogames.
    else:
        print("Anúncios de videogames")  # Exibe anúncios voltados para o público masculino não-atleta ou feminino não-específico.

# Caso o usuário tenha entre 22 e 32 anos
elif 22 <= idade <= 32:  
    # Verifica se a idade está entre 22 e 32 anos, inclusive.
    
    # Se o gênero for masculino e a pessoa for atleta, exibe anúncios de artigos esportivos.
    if genero == "masculino" and atleta == "sim":
        print("Anúncios de artigos esportivos")  # Exibe anúncios esportivos para homens atletas.
    
    # Se o gênero não for masculino e a pessoa não for atleta, exibe anúncios de livros, jardinagem e eletrodomésticos.
    elif genero != "masculino" and atleta == "não":
        print("Anúncios de livros, jardinagem e eletrodomésticos")  # Exibe anúncios voltados para o público feminino e não-atleta.

# Caso o usuário tenha entre 22 e 35 anos e seja do gênero feminino
elif 22 <= idade <= 35 and genero == "feminino":  
    # Verifica se a idade está entre 22 e 35 anos, inclusive, e se o gênero é feminino.
    print("Anúncios de artigos esportivos e itens de casa")  # Exibe anúncios que atendem ao público feminino, incluindo artigos esportivos e itens de casa.
