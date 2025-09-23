# estrutura do projeto 
# etapa 1 do projeto 
import sqlite3
import _sqlite3
# etapa 1

conexao = sqlite3.connect("biblioteca.db")
cursor = conexao.cursor()

# # Criando uma tabela no banco chamada de "biblioteca"
# cursor.execute("""
#     CREATE TABLE IF NOT EXISTS livros (
#      id INTEGER PRIMARY KEY AUTOINCREMENT,
#      autor TEXT NOT NULL,
#      ano INTEGER,
#      disponivel TEXT    
#      )                
#  """)
# print("Tabela criada com sucesso!")

# etapa 2 

def cadastrar_livros(titulo, autor,ano): 
    conn = conexao()
    cursor = conn.cursor 

    cursor.execute("""
        INSERT INTO livros (titulo, autor, ano) 
        VALUES (?, ?, ?)
    """, (titulo, autor, ano, 'SIM'))
# Todo livro novo deve ser cadastrado com disponivel = "Sim". 

# Etapa 3: Função para listar livros
def listar_livros():
    conn = sqlite3.connect("biblioteca.db")
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM livros')
    livros = cursor.fetchall()

    if livros:
        for livro in livros:
            print(f"ID: {livro[0]}, Título: {livro[1]}, Autor: {livro[2]}, Ano: {livro[3]}, Disponível: {livro[4]}")
    else:
        print("Nenhum livro encontrado na biblioteca.")
    conn.close()











