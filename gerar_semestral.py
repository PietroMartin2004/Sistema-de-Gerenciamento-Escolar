import sqlite3
import conexao

def gerar_relatorio_semestral():
    try:
        
        #Concede a conexão com o banco de dados.
        conexao.conectar_banco()

        #Solicita ao usuário que insira a matrícula do aluno para o qual o relatório será gerado.
        matricula = int(input("Informe a matrícula do aluno para gerar o relatório: "))
        
        #Obtém as informações do aluno correspondente à matrícula fornecida.
        conexao.cursor.execute("SELECT * FROM aluno WHERE matricula=?", (matricula,))
        # Pega o resultado (dados do aluno).
        aluno = conexao.cursor.fetchone()

        #Solicita ao usuário que informe para qual semestre o relatório será gerado (1º ou 2º semestre).
        opcaoSemestre = input("Qual semestre você deseja gerar o relatório (1 ou 2): ")

        if aluno:

            #Se o semestre escolhido for o 1º.
            if opcaoSemestre == '1':
                #Solicita informações de desempenho, presença e comportamento.
                relatorio1 = input("Informe o relatório sobre o desempenho: ")
                relatorio2 = input("Informe o relatório sobre a presença: ")
                relatorio3 = input("Informe o relatório sobre o comportamento: ")
                
                #Atualiza os relatórios do 1º semestre no banco de dados.
                conexao.cursor.execute("""
                UPDATE aluno
                SET relatorio1 = ?, relatorio2 = ?, relatorio3 = ?
                WHERE matricula = ?
            """, (relatorio1, relatorio2, relatorio3, matricula))
                
            #Se o semestre escolhido for o 2º.
            elif opcaoSemestre == '2':
                #Solicita informações de desempenho, presença e comportamento.
                relatorio4 = input("Informe o relatório sobre o desempenho: ")
                relatorio5 = input("Informe o relatório sobre a presença: ")
                relatorio6 = input("Informe o relatório sobre o comportamento: ")
                
                #Atualiza os relatórios referentes ao 2º semestre no banco de dados.
                conexao.cursor.execute("""
                UPDATE aluno
                SET relatorio4 = ?, relatorio5 = ?, relatorio6 = ?
                WHERE matricula = ?
            """, (relatorio4, relatorio5, relatorio6, matricula))
            
            #Confirma as mudanças no banco de dados.
            conexao.conn.commit()
            print("Relatório atualizado com sucesso!")
        else:
            #Se a matrícula não for encontrada, exibe uma mensagem.
            print("Aluno não encontrado!")

    except sqlite3.Error as erro:
        #Caso de algum erroo, exibe a mensagem de erro.
        print("Erro ao gerar o relatório!", erro)
    finally:
        # Fecha a conexão com o banco de dados.
        conexao.conn.close()
