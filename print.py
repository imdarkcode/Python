"""
A função print permite mostrar um elemento na tela
"""

print(1234)

"""
É possível separar mostrar mais de um elemento
seprando eles por vírgula
"""

print(12, "abc")

""" 
Por padrão os elemento são separados por um espaço,
mas é possível mudar isso com o atributo "sep"
"""

print(12, "abc", sep="-")

"""
Por padrão o print sempre vai terminar com uma quebra de linha (\n),
mas é possível mudar isso com o atributo "end"
"""

print(1234, end="|")
print("abc")