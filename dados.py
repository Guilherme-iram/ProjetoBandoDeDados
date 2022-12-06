from cinemassauro import *
from random import randint

def insere_dados_filme_sessao():
    
    try:
        cod_filme = "1234"
        nome_filme = "Sousa Park 1: Dinossauros em acao"
        categoria_filme = "Acao"
        duracao_filme = 120
        indicacao_etaria = 14
        empresa_produtora = "Sousa Producoes"
        nacional_filme = 1
        data_estreia = "2022/01/01"
        lista_dict_atores = [
            {
                "cod_ator": "12341",
                "nome": "Marcelo Yuri",
                "idade": 40,
                "sexo": 'M'
            },
            {
                "cod_ator": "12342",
                "nome": "Mirelly Alves",
                "idade": 22,
                "sexo": 'F'
            },
            {
                "cod_ator": "12343",
                "nome": "Neymar Jr",
                "idade": 30,
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
        nome_filme = "Sousa Park 2: A vingança de Acressauro"
        categoria_filme = "Acao"
        duracao_filme = 200
        indicacao_etaria = 16
        empresa_produtora = "Sousa Producoes"
        nacional_filme = 1
        data_estreia = "2022/06/01"
        lista_dict_atores = [
            {
                "cod_ator": "12351",
                "nome": "Marcelo Yuri",
                "idade": 40,
                "sexo": 'M'
            },
            {
                "cod_ator": "12352",
                "nome": "Mirelly Alves",
                "idade": 22,
                "sexo": 'F'
            },
            {
                "cod_ator": "12353",
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

        cod_filme = "1236"
        nome_filme = "Sousa Park 3: Nova esperança pre-histórica"
        categoria_filme = "Acao"
        duracao_filme = 200
        indicacao_etaria = 16
        empresa_produtora = "Sousa Producoes"
        nacional_filme = 1
        data_estreia = "2022/12/01"
        lista_dict_atores = [
            {
                "cod_ator": "12361",
                "nome": "Marcelo Yuri",
                "idade": 40,
                "sexo": 'M'
            },
            {
                "cod_ator": "12362",
                "nome": "Mirelly Alves",
                "idade": 22,
                "sexo": 'F'
            },
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
        
        cod_filme = "1237"
        nome_filme = "Sousa Park: Rex One"
        categoria_filme = "Drama"
        duracao_filme = 220
        indicacao_etaria = 18
        empresa_produtora = "Sao Jose Estudio"
        nacional_filme = 0
        data_estreia = "2022/12/03"
        lista_dict_atores = [
            {
                "cod_ator": "12371",
                "nome": "Neymar Jr",
                "idade": 31,
                "sexo": 'M'
            },
            {
                "cod_ator": "12372",
                "nome": "Richalisson Pombo",
                "idade": 25,
                "sexo": 'M'
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
        id_data = "1233454"
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
        cod_filme = "1234"
        num_sala = 1
        id_data = "1233455"
        horario_sessao = "23:00:00"
        estreia = 1
        dia_sessao = 12
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
        id_data = "12365476"
        horario_sessao = "16:00:00"
        estreia = 0
        dia_sessao = 1
        mes_sessao = 2
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

        cod_sessao = "444"
        cod_filme = "1236"
        num_sala = 2
        id_data = "123642323"
        horario_sessao = "22:00:00"
        estreia = 0
        dia_sessao = 1
        mes_sessao = 2
        ano_sessao = 2024


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

        cod_sessao = "555"
        cod_filme = "1237"
        num_sala = 3
        id_data = "123623253"
        horario_sessao = "08:00:00"
        estreia = 0
        dia_sessao = 2
        mes_sessao = 2
        ano_sessao = 2025


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

    nomes_masculinos = ["Carlos", "Eduardo", "Gustavo", "Renato", "Daniel", "Davi", "Neymar"]
    nomes_femininos = ["Ana", "Thereza", "Carla", "Izabell", "Maria", "Marta", "Madalena"]
    sobrenomes = ["Araujo", "Silva", "Costa", "Montenegro", "De Jesus", "Dos Anjos", "Jr"]
    tipo_pagamentos = ["pix", "dinheiro", "bitcoin", "cartao"]
    times = ["flamengo", "vasco", "corintias", "palmeiras", "bota fogo", "brasil"]
    sexo = ["M", "F"]
    sessoes = ["111", "222", "333", "444", "555"]

    for n in range(1, 30 + 1):
        com_pedido = randint(0, 1)
        cod_cliente = f"{n * randint(1000, 9999)}"
        cpf = f"{randint(1000000000, 9999999999)}"
        sexo_cliente = sexo[randint(0, 1)]
        if sexo_cliente == "M":
            len_nome = len(nomes_masculinos) - 1
            len_sobre = len(sobrenomes) - 1
            nome_cliente = nomes_masculinos[randint(0, len_nome)] + " " + sobrenomes[randint(0, len_sobre)]

        else:
            len_nome = len(nomes_femininos) - 1
            len_sobre = len(sobrenomes) - 1
            nome_cliente = nomes_femininos[randint(0, len_nome)] + " " + sobrenomes[randint(0, len_sobre)]
        
        idade_cliente = randint(3, 120)
        len_times = len(times) - 1
        time_cliente = times[randint(0, len_times)]

        if idade_cliente <= 16:
            tipo_ingresso = "infantil"
        elif idade_cliente <= 60:
            tipo_ingresso = "adulto"
        else:
            tipo_ingresso = "idoso"
        
        if randint(0, 1) == 1:
            tipo_ingresso = "estudante"

        if tipo_ingresso == "estudante":
            estudante = 1
        else:
            estudante = 0
        
        len_pag = len(tipo_pagamentos) - 1
        tipo_pagamento = tipo_pagamentos[randint(0, len_pag)]
        cod_ingresso = f"{n * randint(1000, 9999)}"
        
        len_sessoes = len(sessoes) - 1
        cod_sessao = sessoes[randint(0, len_sessoes)]

        num_poltrona = n
        
        cod_pedido = f"cod_pedido{n * randint(1, 100)}"
        
        pedido = {}

        nome_todos_produtos = retorna_nome_produtos()
        len_produtos = len(nome_todos_produtos) - 1
        for produto in nome_todos_produtos:
            pedido[produto] = 0
        
        if com_pedido:
            opcao = 1
            while opcao:

                nome_produto = nome_todos_produtos[randint(0, len_produtos)]
                qtdade_produto = randint(0, 5)
                pedido[nome_produto] += qtdade_produto
                opcao = randint(0, 1)
            

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

insere_dados_filme_sessao()
insere_dados_compras()