"""
4 - Fizz Buzz
Se o parâmetro da função for divisível por 2, retorne fizz.
Se o parâmetro da função for divisível por 5, retorne buzz.
Se o parâmetro da função for divisível por 5 e por 3, retorne FizzBuzz
Caso contrário, retorne o número
enviado.
"""


def fizz_buzz(num):
    if num % 2 == 0:
        return 'fizz'
    elif num % 5 == 0 and num % 3 == 0:
        return 'FizzBuzz'
    elif num % 5 == 0:
        return 'buzz'
    else:
        return num


print(fizz_buzz(10))
print(fizz_buzz(15))
print(fizz_buzz(5))
print(fizz_buzz(27))