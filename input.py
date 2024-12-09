"""
Utilizando a função input é possível solicitar que
o usuário digite um dado, por padrão o input sempre vai
receber um valor string
"""

nome = input("Digite o seu nome: ") # Nessa caso, irá salvar o valor que o usuário digitar na variável
print(f"O seu nome é {nome}")

"""
Para alterar o tipo de dado que o usuário irá inserir
é preciso converter o valor da variável
"""

valor_1 = int(input("Digite o primeior valor: ")) # A função int irá converter o valor antes de salvra na variável
valor_2 = int(input("Digite o segundo valor: "))
print(f"O resultado da soma será {valor_1 + valor_2}")

