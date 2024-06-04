import sqlite3

class SQLiteExecutor:
    def __init__(self, db_path):
        self.db_path = db_path

    def execute(self, command):
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            cursor.execute(command)
            conn.commit()
            return cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Erro ao executar o comando SQL: {e}")
            return None
        finally:
            conn.close()

    def executescript(self, script):
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            cursor.executescript(script)
            conn.commit()
        except sqlite3.Error as e:
            print(f"Erro ao executar o script SQL: {e}")
        finally:
            conn.close()

# Exemplo de uso
db_path = '/Users/railanabreu/Documents/Projects/GasGuardian/Raillan/dados/DADOS.sqlite'
executor = SQLiteExecutor(db_path)

# Executar um comando SQL
result = executor.execute("SELECT * FROM Bombas;")
print(result)

# Executar um script SQL
sql_script = '''
CREATE TABLE IF NOT EXISTS Bombasx (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    autoAbastecimento BOOLEAN NOT NULL,
    tipoCombustivel_nome TEXT NOT NULL,
    bombaAtiva BOOLEAN NOT NULL,
    tanque_id INTEGER NOT NULL,
    nomeBomba TEXT NOT NULL,
    FOREIGN KEY (tanque_id) REFERENCES Tanques (id),
    FOREIGN KEY (tipoCombustivel_nome) REFERENCES TipoCombustivel (nome)
);
'''

executor.executescript(sql_script)
