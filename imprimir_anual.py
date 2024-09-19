import sqlite3
import conexao


def imprimir_relatorio_anual():
    try:
        conexao.conectar_banco()
        matricula = int(
            input("Informe a matrícula do aluno para imprimir os relatórios: "))

        # Obter o relatório sobre o desempenho
        conexao.cursor.execute(
            "SELECT relatorioA1 FROM aluno WHERE matricula=?", (matricula,))
        relatorioA1 = conexao.cursor.fetchone()

        # Obter o relatório sobre a presença
        conexao.cursor.execute(
            "SELECT relatorioA2 FROM aluno WHERE matricula=?", (matricula,))
        relatorioA2 = conexao.cursor.fetchone()

        # Obter o relatório sobre o comportamento
        conexao.cursor.execute(
            "SELECT relatorioA3 FROM aluno WHERE matricula=?", (matricula,))
        relatorioA3 = conexao.cursor.fetchone()

        print("\nRelatório sobre o desempenho:")
        print(relatorioA1)

        print("\nRelatório sobre a presença:")
        print(relatorioA2)

        print("\nRelatório sobre o comportamento:")
        print(relatorioA3)

    except sqlite3.Error as erro:
        print("Erro ao imprimir os relatórios!", erro)
    finally:
        conexao.conn.close()
