"""
Para criar uma estrutura condicional em Python é
utilizado a função if, todo o código que estiver identado
abaixo do if será executado se a condição for verdadeira
"""

if (0 == 0):
    print("A condição é verdadeira")

"""
Para executar um comando caso a condição não
seja verdadeira é utilizado o else
"""

if (0 == 5):
    print("A condição é verdadeira")
else:
    print("A condição é falsa")

"""
Para criar mais de uma opção de condição
é utilizado o elif (else if)
"""

numero = int(input("Digite um número de 1 a 3: "))

if (numero == 1):
    print("Você digitou o número 1")
elif (numero == 2):
    print("Você digitou o número 2")
else:
    print("Você digitou o número 3")