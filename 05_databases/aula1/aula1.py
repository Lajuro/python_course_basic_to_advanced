"""
SQLite
"""

import sqlite3

conexao = sqlite3.connect('basededados.db')
cursor = conexao.cursor()

# cursor.execute("DROP TABLE IF EXISTS clientes")
cursor.execute('CREATE TABLE IF NOT EXISTS clientes ('
               'id INTEGER PRIMARY KEY AUTOINCREMENT,'
               'nome TEXT NOT NULL UNIQUE,'
               'peso REAL NOT NULL'
               ')')
try:
    cursor.execute('INSERT INTO clientes VALUES (:id, :nome, :peso)', {'id': None, 'nome': 'Pedro', 'peso': 80.5})
    cursor.execute('INSERT INTO clientes (nome, peso) VALUES (:nome, :peso)', {'nome': 'Maria', 'peso': 60.5})
    cursor.execute('INSERT INTO clientes (nome, peso) VALUES (?, ?)', ('João', 80.5))
    conexao.commit()
except sqlite3.IntegrityError as e:
    print('[INFO] Não foi possível inserir o registro')
    if 'UNIQUE constraint failed' in str(e):
        print('[ERROR] Nome duplicado')
    print(f'[ERROR]: {e}')

cursor.execute('UPDATE clientes SET nome=:nome WHERE id=:id', {'nome': 'Oscar', 'id': 3})

cursor.execute('SELECT * FROM clientes')
for linha in cursor.fetchall():
    id, nome, peso = linha
    print(f'{id:<5} {nome:<10} {peso:<5}')


cursor.close()
conexao.close()
