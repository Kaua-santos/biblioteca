import sqlite3
import streamlit as st

# Inicializa/cria o banco corretamente
def inicializar_banco():
    conn = sqlite3.connect("biblioteca.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS livros (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            autor TEXT NOT NULL,
            ano INTEGER,
            disponivel TEXT
        )
    """)
    conn.commit()
    conn.close()

# Cadastra livros
def cadastrar_livros(titulo, autor, ano):
    try:
        conn = sqlite3.connect("biblioteca.db")
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO livros (titulo, autor, ano, disponivel)
            VALUES (?, ?, ?, 'SIM')
        """, (titulo, autor, ano))
        conn.commit()
        st.success(" Livro cadastrado com sucessoo!")
    except sqlite3.Error as e:
        st.error(f"Erro ao cadastrar livro: {e}")
    finally:
        conn.close()

# Lista livros
def listar_livros():
    try:
        conn = sqlite3.connect("biblioteca.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM livros")
        livros = cursor.fetchall()
        conn.close()
        return livros
    except sqlite3.Error as e:
        st.error(f"Erro ao listar livros: {e}")
        return []

# Atualiza disponibilidade
def atualizar_disponibilidade(id_livro):
    try:
        conn = sqlite3.connect("biblioteca.db")
        cursor = conn.cursor()
        cursor.execute("SELECT disponivel FROM livros WHERE id = ?", (id_livro,))
        resultado = cursor.fetchone()
        if resultado:
            status_atual = resultado[0].upper()
            novo_status = 'NÃO' if status_atual == 'SIM' else 'SIM'
            cursor.execute("UPDATE livros SET disponivel = ? WHERE id = ?", (novo_status, id_livro))
            conn.commit()
            st.success(f"📘 Disponibilidade do livro com ID {id_livro} atualizada para: {novo_status}")
        else:
            st.warning(f"Nenhum livro encontrado com ID {id_livro}.")
    except sqlite3.Error as e:
        st.error(f"Erro ao atualizar disponibilidade: {e}")
    finally:
        conn.close()

# Interface com Streamlit
def main():
    st.set_page_config(page_title="Biblioteca Santos", layout="centered")
    st.title(" Sistema da bibliotecaa")
    inicializar_banco()

    menu = ["Cadastrar Livro", "Listar Livros", "Atualizar Disponibilidade"]
    escolha = st.sidebar.selectbox("Menu", menu)

    if escolha == "Cadastrar Livro":
        st.subheader("Cadastro de Livros")
        with st.form(key="form_cadastro"):
            titulo = st.text_input("Título do Livro")
            autor = st.text_input("Autor do Livro")
            ano = st.number_input("Ano de Publicação", min_value=0, max_value=2100, step=1)
            submit = st.form_submit_button("Cadastrar")

            if submit:
                if titulo and autor:
                    cadastrar_livros(titulo, autor, ano)
                else:
                    st.warning("Preencha todos os campos obrigatórios.")

    elif escolha == "Listar Livros":
        st.subheader("Lista de Livros")
        livros = listar_livros()

        if livros:
            for livro in livros:
                st.write(f"**ID**: {livro[0]} | **Título**: {livro[1]} | **Autor**: {livro[2]} | **Ano**: {livro[3]} | **Disponível**: {livro[4]}")
        else:
            st.info("Nenhum livro cadastrado ainda.")

    elif escolha == "Atualizar Disponibilidade":
        st.subheader(" Atualizar Disponibilidade dos Livros")
        livros = listar_livros()
        if livros:
            ids = [f"{livro[0]} - {livro[1]}" for livro in livros]
            escolha_id = st.selectbox("Escolha o livro:", ids)

            if escolha_id:
                id_livro = int(escolha_id.split(" - ")[0])
                if st.button("Atualizar Disponibilidade"):
                    atualizar_disponibilidade(id_livro)
        else:
            st.info("Não há livros para atualizar.")

if __name__ == "__main__":
    main()
