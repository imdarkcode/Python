"""
Utilizando a função format é possível concatenar
valores em um mesmo elemento, apenas passando os índices
do elemento
"""

texto = "abc"
inteiro = 12
decimal = 4.75
concatenacao = 'Texto:{0} Inteiro:{1} Decimal:{2}'.format(texto, inteiro, decimal) # O índice representa sua posição nos parenteses

print(concatenacao)