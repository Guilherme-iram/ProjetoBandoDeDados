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

    print("Sessoes disponiveis: \n")

    con = sqlite3.connect('cinemaSauro.db')
    c = con.cursor()

    c.execute("select cod_sessao, nome_filme, horario_sessao, dia_sessao, mes_sessao, ano_sessao from"\
              "(select * from (select * from Data as C INNER JOIN (select * from Filme as A"\
              " INNER JOIN Sessao as B on A.cod_filme = B.cod_filme) as D on C.id_data = D.id_data))")
    
    dict_sessoes = {
        "cod sessao": [],
        "filme": [],
        "horaio": [],
        "data": []
        }

    for raw in c.fetchall():
        dict_sessoes["cod sessao"].append(raw[0])
        dict_sessoes["filme"].append(raw[1])
        dict_sessoes["horaio"].append(raw[2])
        data_aux = f"{raw[3]:02}/{raw[4]:02}/{raw[5]}"
        dict_sessoes["data"].append(data_aux)

    print(pd.DataFrame(dict_sessoes))

def custo_total_compra(cod_ingresso, cod_pedido):
    
    con = sqlite3.connect('cinemaSauro.db')
    c = con.cursor()

    preco_pedido = 0
    preco_ingresso = 0

    c.execute(f"SELECT sum(preco_produto) as total_compra FROM Lanchonete WHERE cod_pedido = '{cod_pedido}'")
    for raw in c.fetchall():
        preco_pedido = float(raw[0])

    c.execute(f"SELECT preco_ingresso FROM Ingresso WHERE cod_ingresso = '{cod_ingresso}'")
    for raw in c.fetchall():
        preco_ingresso = float(raw[0])

    return preco_ingresso, preco_pedido, preco_ingresso + preco_pedido