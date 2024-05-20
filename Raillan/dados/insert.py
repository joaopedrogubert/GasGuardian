import sqlite3

# Caminho do banco de dados
db_path = '/Users/railanabreu/Documents/Projects/GasGuardian/Raillan/dados/dadosPosto.sqlite'

# Caminho do arquivo SQL
sql_file_path = '/Users/railanabreu/Documents/Projects/GasGuardian/Raillan/dados/create_and_insert_data.sql'

# Conectar ao banco de dados SQLite
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Ler o conteúdo do script SQL
with open(sql_file_path, 'r') as sql_file:
    sql_script = sql_file.read()

# Executar o script SQL
cursor.executescript(sql_script)

# Fechar a conexão
conn.close()
