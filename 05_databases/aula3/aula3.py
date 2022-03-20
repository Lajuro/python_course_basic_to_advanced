import pymysql.cursors
from contextlib import contextmanager


@contextmanager
def conecta():
    conexao = pymysql.connect(
        host='localhost',
        user='root',
        password='admin',
        db='clientes',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )
    try:
        yield conexao
    finally:
        print("Conexão encerrada")
        conexao.close()


# with conecta() as conexao:
#     with conexao.cursor() as cursor:
#         sql = "INSERT INTO clientes (nome, sobrenome, idade, peso) VALUES (%s, %s, %s, %s)"
#         cursor.execute(sql, ('João', 'Silva', 20, 80.5))
#         conexao.commit()
#
# with conecta() as conexao:
#     with conexao.cursor() as cursor:
#         sql = "INSERT INTO clientes (nome, sobrenome, idade, peso) VALUES (%s, %s, %s, %s)"
#         dados = [
#             ('Maria', 'Silva', 30, 50.5),
#             ('Pedro', 'Santos', 20, 70.5),
#             ('Ana', 'Pereira', 25, 60.5),
#             ('José', 'Oliveira', 35, 40.5)
#         ]
#         cursor.executemany(sql, dados)
#         conexao.commit()


# with conecta() as conexao:
#     with conexao.cursor() as cursor:
#         # sql = "DELETE FROM clientes WHERE id IN (%s, %s, %s)"
#         sql = "DELETE FROM clientes"
#         cursor.execute(sql)
#         conexao.commit()


with conecta() as conexao:
    with conexao.cursor() as cursor:
        cursor.execute('SELECT * FROM clientes')
        resultado = cursor.fetchall()
        for linha in resultado:
            # id, nome, sobrenome, idade, peso = linha
            print(f'{linha["id"]:<3} {linha["nome"]:<10} {linha["sobrenome"]:<10} {linha["idade"]:<3} {linha["peso"]:0>6.2f}')

