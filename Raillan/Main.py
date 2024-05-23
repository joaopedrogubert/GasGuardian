import sqlite3

# Conectar ao banco de dados
conn = sqlite3.connect('/Users/railanabreu/Documents/Projects/GasGuardian/Raillan/dados/DADOS.sqlite')
cursor = conn.cursor()

# Adicionar a nova coluna 'Nome'
cursor.execute("ALTER TABLE Tanques ADD COLUMN Nome TEXT")

# Atualizar os valores da nova coluna 'Nome'
for i in range(1, 11):
    nome = f"Bomba {i:02}"
    cursor.execute("UPDATE Tanques SET Nome = ? WHERE rowid = ?", (nome, i))

# Confirmar as alterações e fechar a conexão
conn.commit()
conn.close()
