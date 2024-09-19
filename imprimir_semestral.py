import sqlite3
import conexao


def imprimir_relatorio_semestral():
    try:
        conexao.conectar_banco()
        matricula = int(
            input("Informe a matrícula do aluno para imprimir os relatórios: "))

        # Obter o relatório sobre o desempenho
        conexao.cursor.execute(
            "SELECT relatorio1 FROM aluno WHERE matricula=?", (matricula,))
        relatorio1 = conexao.cursor.fetchone()

        # Obter o relatório sobre a presença
        conexao.cursor.execute(
            "SELECT relatorio2 FROM aluno WHERE matricula=?", (matricula,))
        relatorio2 = conexao.cursor.fetchone()

        # Obter o relatório sobre o comportamento
        conexao.cursor.execute(
            "SELECT relatorio3 FROM aluno WHERE matricula=?", (matricula,))
        relatorio3 = conexao.cursor.fetchone()

        print("\nRelatório sobre o desempenho:")
        print(relatorio1)

        print("\nRelatório sobre a presença:")
        print(relatorio2)

        print("\nRelatório sobre o comportamento:")
        print(relatorio3)

    except sqlite3.Error as erro:
        print("Erro ao imprimir os relatórios!", erro)
    finally:
        conexao.conn.close()
