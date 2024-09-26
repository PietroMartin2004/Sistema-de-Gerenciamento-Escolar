import menu_aluno
import menu_pais
import menu_professor
import menu_diretor
import menu_principal
import verificar_senha

def main(): # A função main é o ponto de entrada
    while True: # Um while True para manter em loop até que o usuário escolha a opção de sair.
        opcao = menu_principal.menu()
        # Opções de 1 a 4, o código chama a função correspondente 
        if opcao == '1': # Por exemplo, menu_aluno.aluno() para a opção "Aluno".
            menu_aluno.aluno()

        elif opcao == '2': # menu_pais.pais() para a opção "Pais".
            menu_pais.pais()

        elif opcao == '3': # menu_professor.professor() para a opção "Professor".
            menu_professor.professor()

        elif opcao == '4': # Aqui verificando a senha para ter acesso
            if verificar_senha.verificacao():
                menu_diretor.diretor()
            else:
                continue  # Volta ao menu principal se a senha estiver incorreta

        elif opcao == '5':
            print("Encerrando o programa...")
            break

        else:
            print("Opção inválida. Tente novamente.")

main()