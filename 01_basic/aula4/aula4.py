"""
    Tipos de dados
    str - string - textos 'Assim' "Assim"
    int - integer - 123456 0 -10 -20 -50 -60 -15000 1500
    float - real/ponto flutuante - 10.50 1.5 -10.10 -50.93 0.0
    bool - booleano/lógico - True/False 10 == 10
"""

print("Assim", type("Assim"))  # <class 'str'>
print(123456, type(123456))  # <class 'int'>
print(10.50, type(10.50))  # <class 'float'>
print(10 == 10, type(10 == 10))  #

print(bool('Roberto'))
print(int("10"), "10")
print(float("10"), "10.0")
print(10 + int("10"))

# Exercício

# Nome: string
print("Nome:", end=" ")
print('Roberto Camargo', type('Roberto Camargo'))

# Idade: int
print("Idade:", end=" ")
print(25, type(25))

# Altura: float
print("Altura:", end=" ")
print(1.70, type(1.70))

# É maior de idade: boolean
print("É maior de idade:", end=" ")
print(25 >= 18, type(25 >= 18))

