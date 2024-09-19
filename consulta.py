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
                print(f"              (1ªUnidade ),    (2ªUnidade ),    (3ªUnidade )")
                print(f"  Português:     {result[16]}              {result[17]}              {result[18]}")
                print(f"  Matemática:    {result[19]}              {result[20]}              {result[21]}")
                print(f"  Biologia:      {result[22]}              {result[23]}              {result[24]}")
                print(f"  Física:        {result[25]}              {result[26]}              {result[27]}")
                print(f"  Inglês:        {result[28]}              {result[29]}              {result[30]}")
                print(f"  Filosofia:     {result[31]}              {result[32]}              {result[33]}")
                print(f"  Artes:         {result[34]}              {result[35]}              {result[36]}")
                print(f"  Química:       {result[37]}              {result[38]}              {result[39]}")
                print(f"  História:      {result[40]}              {result[41]}              {result[42]}")
                print(f"  Sociologia:    {result[43]}              {result[44]}              {result[45]}")
            
                print("\nMédias Finais:")
                print(f"  Português:  {result[49]}")
                print(f"  Matemática: {result[50]}")
                print(f"  Biologia:   {result[51]}")
                print(f"  Física:     {result[52]}")
                print(f"  Inglês:     {result[53]}")
                print(f"  Filosofia:  {result[54]}")
                print(f"  Artes:      {result[55]}")
                print(f"  Química:    {result[56]}")
                print(f"  História:   {result[57]}")
                print(f"  Sociologia: {result[58]}")
                
        
    except sqlite3.Error as erro:
        print("Erro ao encontrar aluno", erro)
    finally:
        conexao.conn.close()
