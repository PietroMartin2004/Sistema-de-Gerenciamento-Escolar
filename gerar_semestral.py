import sqlite3
import conexao


def gerar_relatorio_semestral():
    try:

        conexao.conectar_banco()
        matricula = int(
            input("Informe a matrícula do aluno para gerar o relatório: "))

        # Obter o aluno

        conexao.cursor.execute(
            "SELECT * FROM aluno WHERE matricula=?", (matricula,))
        aluno = conexao.cursor.fetchone()

        if aluno:
            relatorio1 = input("Informe o relatório sobre o desempenho: ")
            relatorio2 = input("Informe o relatório sobre a presença: ")
            relatorio3 = input("Informe o relatório sobre o comportamento: ")

            conexao.cursor.execute("""
                UPDATE aluno
                SET relatorio1 = ?, relatorio2 = ?, relatorio3 = ?
                WHERE matricula = ?
            """, (relatorio1, relatorio2, relatorio3, matricula))

            conexao.conn.commit()
            print("Relatório atualizado com sucesso!")
        else:
            print("Aluno não encontrado!")

    except sqlite3.Error as erro:
        print("Erro ao gerar o relatório!", erro)
    finally:
        conexao.conn.close()
