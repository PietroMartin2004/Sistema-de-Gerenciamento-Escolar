import conexao


def verificar_credenciais():
<<<<<<< HEAD
    global email, senha
    
    conexao.conectar_banco()
    
    # Pergunta email e senha
    email = input("Qual o seu email? ")
    senha = input("Qual a sua senha? ")
    
    # Faz a busca
=======

 while True:
    global email, senha

    conexao.conectar_banco()

    # Pergunta email e senha

    email = input("Qual o seu email? ")
    senha = input("Qual a sua senha? ")

    # Faz a busca

>>>>>>> 4bcd64947ae7db7d3d51dafd82ef5509299b86de
    resultado = conexao.conn.execute('''
    SELECT materia FROM professor WHERE email = ? AND senha = ?
    ''', (email, senha)).fetchone()

    if resultado:
        # Printa o resultado da busca
        print(f"A sua matéria é: {resultado}")
        return email, senha
<<<<<<< HEAD
    
    else:
        print("Email e senha inválidos")
        verificar_credenciais()
=======

    else:
        print("Email e senhas inválidas")
    break
>>>>>>> 4bcd64947ae7db7d3d51dafd82ef5509299b86de
