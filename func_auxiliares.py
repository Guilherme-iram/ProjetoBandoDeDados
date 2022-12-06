import sqlite3
import pandas as pd

def retorna_nome_produtos():

    con = sqlite3.connect("cinemaSauro.db")
    c = con.cursor()

    nome_produtos = []
    c.execute("SELECT produto From Produto")
    for raw in c.fetchall():
        nome_produtos.append(raw[0])
    
    return nome_produtos

def exibir_produtos():

    con = sqlite3.connect("cinemaSauro.db")
    c = con.cursor()

    dict_produtos = {"Produto": [], "Preco": []}
    c.execute("SELECT produto, preco_produto From Produto")
    print("Ofertas disponíveis!\n")

    for raw in c.fetchall():
        nome_produto, preco_produto = raw[0], raw[1]
        preco_produto = f"R$ {preco_produto:.2f}"
        dict_produtos['Produto'].append(nome_produto)
        dict_produtos['Preco'].append(preco_produto)
    print(pd.DataFrame(dict_produtos))

def exibir_sessoes():

    print("SESSOES DISPONIVEIS\n")

    con = sqlite3.connect('cinemaSauro.db')
    c = con.cursor()

    c.execute("select cod_sessao, nome_filme, num_sala, horario_sessao, dia_sessao, mes_sessao, ano_sessao from"\
              "(select * from (select * from Data as C INNER JOIN (select * from Filme as A"\
              " INNER JOIN Sessao as B on A.cod_filme = B.cod_filme) as D on C.id_data = D.id_data))")
    
    dict_sessoes = {
        "cod sessao": [],
        "filme": [],
        "num. sala:" : [],
        "horaio": [],
        "data": []
        }

    for raw in c.fetchall():
        dict_sessoes["cod sessao"].append(raw[0])
        dict_sessoes["filme"].append(raw[1])
        dict_sessoes["num. sala:"].append(raw[2])
        dict_sessoes["horaio"].append(raw[3])
        data_aux = f"{raw[4]:02}/{raw[5]:02}/{raw[6]}"
        dict_sessoes["data"].append(data_aux)

    print(pd.DataFrame(dict_sessoes))

def custo_total_compra(cod_ingresso, cod_pedido):
    
    con = sqlite3.connect('cinemaSauro.db')
    c = con.cursor()

    preco_pedido = 0
    preco_ingresso = 0

    c.execute(f"SELECT sum(preco_produto) as total_compra FROM Lanchonete WHERE cod_pedido = '{cod_pedido}'")
    for raw in c.fetchall():
        if raw[0] == None:
            continue
        preco_pedido = float(raw[0])

    c.execute(f"SELECT preco_ingresso FROM Ingresso WHERE cod_ingresso = '{cod_ingresso}'")
    for raw in c.fetchall():
        if raw[0] == None:
            continue
        preco_ingresso = float(raw[0])

    return preco_ingresso, preco_pedido, preco_ingresso + preco_pedido

def verifica_poltronas(cod_sessao, num_sala):
    
    con = sqlite3.connect('cinemaSauro.db')
    c = con.cursor()
    
    c.execute(f"select capacidade_sala from Sala where num_sala = '{num_sala}'")
    for raw in c.fetchall():
        capacidade_sala = int(raw[0])
    
    poltronas_ocupadas = []
    c.execute(f"SELECT num_poltrona FROM Poltrona WHERE cod_sessao == '{cod_sessao}' AND num_sala == '{num_sala}'")
    for raw in c.fetchall():
        poltronas_ocupadas.append(int(raw[0]))

    if len(poltronas_ocupadas) > capacidade_sala:
        return False
    else:

        matriz_poltronas = []
        for i in range(5):
            linha = []
            for j in range(10):
                linha.append('O')
            matriz_poltronas.append(linha)

        for poltrona in poltronas_ocupadas:
                    
                    if poltrona <= 10:
                        poltrona_i = 0
                        poltrona_j = poltrona - 1
                    elif poltrona % 10 == 0:
                        poltrona_i = poltrona // 10 - 1
                        poltrona_j = 0
                    else:
                        poltrona_i = poltrona // 10
                        poltrona_j = int(poltrona - (poltrona_i * 10))

                    matriz_poltronas[poltrona_i][poltrona_j] = 'X'
        while True:
            
            print("Poltronas disponíveis: \n")
            print("coluna - ", end='')
            for i in range(1, 10 + 1):
                print(f"{i} ", end='')
            print()
            for i in range(5):
                print(f"fila {i + 1} - ", end='')
                for j in range(10):
                    print(f"{matriz_poltronas[i][j]} ", end='')
                print()
            
            fila_poltrona = int(input("Digite o numero da fila: "))
            coluna_poltrona = int(input("Digite o numero da coluna: "))
            num_poltrona = ((fila_poltrona - 1) * 10) + coluna_poltrona 

            i_fila =  fila_poltrona - 1
            j_coluna =  coluna_poltrona - 1
             
            if (num_poltrona >= capacidade_sala):
                print("\nPoltrona invalida! Tente outra.\n")
            elif matriz_poltronas[i_fila][j_coluna] == 'X':
                print("\nPoltrona invalida! Tente outra.\n")
            else:
                # matriz_poltronas[i_fila][j_coluna] = 'X'
                # for i in range(1, 10 + 1):
                #     print(f"{i} ", end='')
                # print()
                # for i in range(5):
                #     print(f"fila {i + 1} - ", end='')
                #     for j in range(10):
                #         print(f"{matriz_poltronas[i][j]} ", end='')
                #     print()
                # print("Num Poltrona: ", num_poltrona)

                return num_poltrona
