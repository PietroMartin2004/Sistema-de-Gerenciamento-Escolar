import sqlite3
import conexao

def imprimir_relatorio_anual():
    try:
        # Estabelece a conexão e o cursor localmente
        conn = conexao.conectar_banco()
        cursor = conn.cursor()

        matricula = int(input("Informe a matrícula do aluno para imprimir os relatórios: "))

        # Obter o relatório sobre o desempenho
        cursor.execute("SELECT relatorioA1 FROM aluno WHERE matricula=?", (matricula,))
        relatorioA1 = cursor.fetchone()

        # Obter o relatório sobre a presença
        cursor.execute("SELECT relatorioA2 FROM aluno WHERE matricula=?", (matricula,))
        relatorioA2 = cursor.fetchone()

        # Obter o relatório sobre o comportamento
        cursor.execute("SELECT relatorioA3 FROM aluno WHERE matricula=?", (matricula,))
        relatorioA3 = cursor.fetchone()

        print("\nRelatório sobre o desempenho:")
        print(relatorioA1[0] if relatorioA1 else "Nenhum relatório disponível.")

        print("\nRelatório sobre a presença:")
        print(relatorioA2[0] if relatorioA2 else "Nenhum relatório disponível.")

        print("\nRelatório sobre o comportamento:")
        print(relatorioA3[0] if relatorioA3 else "Nenhum relatório disponível.")

    except sqlite3.Error as erro:
        print("Erro ao imprimir os relatórios!", erro)
    finally:
        # Garante o fechamento da conexão no fim
        if conn:
            conn.close()