# estrutura do projeto 
# etapa 1 do projeto 
import sqlite3
import _sqlite3
# etapa 1
conexao = sqlite3.connect("biblioteca.db")
cursor = conexao.cursor()

# Criando uma tabela no banco chamada de "biblioteca"
cursor.execute("""
    CREATE TABLE IF NOT EXISTS livros (
     id INTEGER PRIMARY KEY AUTOINCREMENT,
     autor TEXT NOT NULL,
     ano INTEGER,
     disponivel TEXT    
     )                
 """)
print("Tabela criada com sucesso!")



























