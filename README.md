# 📚 Sistema de Gerenciamento de Biblioteca

Este é um projeto simples de gerenciamento de biblioteca desenvolvido em Python, utilizando banco de dados SQLite3. O sistema permite cadastrar, listar, atualizar a disponibilidade e remover livros do banco.

## ✅ Funcionalidades

- 📘 Cadastrar novos livros
- 📖 Listar todos os livros cadastrados
- 🔄 Atualizar a disponibilidade de um livro (SIM/NÃO)
- ❌ Remover livros do sistema
- 📋 Interface de menu interativo via terminal

---

## ⚙️ Tecnologias Utilizadas

- Python 3
- SQLite (banco de dados local)
- Biblioteca `sqlite3` (padrão do Python)

---

## 📂 Estrutura do Projeto


biblioteca/
├── biblioteca.db        # Banco de dados SQLite (criado automaticamente)
├── biblioteca.py        # Script principal com todas as funções e o menu
├── README.md            # Este arquivo

---MENU BIBLIOTECA---
1. cadastrar livro
2. listar livros
3. atualizar disponibilidade do livro
4. remover livro
5. sair
📌 Observações
Todo novo livro é cadastrado com o status de disponível = "SIM".

A tabela do banco de dados (livros) será criada automaticamente ao executar o programa pela primeira vez.

O banco de dados é salvo no arquivo biblioteca.db na mesma pasta do script.

🧑‍💻 Autor
Desenvolvido por [Kauã Santos]
💬 Contato: [kaua7santos7oliveiraa@gmail.com]