import conexao


def verificar_credenciais():
    global email, senha

    conexao.conectar_banco()

    # Pergunta email e senha

    email = input("Qual o seu email? ")
    senha = input("Qual a sua senha? ")

    # Conecta com o banco

    # Faz a busca

    resultado = conexao.conn.execute('''
    SELECT materia FROM professor WHERE email = ? AND senha = ?
    ''', (email, senha)).fetchone()
    if resultado:
        # Printa o resultado da busca
        print(f"A sua matéria é: {resultado}")
        return email, senha
    else:
        print("Email e senhas inválidas")
        verificar_credenciais()
