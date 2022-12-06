import sqlite3
from cinemassauro import cadastrar_novo_produto, cadastrar_sala

def create_tables():
    con = sqlite3.connect('cinemaSauro.db')
    c = con.cursor()

    # Criando tabela FILME
    c.execute(f"CREATE TABLE IF NOT EXISTS Filme"\
        "(cod_filme varCHAR PRIMARY KEY NOT NULL,"\
        "nome_filme varCHAR, "\
        "categoria_filme varCHAR, "\
        "duracao_filme INT, "\
        "indicacao_etaria INT,"\
        "empresa_produtora varCHAR,"\
        "nacional_filme BOOL,"\
        "data_estreia DATE)")

    # Criando tabela Participa_Filme_Ator
    c.execute(f"CREATE TABLE IF NOT EXISTS Participa_Filme_Ator"\
        "(cod_filme varCHAR,"\
        "cod_ator varCHAR)")

    # Criando tabela ATOR
    c.execute(f"CREATE TABLE IF NOT EXISTS Ator"\
        "(cod_ator varCHAR PRIMARY KEY NOT NULL,"\
        "nome_ator varCHAR, "\
        "idade_ator INT, "\
        "sexo_ator CHAR(1))")

    # Criando tabela SESSAO
    c.execute(f"CREATE TABLE IF NOT EXISTS Sessao"\
        "(cod_sessao varCHAR PRIMARY KEY NOT NULL,"\
        "cod_filme varCHAR, "\
        "num_sala INT, "\
        "id_data varCHAR, "\
        "horario_sessao TIME, "\
        "estreia BOOL)")

    # Criando tabela DATA
    c.execute(f"CREATE TABLE IF NOT EXISTS Data"\
        "(id_data varCHAR PRIMARY KEY NOT NULL,"\
        "dia_sessao SMALLINT, "\
        "mes_sessao SMALLINT, "\
        "ano_sessao INT)"\
        )

    # Criando tabela SALA
    c.execute(f"CREATE TABLE IF NOT EXISTS Sala"\
        "(num_sala INT PRIMARY KEY NOT NULL,"\
        "capacidade_sala INT)"
        )

    # tabela PRODUTO
    c.execute(f"CREATE TABLE IF NOT EXISTS Produto"\
        "(cod_produto varCHAR PRIMARY KEY NOT NULL,"\
        "produto varCHAR,"\
        "preco_produto FLOAT)"
        )

    # tabela PEDIDO
    c.execute(f"CREATE TABLE IF NOT EXISTS Pedido"\
        "(cod_produto varCHAR,"\
        "cod_pedido varCHAR,"\
        "quantidade INT)"
        )

    # tabela LANCHONETE
    c.execute(f"CREATE TABLE IF NOT EXISTS Lanchonete"\
        "(cod_pedido INT,"\
        "preco_produto FLOAT,"\
        "cod_produto varCHAR)"
        )

    # tabela CLIENTE
    c.execute(f"CREATE TABLE IF NOT EXISTS Cliente"\
        "(cod_cliente varCHAR PRIMARY KEY NOT NULL,"\
        "CPF varCHAR,"\
        "idade_cliente SMALLINT,"\
        "nome_cliente varCHAR,"\
        "sexo_cliente CHAR(1),"\
        "time_cliente varCHAR,"\
        "estudante BOOL)"
        )

    # tabela COMPRA
    c.execute(f"CREATE TABLE IF NOT EXISTS Compra"\
        "(cod_pedido varCHAR,"\
        "cod_ingresso varCHAR,"\
        "cod_cliente varCHAR,"\
        "tipo_pagamento varCHAR)"
        )


    # tabela INGRESSO
    c.execute(f"CREATE TABLE IF NOT EXISTS Ingresso"\
        "(cod_ingresso varCHAR PRIMARY KEY NOT NULL,"\
        "cod_sessao varCHAR,"\
        "num_poltrona SMALLINT,"\
        "tipo_ingresso varCHAR,"\
        "preco_ingresso FLOAT)"
        )

    # Criando tabela Poltrona
    c.execute(f"CREATE TABLE IF NOT EXISTS Poltrona"\
        "(cod_sessao varCHAR,"\
        "num_sala INT,"\
        "num_poltrona SMALLINT)"
        )

    for n in range(1, 45 + 1):
        cadastrar_sala(n, 50)
    
    cadastrar_novo_produto("111", "pipoca", 3.00)
    cadastrar_novo_produto("222", "coca-cola lata", 4.50)
    cadastrar_novo_produto("333", "barra chocolate", 2.50)

    con.commit()

reiniciar = int(input("Reiniciar banco de dados? "))

if reiniciar:
    con = sqlite3.connect('cinemaSauro.db')
    c = con.cursor()
    c.execute("DROP TABLE Filme")
    c.execute("DROP TABLE Participa_Filme_Ator")
    c.execute("DROP TABLE Ator")
    c.execute("DROP TABLE Sessao")
    c.execute("DROP TABLE Data")
    c.execute("DROP TABLE Sala")
    c.execute("DROP TABLE Produto")
    c.execute("DROP TABLE Lanchonete")
    c.execute("DROP TABLE Cliente")
    c.execute("DROP TABLE Pedido")
    c.execute("DROP TABLE Compra")
    c.execute("DROP TABLE Ingresso")
    c.execute("DROP TABLE Poltrona")
    con.commit()
    c.close()

    print("Bando de reiniciado!")

create_tables()
