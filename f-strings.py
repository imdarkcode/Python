"""
Uilizando o f no inicio de uma string é possível
concatenar de uma forma mais simples
"""

nome = "João"
idade = 19

print(f"{nome} tem {idade} anos")

"""
Utilizando o sinal de .f é possível arredondar um valor
para uma quantidade de casas decimais específica
"""

valor = 5.784434676
print(f"4 casas: {valor:.4f}") # O número que vai antes do f indica a quantidde de casas
print(f"2 casas: {valor:.2f}")
print(f"Nenhuma casa: {valor:.0f}")

