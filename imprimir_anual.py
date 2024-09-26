import sqlite3 # Importação padrão do Python para interagir com bancos de dados SQLite
import conexao # Responsável por estabelecer a conexão com o banco de dados

def gerar_relatorio_anual():
    try:  # Capturar as exceções
        conexao.conectar_banco() # Chama a função para estabelecer a conexão com o banco de dados
        matricula = int(input("Informe a matricula do aluno para gerar o relatório anual: ")) #  Solicita ao usuário a matrícula do aluno para gerar o relatório
        
        # Busca o aluno com a matrícula informada, se o aluno for encontrado, os dados são armazenados na variável
        conexao.cursor.execute("SELECT * FROM aluno WHERE matricula =?", (matricula,))
        aluno = conexao.cursor.fetchone()

        # Se o aluno for encontrado, o usuário é solicitado a fornecer os relatórios sobre desempenho, presença e comportamento
        if aluno:
            relatorioA1 = input("Informe o relatório sobre o desempenho: ")
            relatorioA2 = input("Informe o relatório sobre a presença:  ")
            relatorioA3 = input("Informe o relatório sobre o comportamento:  ")
            
            conexao.cursor.execute("""
                UPDATE aluno
                SET relatorioA1 = ?, relatorioA2 = ?, relatorioA3 = ?
                WHERE matricula = ?
            """, (relatorioA1, relatorioA2, relatorioA3, matricula))

            # Uma nova query é executada para atualizar os campos de relatório do aluno na tabela aluno
            conexao.conn.commit() # As alterações no banco de dados são confirmadas com conexao.conn.commit()
            print("Relatório anual atualizado com sucesso!") # Uma mensagem é exibida para informar que o relatório foi atualizado de boa
        else:
            print("Aluno não encontrado!") # Se o aluno não for encontrado, uma mensagem de erro é exibida

    except sqlite3.Error as erro: #  Qualquer exceção do tipo sqlite3.Error que possa ocorrer, a mensagem de erro é exibida para o usuário
        print("Erro ao gerar o relatório anual!", erro)
    finally: # Garante que a conexão com o banco de dados seja fechada, mesmo que ocorra uma exceção
        conexao.conn.commit()
        conexao.conn.close()