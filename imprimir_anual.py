import sqlite3
import conexao
def imprimir_relatorio_anual():
    try:
        #Conectar banco
        conexao.conectar_banco()

        matricula = int(input("Informe a matrícula do aluno para imprimir os relatórios: "))

        # Obter o relatório sobre o desempenho
        conexao.conn.execute("SELECT relatorioA1 FROM aluno WHERE matricula=?", (matricula,))
        relatorioA1 = conexao.cursor.fetchone()

        # Obter o relatório sobre a presença
        conexao.conn.execute("SELECT relatorioA2 FROM aluno WHERE matricula=?", (matricula,))
        relatorioA2 = conexao.cursor.fetchone()

        # Obter o relatório sobre o comportamento
        conexao.conn.execute("SELECT relatorioA3 FROM aluno WHERE matricula=?", (matricula,))
        relatorioA3 = conexao.cursor.fetchone()

        print("\nRelatório sobre o desempenho:")
        print(relatorioA1[0] if relatorioA1 else "Nenhum relatório disponível.")

        print("\nRelatório sobre a presença:")
        print(relatorioA2[0] if relatorioA2 else "Nenhum relatório disponível.")

        print("\nRelatório sobre o comportamento:")
        print(relatorioA3[0] if relatorioA3 else "Nenhum relatório disponível.")

    except sqlite3.Error as erro:
        print("Erro ao imprimir os relatórios!", erro)
        conexao.conn.close()