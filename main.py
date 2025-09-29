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

# etapa 2 

def cadastrar_livros(titulo, autor, ano):
    try:
        conn = sqlite3.connect("biblioteca.db")
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO livros (titulo, autor, ano, disponivel)
            VALUES (?, ?, ?, 'SIM')
        """, (titulo, autor, ano))
        conn.commit()
        print("Livro cadastrado com sucesso!")
    except sqlite3.Error as e:
        print("Erro ao cadastrar livro:", e)
    finally:
        conn.close()

# Todo livro novo deve ser cadastrado com disponivel = "Sim". 

# Etapa 3: Função para listar livros
def listar_livros():
    try:
        conn = sqlite3.connect("biblioteca.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM livros")
        livros = cursor.fetchall()

        if livros:
            for livro in livros:
                print(f"ID: {livro[0]}, Título: {livro[1]}, Autor: {livro[2]}, Ano: {livro[3]}, Disponível: {livro[4]}")
        else:
            print("Nenhum livro encontrado na biblioteca.")
    except sqlite3.Error as e:
        print("Erro ao listar livros:", e)
    finally:
        conn.close()

# etapa 4: atualizar disponibilidade

def disponibilizar_livros(id_livro):
    try: 
        conn = sqlite3.connect("biblioteca.db")
        cursor = conn.cursor()

        # verifica os status atual do livro
        cursor.execute("SELECT disponivel FROM livros WHERE id = ?", (id_livro,))
        resultado = cursor.fetchone()

        if resultado:
            status_atual = resultado[0].upper()
            novo_status = 'NÂO' if status_atual == 'SIM' else 'SIM'

            # atualizando o status do livro
            cursor.execute("UPDATE livros SET disponivel = ? WHERE id = ?", (novo_status, id_livro))
            conn.commit()
            print(f"Disponibilidade do livro com ID {id_livro} atualizada para: {novo_status}")
        else:
            print(f"Nenhum livro encontrado com ID {id_livro}.")
    except sqlite3.Error as e:
        print("Erro ao atualizar disponibilidade:", e)
    finally:
        conn.close()

# etapa 5 remoção de livros 

def remover_livros(id):
    try: 
        conn = sqlite3.connect('biblioteca.db')
        cursor = conn.cursor()

        cursor.execute("DELETE FROM livros WHERE id = ?", (id,))
        conn.commit()

        if cursor.rowcount > 0:
            print(f"Livro com ID {id} removido com sucesso!")
        else:
            print(f"Nenhum livro encontrado com ID {id}.")
    except sqlite3.Error as e:
        print("Erro ao remover livro:", e)
    finally:
        conn.close()


# 