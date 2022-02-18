"""
Condições IF, ELIF e ELSE
Operadores Relacionais
== > >= < <= !=

== - Igual a
>  - Maior que
>= - Maior ou igual a
<  - Menor que
<= - Menor ou igual a
!= - Diferente de

"""

print("### Example 1: IF, ELIF, ELSE ###")

print("\n1 - IF")
print("2 - ELIF")
print("ANY OTHER THING - ELSE")

option = input("\nChoose an option: ")

print("\n\t# YOU CHOSE: ", end="")
if option == "1":
    print("IF", end="\n\n")
elif option == "2":
    print("ELIF", end="\n\n")
else:
    print("ELSE", end="\n\n")

print("#########################################################")
print("### Example 2: 2 compared to 2 - Relational Operators ###")
print("#########################################################\n")

equalsTo = 2 == 2
greaterThan = 2 > 2
greaterOrEqualsTo = 2 >= 2
lessThan = 2 < 2
lessOrEqualsTo = 2 <= 2
differentThan = 2 != 2

print(f"2 equalsTo 2: {equalsTo}")
print(f"2 greaterThan 2: {greaterThan}")
print(f"2 greaterOrEqualsTo 2: {greaterOrEqualsTo}")
print(f"2 lessThan 2: {lessThan}")
print(f"2 lessOrEqualsTo 2: {lessOrEqualsTo}")
print(f"2 differentThan 2: {differentThan}")

