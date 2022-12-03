import sqlite3

from func_auxiliares import *


def cadastra_novo_filme(cod_filme, 
                        nome_filme,
                        categoria_filme,
                        duracao_filme,
                        indicacao_etaria,
                        empresa_produtora,
                        nacional_filme,
                        data_estreia,
                        lista_dict_atores):

    con = sqlite3.connect('cinemaSauro.db')
    c = con.cursor()

    all_cod_filme = []
    c.execute(f"SELECT cod_filme FROM Filme")
    for raw in c.fetchall():
        all_cod_filme.append(raw[0])
    
    if cod_filme in all_cod_filme:
        print("Código de filme já cadastrado no sistema!")
        con.commit()
        return
    
    c.execute("INSERT INTO Filme (cod_filme,"\
              "nome_filme,"\
              "categoria_filme,"\
              "duracao_filme,"\
              "indicacao_etaria,"\
              "empresa_produtora,"\
              "nacional_filme,"\
              "data_estreia) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", 
                (cod_filme,
                nome_filme,
                categoria_filme,
                duracao_filme,
                indicacao_etaria,
                empresa_produtora,
                nacional_filme,
                data_estreia))
    
    for dict_ator in lista_dict_atores:
        
        c.execute("INSERT INTO Participa_Filme_Ator"\
                    "(cod_filme,"\
                    "cod_ator) VALUES (?, ?)",
                    (cod_filme,
                    dict_ator['cod_ator']))
        
        all_cod_ator = []
        c.execute(f"SELECT cod_ator FROM Ator")
        for raw in c.fetchall():
            all_cod_ator.append(raw[0])

            
        if dict_ator['cod_ator'] not in all_cod_ator:
            c.execute("INSERT INTO Ator"\
                        "(cod_ator,"\
                        "nome_ator, "\
                        "idade_ator, "\
                        "sexo_ator) VALUES (?, ?, ?, ?)",
                            (dict_ator['cod_ator'],
                             dict_ator['nome'],
                             dict_ator['idade'],
                             dict_ator['sexo']))

    con.commit()

def novo_filme():

    print("Cadastre um novo filme: ")

    cod_filme = input("Codigo filme: ").strip()
    nome_filme = input("Nome filme: ").strip()
    categoria_filme = input("Categoria Filme: ").strip()
    duracao_filme = int(input("Duracao Filme: (mintos) "))
    indicacao_etaria = int(input("Indicacao etaria Filme: "))
    empresa_produtora = input("Empresa Produtora filme: ")
    nacional_filme = int(input("Filme Nacional? [Sim - 1, Nao - 0] "))
    dia, mes, ano = input("Data de estreia: [dd/mm/aaaa] ").split("/")
    data_estreia = f"{ano}/{mes}/{dia}"
    n_atores = int(input("Quantos atores no filme? "))

    for i in range(1, n_atores + 1):
        cod_ator = input(f"Código ator/atriz {i}: ")
        nome_ator = input(f"Nome ator/atriz {i}: ")
        idade_ator = int(input(f"Idade ator/atriz {i}: "))
        sexo_ator = input(f"Sexo ator/atriz {i}: [M - Masculino, F - Feminino] ").upper().strip()[0]
        lista_dict_atores.append(
            {
                "cod_ator": cod_ator,
                "nome": nome_ator,
                "idade": idade_ator,
                "sexo": sexo_ator
            }
        )

    cadastra_novo_filme(cod_filme, 
                        nome_filme,
                        categoria_filme,
                        duracao_filme,
                        indicacao_etaria,
                        empresa_produtora,
                        nacional_filme,
                        data_estreia,
                        lista_dict_atores)

def deleta_filme(nome_filme="", cod_filme=""):
    
    try:
        con = sqlite3.connect('cinemaSauro.db')
        c = con.cursor()

        if nome_filme != "":

            cod = 0
            c.execute(f"SELECT nome_filme,  cod_filme FROM Filme where nome_filme = '{nome_filme}'")
            for raw in c.fetchall():
                _, cod = raw
            c.execute(f"DELETE FROM Filme where cod_filme = '{cod}'")
            c.execute(f"DELETE FROM Participa_Filme_Ator where cod_filme = '{cod}'")
            c.execute(f"SELECT cod_sessao, id_data, cod_filme from Sessao where cod_filme = '{cod}'")
            for raw in c.fetchall():
                cod_sessao = raw[0]
                id_data = raw[1]
                c.execute(f"DELETE FROM Sessao where cod_sessa = '{cod_sessao}'")
                c.execute(f"DETELE FROM Data where id_data = '{id_data}'")
            con.commit()
            return

        if cod_filme != "":
            c.execute(f"DELETE FROM Filme where cod_filme = '{cod_filme}'")
            c.execute(f"DELETE FROM Participa_Filme_Ator where cod_filme = '{cod_filme}'")
            c.execute(f"SELECT cod_sessao, id_data, cod_filme from Sessao where cod_filme = '{cod_filme}'")
            for raw in c.fetchall():
                cod_sessao = raw[0]
                id_data = raw[1]
                c.execute(f"DELETE FROM Sessao where cod_sessa = '{cod_sessao}'")
                c.execute(f"DETELE FROM Data where id_data = '{id_data}'")
            con.commit()
            
    except:
        print("Problema na remossao!")

def remove_filme():

    opcao = int(input("Remover o filme pelo nome do filme ou pelo código do filme? [1 - nome, 2 - codigo]"))

    if opcao == 1:
        nome_filme = input("Qual o nome do filme que deseja remover? ")
        deleta_filme(nome_filme=nome_filme)

    elif opcao == 2:
        cod_filme = input("Qual o código do filme que deseja remover? ")
        deleta_filme(cod_filme=cod_filme)
    
    else:
        print("Opcao inválida!")
        return

    print("Filme removido com sucesso!")

def cadastra_nova_sessao(cod_sessao,
                        cod_filme,
                        num_sala,
                        id_data,
                        horario_sessao,
                        estreia,
                        dia,
                        mes,
                        ano):
    
    con = sqlite3.connect('cinemaSauro.db')
    c = con.cursor()
    
    c.execute("SELECT cod_sessao FROM Sessao")
    all_cod_sessao = []
    for raw in c.fetchall():
        all_cod_sessao.append(raw[0])
    
    c.execute("SELECT cod_filme FROM Filme")
    all_cod_filmes = []
    for raw in c.fetchall():
        all_cod_filmes.append(raw[0])
    
    c.execute("SELECT num_sala FROM Sala")
    all_num_sala = []
    for raw in c.fetchall():
        all_num_sala.append(raw[0])
    
    if cod_sessao in all_cod_sessao:
        print("Código de sessão duplicado!")
        return
    
    elif cod_filme not in all_cod_filmes:
        print("Filme não cadastrado no cinema para se criar uma sessao!")
        return
    
    elif num_sala not in all_num_sala:
        print("Sala não existe e/ou não está disponível para sessão!")
        return
    
    else:
        print("Criando sessao ...")
    
        c.execute("INSERT INTO Sessao (cod_sessao,"\
                  "cod_filme,"\
                  "num_sala,"\
                  "id_data,"\
                  "horario_sessao,"\
                  "estreia) VALUES (?, ?, ?, ?, ?, ?)", 
                    (cod_sessao,
                    cod_filme,
                    num_sala,
                    id_data,
                    horario_sessao,
                    estreia))
        
        c.execute("INSERT INTO Data (id_data,"\
                  "dia_sessao,"\
                  "mes_sessao,"\
                  "ano_sessao) VALUES (?, ?, ?, ?)", 
                    (id_data,
                    dia,
                    mes,
                    ano))
        
        con.commit()

def nova_sessao():

    cod_sessao = input("Digite o codigo da sessao: ").strip()
    cod_filme = input("Digite o codigo do filme: ").strip()
    num_sala = int(input("Digite o número da sala para alocar nessa sessão: [1, 45] "))
    horario_sessao = input("Digite o horario dasessao: [HH:MM] ")
    horario_sessao += ":00"
    data_sessao = input("Digite a data da sessao: [DD/MM/YYYY] ")
    dia_sessao, mes_sessao, ano_sessao = data_sessao.split('/')
    dia_sessao, mes_sessao, ano_sessao = int(dia_sessao), int(mes_sessao), int(ano_sessao)
    id_data = input("Digite o id da data: ")
    estreia = int(input("Essa sessao eh uma estreia? [1 - sim, 0 - nao] "))

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

def deleta_sessao(cod_sessao):

    con = sqlite3.connect('cinemaSauro.db')
    c = con.cursor()

    id_data = None
    c.execute(f"SELECT id_data, cod_sessao FROM sessao WHERE cod_sessao = '{cod_sessao}'")
    for raw in c.fetchall():
        id_data = raw[0]
    c.execute(f"DELETE FROM Sessao where cod_sessao = '{cod_sessao}'")
    c.execute(f"DELETE FROM Data where id_data = '{id_data}'")

    con.commit()

def remove_sessao():
    
    cod_sessao = input("Digite o codigo da sessao a ser cancelada: ").strip()
    deleta_sessao(cod_sessao)

def cadastra_compra_cliente(
    cod_cliente,
    CPF,
    idade_cliente,
    nome_cliente,
    sexo_cliente,
    time_cliente,
    estudante, 
    cod_ingresso,
    cod_pedido,
    pedido,
    tipo_pagamento_ingresso,
    cod_sessao,
    num_poltrona,
    tipo_ingresso
    ):

    con = sqlite3.connect('cinemaSauro.db')
    c = con.cursor()

    c.execute("SELECT cod_cliente from Cliente")
    for raw in c.fetchall():
        if raw[0] == cod_cliente:
            print("Código de cliente já cadastrado!")
            return
        
    c.execute("SELECT cod_ingresso from Ingresso")
    for raw in c.fetchall():
        if raw[0] == cod_ingresso:
            print("Código de ingresso já cadastrado!")
            return
    
    c.execute("SELECT cod_pedido from Pedido")
    for raw in c.fetchall():
        if raw[0] == cod_pedido:
            print("Código de pedido já cadastrado!")
            return
    
    list_pedido = []
    c.execute("SELECT cod_produto, produto from Produto")
    for raw in c.fetchall():
        for k, v in pedido.items():
            if raw[1] == k:
                list_pedido.append([raw[0], v])
    
    c.execute("INSERT INTO Cliente (cod_cliente, CPF,"\
              "idade_cliente, nome_cliente, sexo_cliente,"\
              "time_cliente, estudante)"\
              " VALUES (?, ?, ?, ?, ?, ?, ?)", (cod_cliente, CPF,\
              idade_cliente, nome_cliente, sexo_cliente, time_cliente, estudante))

    for pedido in list_pedido:
        c.execute("INSERT INTO Pedido (cod_produto, cod_pedido, quantidade)"\
                 "VALUES (?, ?, ?)", (pedido[0], cod_pedido, pedido[1]))
        
        preco_pedido = 0
        c.execute(f"SELECT preco_produto, cod_produto from Produto where cod_produto = '{pedido[0]}'")
        for raw in c.fetchall():
            preco_pedido = float(raw[0]) * pedido[1]
            
            c.execute("INSERT INTO lanchonete (cod_pedido, preco_produto, cod_produto)"\
                     "VALUES (?, ?, ?)", (cod_pedido, preco_pedido, pedido[0]))
        
    c.execute("INSERT INTO Compra (cod_pedido, cod_ingresso, cod_cliente, tipo_pagamento) VALUES (?, ?, ?, ?)",\
               (cod_pedido, cod_ingresso, cod_cliente, tipo_pagamento_ingresso))
    
    preco_ingresso = 50
    
    if tipo_ingresso.lower() == "adulto":
        pass
    
    elif tipo_ingresso.lower() in ["estudante", "idoso"]:
        preco_ingresso = preco_ingresso / 2
    
    elif tipo_ingresso.lower() == "infantil":
        preco_ingresso = preco_ingresso / 4
    
    elif time_cliente.lower() == "flamengo":
        preco_ingresso = 0
        
    c.execute("INSERT INTO Ingresso (cod_ingresso,  cod_sessao,"\
             "num_poltrona, tipo_ingresso, preco_ingresso)"\
            " VALUES (?, ?, ?, ?, ?)",\
             (cod_ingresso, cod_sessao, num_poltrona, tipo_ingresso, preco_ingresso))
    
    con.commit()

def compra_ingresso(com_pedido = False):

    cod_cliente = input("Código do cliente: ").strip()
    cpf = input("CPF do cliente: [apenas numeros] ").strip()
    nome_cliente = input("Nome do cliente: ").strip()
    idade_cliente = int(input("Idade do cliente: "))
    sexo_cliente = input("Sexo do cliente: [M - masculino, F - feminisno] ")[0].upper().strip()
    time_cliente = input("Time do cliente: [flamengo = ingresso gratis] ").lower().strip()
    tipo_ingresso = input("Qual o tipo de ingresso do cliente? [infantil, estudante, adulto, idoso, flamengo] ").lower().strip()
    
    if tipo_ingresso == "estudante":
        estudante = 1
    else:
        estudante = 0
    
    tipo_pagamento = input("Qual o meio de pagamento do cliente? [cartao, pix, dinheiro, bitcoin] ").lower().strip()
    cod_ingresso = input("Insira o código do ingresso: ")
    exibir_sessoes()
    cod_sessao = input("Escolha o codigo de uma das sessoes disponiveis: ")
    num_poltrona = int(input("Digite o numero da poltrona: "))
    
    cod_pedido = input("Digite o codigo do pedido: ")
    
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
    msg_voucher = "-> VOUCHER da compra <-"
    len_msg = len(msg_voucher) - 1
    print("-" * len_msg)
    print(msg_voucher)
    print("-" * len_msg)
    print(f"Cod. cliente: {cod_cliente}")
    print(f"Cod. sessao: {cod_sessao}")
    print(f"Cod. pedido: {cod_pedido}")
    print(f"Cod. ingresso: {cod_ingresso}")
    print(f"Tipo de ingresso: {tipo_ingresso}")
    print(f"Num. poltrona: {num_poltrona}")
    preco_ingresso, preco_pedido, preco_total = custo_total_compra(cod_ingresso, cod_pedido)
    print(f"Preco ingresso: R$ {preco_ingresso:.2f}")
    print(f"Preco pedido: R$ {preco_pedido:.2f}")
    print(f"Preco total: R$ {preco_total:.2f}")
    print("-" * len_msg)

def deleta_compra(cod_cliente):

    try:
        con = sqlite3.connect("cinemaSauro.db")
        c = con.cursor()

        c.execute(f"SELECT cod_ingresso, cod_pedido, cod_cliente from Compra where cod_cliente = '{cod_cliente}'")
        for raw in c.fetchall():
            cod_ingresso, cod_pedido = raw[0], raw[1]

        # Apagando o registro em Cliente
        c.execute("SELECT cod_cliente from Cliente")
        for raw in c.fetchall():
            if raw[0] == cod_cliente:
                c.execute(f"DELETE FROM Cliente where cod_cliente = '{cod_cliente}'")

        # Apagando o registro em Pedido
        c.execute(f"SELECT cod_pedido from Pedido where cod_pedido = '{cod_pedido}'")
        for raw in c.fetchall():
            if raw[0] == cod_pedido:
                c.execute(f"DELETE FROM Pedido where cod_pedido = '{cod_pedido}'")

        # Apagando o registro em Lanchonete
        c.execute(f"SELECT cod_pedido from Lanchonete where cod_pedido = '{cod_pedido}'")
        for raw in c.fetchall():
            if raw[0] == cod_pedido:
                c.execute(f"DELETE FROM Lanchonete where cod_pedido = '{cod_pedido}'")

        # Apagando registro em Compra
        c.execute(f"SELECT cod_pedido from Compra where cod_pedido = '{cod_pedido}'")
        for raw in c.fetchall():
            if raw[0] == cod_pedido:
                c.execute(f"DELETE FROM Compra where cod_pedido = '{cod_pedido}'")

        # Apagando registro em Ingresso
        c.execute(f"SELECT cod_ingresso from Ingresso where cod_ingresso = '{cod_ingresso}'")
        for raw in c.fetchall():
            if raw[0] == cod_ingresso:
                c.execute(f"DELETE FROM Ingresso where cod_ingresso = '{cod_ingresso}'")

        con.commit()
        
    except:
        print("Impossibilitado de remover compra")

def remove_compra():
    cod_cliente = input("Qual o código do cliente que deseja cancelar suas compras?")
    deleta_compra(cod_cliente=cod_cliente)
    print("Compra deletada com sucesso!")

def cadastrar_novo_produto(cod_produto, nome_produto, preco_produto):
    try:
        con = sqlite3.connect('cinemaSauro.db')
        c = con.cursor()
        c.execute("INSERT INTO Produto (cod_produto,"\
                          "produto,"\
                          "preco_produto) VALUES (?, ?, ?)", 
                            (cod_produto,
                             nome_produto,
                            preco_produto))
        con.commit()
    except:
        print("Erro no cadastro de novo produto!")

def cadastrar_sala(num_sala, capacidade_sala):

    try:

        con = sqlite3.connect('cinemaSauro.db')
        c = con.cursor()
        
        c.execute("SELECT num_sala FROM Sala")
        all_num_sala = []
        for raw in c.fetchall():
            all_num_sala.append(raw[0])
            
        if num_sala not in all_num_sala: 
            c.execute("INSERT INTO Sala (num_sala,"\
                        "capacidade_sala) VALUES (?, ?)", 
                            (num_sala,
                            capacidade_sala))
        else:
            print("Número de sala já ocupado!")
            return
        
        con.commit()
    
    except:
        print("Erro no cadastro da nova sala!")