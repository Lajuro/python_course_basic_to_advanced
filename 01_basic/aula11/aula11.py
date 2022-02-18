"""
Operadores Lógicos
and, or, not, in e not in
"""

print("##########################")
print("### Logical Operators ###")
print("##########################\n")

age1 = 26
age2 = 15

print("# AND")
print(f"{age1} > 18 AND {age2} > 18: {age1 > 18 and age2 > 18}")

print("# OR")
print(f"{age1} > 18 OR {age2} > 18: {age1 > 18 or age2 > 18}")

print("# NOT")
print(f"{age1} NOT GREATER THAN 25: {not age1 > 25}")

print("# IN")
print(f"{age1} IN the list [10, 15, 20, 25]: {age1 in [10, 15, 20, 25]}")

print("# NOT IN")
print(f"{age1} NOT IN the list [10, 15, 20, 25]: {age1 not in [10, 15, 20, 25]}")
