import sqlite3
import conexao
import tabela

def consultar_boletim():
    tabela.criar_tabela()
    # Matricula
    matricula = input("Informe o número da matrícula que deseja consultar: ")
    try:
        # Pegando a matrícula da tabela
        resultado = conexao.conn.execute('''SELECT * FROM aluno WHERE matricula = ?''',(matricula,)).fetchall()
        if not resultado:
            print("Matrícula não encontrada!")
        else:
            for result in resultado:
                print(">>>>>>>>>><<<<<<<<<<\n")
                print(f"Matrícula: {result[0]}")
                print(f"Nome: {result[1]}")
                print(f"Presença: {result[11]}")
                print(f"Falta: {result[12]}")
                print(f"Série: {result[13]}")
                print(f"Turno: {result[14]}\n")
                print("Notas:")
                print(f"  Português: {result[16]} (1ª unidade), {result[17]} (2ª unidade), {result[18]} (3ª unidade)")
                print(f"  Matemática: {result[19]} (1ª unidade), {result[20]} (2ª unidade), {result[21]} (3ª unidade)")
                print(f"  Biologia: {result[22]} (1ª unidade), {result[23]} (2ª unidade), {result[24]} (3ª unidade)")
                print(f"  Física: {result[25]} (1ª unidade), {result[26]} (2ª unidade), {result[27]} (3ª unidade)")
                print(f"  Inglês: {result[28]} (1ª unidade), {result[29]} (2ª unidade), {result[30]} (3ª unidade)")
                print(f"  Filosofia: {result[31]} (1ª unidade), {result[32]} (2ª unidade), {result[33]} (3ª unidade)")
                print(f"  Artes: {result[34]} (1ª unidade), {result[35]} (2ª unidade), {result[36]} (3ª unidade)")
                print(f"  Química: {result[37]} (1ª unidade), {result[38]} (2ª unidade), {result[39]} (3ª unidade)")
                print(f"  História: {result[40]} (1ª unidade), {result[41]} (2ª unidade), {result[42]} (3ª unidade)")
                print(f"  Sociologia: {result[43]} (1ª unidade), {result[44]} (2ª unidade), {result[45]} (3ª unidade)")
            
                print("Médias Finais:")
                print(f"  Português: {result[49]}")
                print(f"  Matemática: {result[50]}")
                print(f"  Biologia: {result[51]}")
                print(f"  Física: {result[52]}")
                print(f"  Inglês: {result[53]}")
                print(f"  Filosofia: {result[54]}")
                print(f"  Artes: {result[55]}")
                print(f"  Química: {result[56]}")
                print(f"  História: {result[57]}")
                print(f"  Sociologia: {result[58]}")
                
        
    except sqlite3.Error as erro:
        print("Erro ao encontrar aluno", erro)
    finally:
        conexao.conn.close()
