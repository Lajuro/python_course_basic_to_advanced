"""
Operador ternário
"""

logged_user = True

# Sem ternário

if logged_user:
    msg = 'Usuário logado.'
else:
    msg = 'Usuário não está logado.'

print(msg)

# Com ternário

msg = 'Usuário logado.' if logged_user else 'Usuário não está logado.'
print(msg)

idade = 15
maiorIdade = 'É maior de idade' if idade >= 18 else 'É menor de idade'

print(maiorIdade)
