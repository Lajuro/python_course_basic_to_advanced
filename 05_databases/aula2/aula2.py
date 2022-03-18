import sqlite3


class AgendaDB:
    def __init__(self, db_name):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.db_name = db_name
        self.create_table()

    def create_table(self):
        self.cursor.execute("DROP TABLE IF EXISTS agenda")
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS agenda (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                telefone TEXT NOT NULL
            )
            """
        )
        self.connection.commit()

    def inserir(self, nome, telefone):
        self.cursor.execute("INSERT INTO agenda VALUES (?, ?, ?)", (None, nome, telefone))
        self.connection.commit()

    def editar(self, id, nome, telefone):
        self.cursor.execute("UPDATE agenda SET nome = ?, telefone = ? WHERE id = ?", (nome, telefone, id))
        self.connection.commit()

    def remover(self, id):
        self.cursor.execute("DELETE FROM agenda WHERE id = ?", (id,))
        self.connection.commit()

    def listar(self):
        self.cursor.execute("SELECT * FROM agenda")
        print(f"\n{' AGENDA ':#^45}")
        print(f"{'ID':>5} {'NOME':<20} {'TELEFONE':<20}")
        for linha in self.cursor.fetchall():
            id, nome, telefone = linha
            print(f"{id:0>5} {nome:<20} {telefone:<20}")
        print(f"{'':#^45}\n")

    def fechar(self):
        self.connection.close()


if __name__ == "__main__":
    agenda = AgendaDB("agenda.db")
    agenda.inserir("Maria", "9999-9999")
    agenda.inserir("João", "8888-8888")
    agenda.inserir("José", "7777-7777")
    agenda.inserir("Pedro", "6666-6666")
    agenda.inserir("Paulo", "5555-5555")
    agenda.inserir("Carlos", "4444-4444")
    agenda.inserir("Antônio", "3333-3333")
    agenda.inserir("Felipe", "2222-2222")
    agenda.inserir("Joaquim", "1111-1111")
    agenda.listar()
    agenda.remover(3)
    agenda.listar()
    agenda.editar(1, "Maria", "5789-5789")
    agenda.listar()
    agenda.inserir("Cleiton", "5353-5353")
    agenda.inserir("José", "5353-5353")
    agenda.listar()
    agenda.fechar()
