import sqlite3

# Conectar Banco


def conectar_banco():
    try:
        # Declarando Banco
        global conn
        conn = sqlite3.connect('teste7.db')
        global cursor
        cursor = conn.cursor()
        print("Banco conectado com sucesso!")
        conn.commit()
    except sqlite3.Error as erro:
        print("Erro de conexão com o banco de dados!")
