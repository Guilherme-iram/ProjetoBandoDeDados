# Consultas SQL

## 1. DDL - Data Definition Language - Linguagem de Definição de Dados.
- São os comandos que interagem com os objetos do banco.
- São comandos DDL : CREATE, ALTER e DROP.
    
    ### 1.1 Criando tabela Filme
        CREATE TABLE IF NOT EXISTS Filme\
        (cod_filme varCHAR PRIMARY KEY NOT NULL,
        nome_filme varCHAR,
        categoria_filme varCHAR,
        duracao_filme INT,
        indicacao_etaria INT,
        empresa_produtora varCHAR,
        nacional_filme BOOL,
        data_estreia DATE)

    ### 1.2 Criando tabela Participa_Filme_Ator
        CREATE TABLE IF NOT
        EXISTS Participa_Filme_Ator
        (cod_filme varCHAR,
        cod_ator varCHAR)

    ### 1.3 Criando tabela Ator
        CREATE TABLE IF NOT EXISTS Ator
        (cod_ator varCHAR PRIMARY KEY NOT NULL,
        nome_ator varCHAR,
        idade_ator INT,
        sexo_ator CHAR(1))
    
    ### 1.4 Criando tabela Sessao
        CREATE TABLE IF NOT EXISTS Sessao
        (cod_sessao varCHAR PRIMARY KEY NOT NULL,
        cod_filme varCHAR,
        num_sala INT,
        id_data varCHAR, 
        horario_sessao TIME, 
        estreia BOOL)

    ### 1.5 Criando tabela Data
        CREATE TABLE IF NOT EXISTS Data
        (id_data varCHAR PRIMARY KEY NOT NULL,
        dia_sessao SMALLINT,
        mes_sessao SMALLINT, 
        ano_sessao INT)

    ### 1.6 Criando tabela Sala
        CREATE TABLE IF NOT EXISTS Sala
        (num_sala INT PRIMARY KEY NOT NULL,
        capacidade_sala INT)

    ### 1.7 Criando tabela Produto
        CREATE TABLE IF NOT EXISTS Produto
        (cod_produto varCHAR PRIMARY KEY NOT NULL,
        produto varCHAR,
        preco_produto FLOAT)
    
    ### 1.8 Criando tabela Pedido
        CREATE TABLE IF NOT EXISTS Pedido
        (cod_produto varCHAR,
        cod_pedido varCHAR,
        quantidade INT)
    
    ### 1.9 Criando tabela Lanchonete
        CREATE TABLE IF NOT EXISTS Lanchonete
        (cod_pedido INT,
        preco_produto FLOAT,
        cod_produto varCHAR)

    ### 1.10 Criando tabela CLIENTE
        CREATE TABLE IF NOT EXISTS Cliente
        (cod_cliente varCHAR PRIMARY KEY NOT NULL,
        CPF varCHAR,
        idade_cliente SMALLINT,
        nome_cliente varCHAR,
        sexo_cliente CHAR(1),
        time_cliente varCHAR,
        estudante BOOL)
        
    ### 1.11 Criando tabela Compra
        CREATE TABLE IF NOT EXISTS Compra
        (cod_pedido varCHAR,
        cod_ingresso varCHAR,
        cod_cliente varCHAR,
        tipo_pagamento varCHAR)
    
    ### 1.12 Criando tabela Ingresso
        CREATE TABLE IF NOT EXISTS Ingresso
        (cod_ingresso varCHAR PRIMARY KEY NOT NULL,
        cod_sessao varCHAR,
        num_poltrona SMALLINT,
        tipo_ingresso varCHAR,
        preco_ingresso FLOAT)
        
    ### 1.13 Criando tabela Poltrona
        CREATE TABLE IF NOT EXISTS Poltrona
        (cod_sessao varCHAR,
        num_sala INT,
        num_poltrona SMALLINT)
        

## 2. DML - Data Manipulation Language - Linguagem de Manipulação de Dados.
- São os comandos que interagem com os dados dentro das tabelas.
- São comandos DML : INSERT, DELETE e UPDATE. 
    ### 2.1 - Adicionando novo registro a tabela Filme

        INSERT INTO Filme (cod_filme,
        nome_filme,
        categoria_filme,
        duracao_filme,
        indicacao_etaria,
        empresa_produtora,
        nacional_filme,
        data_estreia) VALUES (?, ?, ?, ?, ?, ?, ?, ?))

    ### 2.2 - Adicionando novo registro a tabela Participa_Filme_Ator

        INSERT INTO Participa_Filme_Ator 
        (cod_filme, cod_ator) VALUES (?, ?))

    ### 2.3 - Adicionando novo registro a tabela Ator
        INSERT INTO Ator
        (cod_ator,
        nome_ator, 
        idade_ator, 
        sexo_ator) VALUES (?, ?, ?, ?)

    ### 2.4 - Removendo registro da tabela Filme de acordo com um codigo de filme
        DELETE FROM Filme where cod_filme = ?
    ### 2.5 - Removendo registro da tabela Participa_Filme_Ator de acordo com codigo de filme
        DELETE FROM Participa_Filme_Ator where cod_filme = ?
    ### 2.6 - Adicionando novo registro a tabela Sessao
        INSERT INTO Sessao (cod_sessao,
        cod_filme,
        num_sala,
        id_data,
        horario_sessao,
        estreia) VALUES (?, ?, ?, ?, ?, ?)

    ### 2.7 - Adicionando novo registro a tabela Data
        INSERT INTO Data (id_data,
        dia_sessao,
        mes_sessao,
        ano_sessao) VALUES (?, ?, ?, ?)

    ### 2.7 - Removendo registro da tabela Sessao de acordo com um codigo de sessao
        DELETE FROM Sessao where cod_sessa = ?

    ### 2.8 - Removendo registro da tabela Data de acordo com um id
        DETELE FROM Data where id_data = ?

    ### 2.9 - Adicionando novo registro na tabela Cliente
        INSERT INTO Cliente (cod_cliente, CPF,
        idade_cliente,
        nome_cliente,
        sexo_cliente,
        time_cliente,
        estudante)
        VALUES (?, ?, ?, ?, ?, ?, ?) 

    ### 2.10 - Adicionando novo registro na tabela Pedido
        INSERT INTO Pedido (cod_produto,
        cod_pedido,
        quantidade)
        VALUES (?, ?, ?)

    ### 2.11 - Adicionando novo registro na tabela Lanchonete
        INSERT INTO Pedido (cod_produto,
        cod_pedido,
        quantidade)
        VALUES (?, ?, ?)

    ### 2.12 - Adicionando novo registro na tabela Compra
        INSERT INTO Compra (cod_pedido,
        cod_ingresso,
        cod_cliente,
        tipo_pagamento) VALUES (?, ?, ?, ?)

    ### 2.13 - Adicionando novo registro na tabela Ingresso
        INSERT INTO Ingresso (cod_ingresso,
        cod_sessao,
        num_poltrona,
        tipo_ingresso,
        preco_ingresso)
        VALUES (?, ?, ?, ?, ?)

    ### 2.14 - Removendo registro tabela Cliente de acordo com o código do cliente
        DELETE FROM Cliente where cod_cliente = ?

    ### 2.15 - Removendo registro tabela Pedido de acordo com o código do pedido
        DELETE FROM Pedido where cod_pedido =  ?

    ### 2.16 - Removendo registro tabela Lanchonete de acordo com o código do pedido
        DELETE FROM Lanchonete where cod_pedido = ?

    ### 2.17 - Removendo registro tabela Compra de acordo com o código do pedido
        DELETE FROM Compra where cod_pedido = ?

    ### 2.18 - Removendo registro tabela Ingresso de acordo com o código do ingresso
        DELETE FROM Ingresso where cod_ingresso = ?

    ### 2.19 - Adicionando novo registro a tabela Produto
        INSERT INTO Produto (cod_produto,
        produto,
        preco_produto) VALUES (?, ?, ?)

    ### 2.20 - Adicionando novo registro a tabela Sala
        INSERT INTO Sala (num_sala,
        capacidade_sala) VALUES (?, ?)


## 3. DQL - Data Query Language - Linguagem de Consulta de dados.
- São os comandos de consulta.
- São comandos DQL : SELECT (é o comando de consulta)
- Obs.: Não serão listados SELECTs muito triviais, tais quais 'SELECT * FROM Filme'.
    ### 3.1 - Consulta para listas todos os atores em ordem alfabética e os seus respectivos filmes nos quais atuaram
        SELECT nome_ator, nome_filme FROM
        (SELECT * from (select * from FILME
        INNER JOIN Participa_Filme_Ator ON
        FILME.cod_filme = Participa_Filme_Ator.cod_filme) AS A
        INNER JOIN ATOR AS B ON A.cod_ator = B.cod_ator)
        ORDER BY nome_ator

    ### 3.2 - Consulta para listas todos os atores em ordem alfabética e o numero total de filmes nos quais atuaram
        SELECT  nome_ator, COUNT  (nome_filme) AS
        Numero_de_filmes FROM (SELECT * FROM (SELECT * FROM FILME
        INNER JOIN Participa_Filme_Ator ON FILME.cod_filme = Participa_Filme_Ator.cod_filme) AS A
        INNER JOIN ATOR AS B ON A.cod_ator = B.cod_ator) GROUP BY nome_ator ORDER BY nome_ator

    ### 3.3 - Consulta para listas todas as sessões disponíveis e suas principais informações para o cliente
        SELECT cod_sessao,
        nome_filme,
        num_sala,
        horario_sessao,
        dia_sessao,
        mes_sessao,
        ano_sessao
        FROM
        (SELECT * FROM (SELECT * FROM Data
        AS C INNER JOIN (SELECT * from Filme as A
        INNER JOIN Sessao AS B ON 
        A.cod_filme = B.cod_filme) AS D
        ON C.id_data = D.id_data)) 

    ### 3.4 - Consulta para contabilizar a receita levantada por cada um dos produtos cadastrados
        SELECT cod_produto,
        produto,
        SUM(preco_produto) AS receita_produto
        FROM (SELECT * from Lanchonete AS A INNER JOIN
        produto AS B ON A.cod_produto = B.cod_produto)
        GROUP BY cod_produto

    ### 3.5 - Consulta para contabilizar a receita levantada por cada uma das sessões cadastradas 

        SELECT cod_sessao, SUM(preco_ingresso) as 
        receita_ingresso ROM Ingresso GROUP by cod_sessao