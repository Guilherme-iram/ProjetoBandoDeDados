from cinemassauro import *
from time import sleep

def main():
    
    msg_inicial = "\t| BEM VINDO AO CINEMASAURO |"

    print('\t' + "-" * (len(msg_inicial) - 1))
    print(msg_inicial)
    print('\t' + '-' * (len(msg_inicial) - 1))
    
    while True:
        sistema = int(input("\n\t>> Deseja cadastrar/remover ou consultar dados?"\
             "\n\t[1 - cadastrar/remover, 2 - consultar] "))

        if sistema == 1:
            sleep(1)
            print("""
            Escolha uma opção a seguir:

            1 - Cadastrar novo filme.
            2 - Cadastrar nova sessão.
            3 - Remover filme.
            4 - Remover sessão.
            5 - Comprar um ingresso.
            6 - Comprar um ingresso + lanche.
            7 - Cancelar compra
            N - Encerrar programa.

            Obs .: N significa qualquer outro número
            """)

            opcao = int(input("Sua escolha? "))

            if opcao not in range(1, 9):
                break

            if opcao == 1:
                novo_filme()

            if opcao == 2:
                nova_sessao()

            if opcao == 3:
                remove_filme()

            if opcao == 4:
                remove_sessao()

            if opcao == 5:
                compra_ingresso(com_pedido=False)
            
            if opcao == 6:
                compra_ingresso(com_pedido=True)

            if opcao == 7:
                remove_compra()
        
        else:
            sleep(1)
            print("""
            Escolha uma opção a seguir:

            1 - Lista de atores participante dos filmes cadastrados.
            2 - Dados sobre as sessões disponíveis.
            3 - Relatório financeiro do cinema.
            N - Encerrar programa.

            Obs .: N significa qualquer outro número
            """)

            opcao = int(input("Sua escolha? "))

            if opcao not in range(1, 3 + 1):
                break
            
            if opcao == 1:
                querry_atores_filmes()
            elif opcao == 2:
                querry_sessoes_disponiveis()
            elif opcao == 3:
                querry_financeiro()
    
    print("\nPrograma encerrado!")

if __name__ == "__main__":
    main()
