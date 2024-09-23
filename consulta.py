import sqlite3
import conexao
import tabela
import media_final
def consultar_boletim():
    tabela.criar_tabela()
    #Chamando a função do cálculo das médias para ir atualizando
    media_final.obter_medias_finais()
    # Matricula
    matricula = input("Informe o número da matrícula que deseja consultar: ")
    try:
        # Pegando a matrícula da tabela
        resultado = conexao.conn.execute('''SELECT * FROM aluno WHERE matricula = ?''', (matricula,)).fetchall()
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
<<<<<<< HEAD
<<<<<<< Updated upstream
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
=======
                print(f"              (1ªUnidade )    (2ªUnidade )    (3ªUnidade )")
                print(f"  Português:     {result[15]}              {result[24]}              {result[34]}")
                print(f"  Matemática:    {result[16]}              {result[25]}              {result[35]}")
                print(f"  Biologia:      {result[17]}              {result[26]}              {result[36]}")
                print(f"  Física:        {result[18]}              {result[27]}              {result[37]}")
                print(f"  Inglês:        {result[19]}              {result[28]}              {result[38]}")
                print(f"  Filosofia:     {result[20]}              {result[29]}              {result[39]}")
                print(f"  Artes:         {result[21]}              {result[30]}              {result[37]}")
                print(f"  Química:       {result[22]}              {result[31]}              {result[38]}")
                print(f"  História:      {result[23]}              {result[32]}              {result[40]}")
                print(f"  Sociologia:    {result[24]}              {result[33]}              {result[41]}")
            
                print("\nMédias Finais:")
                print(f"  Português:  {result[42]}")
                print(f"  Matemática: {result[43]}")
                print(f"  Biologia:   {result[44]}")
                print(f"  Física:     {result[45]}")
                print(f"  Inglês:     {result[46]}")
                print(f"  Filosofia:  {result[47]}")
                print(f"  Artes:      {result[48]}")
                print(f"  Química:    {result[49]}")
                print(f"  História:   {result[50]}")
                print(f"  Sociologia: {result[51]}")
>>>>>>> Stashed changes
=======
                print(f"              (1ªUnidade ),    (2ªUnidade ),    (3ªUnidade )")
                print(f"  Português:     {result[15]}              {result[25]}              {result[35]}")
                print(f"  Matemática:    {result[16]}              {result[26]}              {result[36]}")
                print(f"  Biologia:      {result[17]}              {result[27]}              {result[37]}")
                print(f"  Física:        {result[18]}              {result[28]}              {result[38]}")
                print(f"  Inglês:        {result[19]}              {result[29]}              {result[39]}")
                print(f"  Filosofia:     {result[20]}              {result[30]}              {result[40]}")
                print(f"  Artes:         {result[21]}              {result[31]}              {result[41]}")
                print(f"  Química:       {result[22]}              {result[32]}              {result[42]}")
                print(f"  História:      {result[23]}              {result[33]}              {result[43]}")
                print(f"  Sociologia:    {result[24]}              {result[34]}              {result[44]}")
            
                print("\nMédias Finais:")
                print(f"  Português:  {result[45]}")
                print(f"  Matemática: {result[46]}")
                print(f"  Biologia:   {result[47]}")
                print(f"  Física:     {result[48]}")
                print(f"  Inglês:     {result[49]}")
                print(f"  Filosofia:  {result[50]}")
                print(f"  Artes:      {result[51]}")
                print(f"  Química:    {result[52]}")
                print(f"  História:   {result[53]}")
                print(f"  Sociologia: {result[54]}")
>>>>>>> 4bcd64947ae7db7d3d51dafd82ef5509299b86de
                
    except sqlite3.Error as erro:
        print("Erro ao encontrar aluno", erro)
    finally:
        conexao.conn.close()