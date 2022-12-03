from cinemassauro import *

def insere_dados():
    
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

insere_dados()