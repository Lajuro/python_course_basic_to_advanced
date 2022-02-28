"""
Levantando exceções em Python (raise)
"""


def divide(n1, n2):
    try:
        if not n1 or not n2:
            raise Exception("Não foi informado o valor para n1 ou para n2")
        return n1 / n2
    except ZeroDivisionError as error:
        return False
    except Exception as error:
        print(error)


print(divide(1, 0))