def verificacao():
    #Define a senha correta para verificação.
    senha_correta = "escolamoderna123"

    #Solicita ao usuário que insira a senha para verificação.
    senha = input("Insira a senha de verificação: ")

    #Enquanto a senha inserida for diferente da senha correta, executar o codigo de baixo.
    while senha != senha_correta:

        #Informa ao usuário que a senha está incorreta.
        print("Senha incorreta. Voltando ao menu principal.")

        #Retorna False, indicando que a verificação falhou.
        return False
    
    #Se a senha for correta, retorna True, indicando sucesso na verificação.
    return True