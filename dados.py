from cinemassauro import *

def insere_dados_filme_sessao():
    
    try:
        cod_filme = "1234"
        nome_filme = "CDIA"
        categoria_filme = "Terror"
        duracao_filme = 120
        indicacao_etaria = 14
        empresa_produtora = "UFPB"
        nacional_filme = 1
        data_estreia = "2022/12/01"
        lista_dict_atores = [
            {
                "cod_ator": "12341",
                "nome": "Guilherme Iram",
                "idade": 21,
                "sexo": 'M'
            },
            {
                "cod_ator": "12342",
                "nome": "Angela Thais",
                "idade": 22,
                "sexo": 'F'
            },
            {
                "cod_ator": "12343",
                "nome": "Guilherme Pujoni",
                "idade": 22,
                "sexo": "M"
            }
        ]

        cadastra_novo_filme(cod_filme, 
                            nome_filme,
                            categoria_filme,
                            duracao_filme,
                            indicacao_etaria,
                            empresa_produtora,
                            nacional_filme,
                            data_estreia,
                            lista_dict_atores)

        cod_filme = "1235"
        nome_filme = "IA"
        categoria_filme = "Comedia"
        duracao_filme = 100
        indicacao_etaria = 16
        empresa_produtora = "Havard"
        nacional_filme = 0
        data_estreia = "2022/12/03"
        lista_dict_atores = [
            {
                "cod_ator": "12351",
                "nome": "Jose Havard",
                "idade": 21,
                "sexo": 'M'
            },
            {
                "cod_ator": "12342",
                "nome": "Angela Thais",
                "idade": 22,
                "sexo": 'F'
            },
            {
                "cod_ator": "12343",
                "nome": "Guilherme Pujoni",
                "idade": 22,
                "sexo": "M"
            }
        ]

        cadastra_novo_filme(cod_filme, 
                            nome_filme,
                            categoria_filme,
                            duracao_filme,
                            indicacao_etaria,
                            empresa_produtora,
                            nacional_filme,
                            data_estreia,
                            lista_dict_atores)

        cod_sessao = "111"
        cod_filme = "1234"
        num_sala = 1
        id_data = "1234"
        horario_sessao = "20:00:00"
        estreia = 1
        dia_sessao = 1
        mes_sessao = 12
        ano_sessao = 2022


        cadastra_nova_sessao(
            cod_sessao,
            cod_filme,
            num_sala,
            id_data,
            horario_sessao,
            estreia,
            dia_sessao,
            mes_sessao,
            ano_sessao
        )

        cod_sessao = "222"
        cod_filme = "1235"
        num_sala = 1
        id_data = "1235"
        horario_sessao = "18:00:00"
        estreia = 1
        dia_sessao = 5
        mes_sessao = 12
        ano_sessao = 2022


        cadastra_nova_sessao(
            cod_sessao,
            cod_filme,
            num_sala,
            id_data,
            horario_sessao,
            estreia,
            dia_sessao,
            mes_sessao,
            ano_sessao
        )

        cod_sessao = "333"
        cod_filme = "1235"
        num_sala = 2
        id_data = "1236"
        horario_sessao = "14:00:00"
        estreia = 0
        dia_sessao = 1
        mes_sessao = 1
        ano_sessao = 2023


        cadastra_nova_sessao(
            cod_sessao,
            cod_filme,
            num_sala,
            id_data,
            horario_sessao,
            estreia,
            dia_sessao,
            mes_sessao,
            ano_sessao
        )

    except:
        print("Erro na inserção dos dados!")


def insere_dados_compras():
    for n in range(1, 30 + 1):
        com_pedido = 0
        cod_cliente = f"codcliente{n}"
        cpf = f"111.111.111-{n:02}"
        nome_cliente = f"Name{n}"
        idade_cliente = f"{n}"
        sexo_cliente = "F"
        time_cliente = "Fluminense"
        tipo_ingresso = "adulto"
        
        if tipo_ingresso == "estudante":
            estudante = 1
        else:
            estudante = 0
        
        tipo_pagamento = "pix"
        cod_ingresso = f"codingresso{n}"
        cod_sessao = 111

        num_poltrona = n
        
        cod_pedido = f"codpedido{n}"
        
        pedido = {}
        nome_todos_produtos = retorna_nome_produtos()
        for produto in nome_todos_produtos:
            pedido[produto] = 0
        
        if com_pedido:
            opcao = 1
            print("Faca seu pedido! ")
            while opcao:

                exibir_produtos()
                nome_produto = input("Digite o nome do produto que deseja comprar: ").lower().strip()
                qtdade_produto = int(input("Digite a quantidade que deseja comprar desse produto: "))
                try:
                    pedido[nome_produto] += qtdade_produto
                except:
                    print("Algo deu errado no seu pedido! Tente novamente.")
                opcao = int(input("Continuar pedindo? [1 - sim, 0 - nao]"))

            print("Pedido finalizado!") 

        cadastra_compra_cliente(
            cod_cliente,
            cpf,
            idade_cliente,
            nome_cliente,
            sexo_cliente,
            time_cliente,
            estudante,
            cod_ingresso,
            cod_pedido,
            pedido,
            tipo_pagamento,
            cod_sessao,
            num_poltrona,
            tipo_ingresso
        )
    pass

insere_dados_filme_sessao()
insere_dados_compras()