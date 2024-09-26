import datetime


def nascimento():
    global data,mes,ano
    
    try:
        #Solicita ao usuário o dia, mês e ano de nascimento do aluno.
        data = int(input("Informe o dia de nascimento do aluno (DD): "))
        mes = int(input("Informe o mês de nascimento do aluno (MM): "))
        ano = int(input("Informe o ano de nascimento do aluno (YYYY): "))
        
        #Tenta criar um objeto datetime para validar a data informada.
        datetime.datetime(ano, mes, data)
        # Retorna o dia, mês e ano se a data for válida.
        return data,mes,ano
    
    except ValueError:
        #Exibe uma mensagem de erro se a data for inválida.
        print("Erro: Data de nascimento inválida. Verifique se os valores são válidos.")
        #Chama a função novamente para solicitar a entrada de uma nova data.
        nascimento()
