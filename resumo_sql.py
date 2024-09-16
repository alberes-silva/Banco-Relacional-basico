# -*- coding: utf-8 -*-
"""Resumo_SQL.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1LsMetotw1wwyzXYstlHneEUZ-T71Royo

##**Comandos SQL**##

#*SELECT*#
"""

#Seleciona todas as informações da tabela
SELECT * FROM nome_da_tabela;

#Selecionando apenas uma coluna
SELECT nome_da_coluna FROM nome _da_tabela;

#Selecionando registro distinto (Sem repetição)
SELECT DISTINCT nome_da_coluna FROM nome_da_tabela;

#Selecionando mais de uma coluna da mesma tabela
SELECT nome_da_coluna1, nome_da_coluna2 FROM nome_da_tabela;

"""#*WHERE, AND, OR, NOT*#"""

#Como o WHERE (onde) eu consigo realizar uma condição de busca
SELECT * FROM nome_da_tabela WHERE nome_da_coluna = 'oquequerencontrar'; #(<, >, <=, >=, =)

#Utilizando o WHERE com o auxilio do AND (e)
SELECT * FROM nome_da_tabela WHERE nome_da_coluna = 'opcao' AND nome_da_coluna = 'opcao';

#Utilizando o WHERE com o auxilio do OR (ou)
SELECT * FROM nome_da_tabela WHERE nome_da_coluna = 'opcao' OR nome_da_coluna = 'opcao';

#Utilizando o WHERE com o auxilio do AND(e) e OR (ou)
SELECT * FROM nome_da_tabela WHERE nome_da_coluna = 'opcao' AND (nome_da_coluna = 'opcao' OR nome_da_coluna = 'opcao');

#Utilizando o WHERE com o auxilio do NOT(não)
SELECT * FROM nome_da_tabela WHERE NOT nome_da_coluna = 'opcao' AND NOT nome_da_coluna = 'opcao';

"""#*ORDER BY*#"""

#Ordena as colunas crescente
SELECT * FROM nome_da_tabela ORDER BY nome_da_coluna;

#Ordena as colunas decrescente
SELECT * FROM nome_da_tabela ORDER BY nome_da_coluna DESC;

#Ordena as colunas selecionando duas colunas
SELECT * FROM nome_da_tabela ORDER BY nome_da_coluna, nome_da_coluna;

#Ordena as colunas selecionando duas colunas uma de forma crescente e outra decrescente
SELECT * FROM nome_da_tabela ORDER BY nome_da_coluna ASC, nome_da_coluna DESC;

"""#*INSERT INTO*#"""

#Inserindo valores nas tabelas
INSERT INTO nome_da_tabela (nome_da_coluna, nome_da_coluna) VALUES (valores, valores);

"""#*UPDATE*#"""

#Serve para atualizar informações dentro de uma coluna
UPDATE nome_da_coluna SET 'campo_a_alterar' = 'novo_campo' WHERE oID = valor;

"""#*DELETE*#"""

#Deleta a informação dentro de uma coluna
DELETE FROM nome_da_tabela WHERE nome_da_coluna = 'opcao';

"""#**EXERCÍCIO**#

Dadas as tabelas representadas abaixo, responda as questões SQL que seguem. Funcionários (Codigo, PrimeiroNome, SegundoNome, UltimoNome, DataNasci, CPF, RG, Endereco, CEP, Cidade, Fone, CodigoDepartamento, Funcao, Salario) Departamentos (Codigo, Nome, Localizacao, CodigoFuncionarioGerente)

 1.Listar nome e sobrenome ordenado por sobrenome

2.Listar todos os campos de funcionários ordenados por cidade

 3.Liste a data de nascimento e o primeiro nome dos funcionários ordenados do mais novo para o mais velho

4.Liste os funcionários como uma listagem telefônica

5.Liste o nome, o nome do departamento e a função de todos os funcionários

#*MIN E MAX*#
"""

#Encontrado o valor mínimo de uma coluna
SELECT MIN(nome_da_coluna) AS valorMinino FROM nome_da_tabela;

#Encontrado o valor máximo de uma coluna
SELECT MAX(nome_da_coluna) AS valorMaximo FROM nome_da_tabela;

"""#*COUNT, AVG, SUM*#"""

#Contando os registro de uma tabela
SELECT COUNT(nome_do_registro) AS contagem FROM nome_da_tabela

#Média dos valores de uma coluna
SELECT AVG(nome_do_COLUNA) AS media FROM nome_da_tabela

#Soma dos valores de uma coluna
SELECT SUM(nome_do_COLUNA) AS quantidade FROM nome_da_tabela

"""#*LIKE*#"""

#Serve para auxiliar o where
SELECT * FROM nome_da_tabela WHERE nome_da_coluna LIKE 'oque pretende usar'
#Sempre usa o LIKE COM %.
--LIKE e NOT LIKE

SELECT * FROM EMPREGADO WHERE NOME LIKE 'J%'

SELECT * FROM EMPREGADO WHERE NOME LIKE '%ta'

SELECT * FROM EMPREGADO WHERE NOME LIKE '%ta%'

SELECT * FROM EMPREGADO WHERE NOME LIKE '_ose'

SELECT * FROM EMPREGADO WHERE NOME LIKE '_____'

SELECT * FROM EMPREGADO WHERE NOME LIKE '__se%'

SELECT * FROM EMPREGADO WHERE NOME LIKE '_os%e'

SELECT * FROM EMPREGADO WHERE NOME LIKE '[^ABC]%'

"""#*IN*#"""

#Quando quer especificar algo dentro de uma consulta
SELECT * FROM nome_da_tabela WHERE nome_da_coluna IN ('opção1','opção2',..'opçãon');

SELECT * FROM nome_da_tabela WHERE nome_da_coluna NOT IN ('opção1','opção2',..'opçãon');

SELECT * FROM nome_da_tabela WHERE nome_da_coluna IN (SELECT nome_da_coluna FROM nome_da_tabela2);

"""#*BETWEEN*#"""

#Auxilia na seleção entre dois valores
SELECT * FROM nome_da_tabela WHERE nome_da_coluna 10 BETWEEN 20;

SELECT * FROM nome_da_tabela WHERE nome_da_coluna 10 BETWEEN 20 AND nome_da_coluna NOT IN ('opção1','opção2',..'opçãon');

#Com Strings
SELECT * FROM nome_da_tabela WHERE nome_da_coluna 'string' BETWEEN 'string2' ORDER BY nome_da_coluna;

#Com datas
SELECT * FROM nome_da_tablea WHERE nome_da_coluna BETWEEN '1996-07-01' AND '1996-07-31';

"""#*INNER JOIN*#"""

#Retorna apenas as linhas que têm correspondências em ambas as tabelas.
SELECT nome_da_tabela.nome_da_coluna, nome_da_tabela2.nome_da_coluna
FROM nome_da_tabela
INNER JOIN nome_da_tabela2 ON nome_da_colunaID = nome_da_coluna2ID;

"""#*LEFT JOIN*#"""

#LEFT JOIN (ou LEFT OUTER JOIN): Retorna todas as linhas da tabela à esquerda e
#as linhas correspondentes da tabela à direita. Se não houver correspondência,
#os resultados conterão NULL para as colunas da tabela à direita.

SELECT customers.CustomerName, orders.OrderID FROM customers
LEFT JOIN orders ON customers.CustomerID = orders.CustomerID
order by customers.CustomerName

"""#*RIGHT JOIN*#"""

#RIGHT JOIN (ou RIGHT OUTER JOIN): Retorna todas as linhas da tabela à direita e
#as linhas correspondentes da tabela à esquerda. Se não houver correspondência,
#os resultados conterão NULL para as colunas da tabela à esquerda.

SELECT  orders.OrderID, employees.LastName,employees.FirstName FROM orders
RIGHT JOIN employees ON orders.EmployeeID = employees.EmployeeID
order by orders.OrderID

"""#*CROSS JOIN*#"""

#CROSS JOIN: Retorna o produto cartesiano das linhas das tabelas envolvidas,
# ou seja, todas as combinações possíveis de linhas.

SELECT customers.CustomerName, orders.OrderID FROM customers CROSS JOIN orders;

SELECT customers.CustomerName, orders.OrderID FROM customers CROSS JOIN orders WHERE
customers.CustomerID = orders.CustomerID;

"""#*STORED PROCEDURES*#"""

#São trechos de códigos que serão salvos e reutilizados depois
CREATE PROCEDURE SelectAllCustomer()
SALECT * FROM customers

CALL SelectAllCustomer

"""#*CREATE DB*#"""

#criando um banco de dados
CREATE DATABASE nome_do_banco;

use nome_do_banco;

"""#*DROP DB*#"""

#COMO IDENTIFICAR QUAIS BANCO DE DADOS EXISTENTE
SHOW DTABASES;

#Excluindo o banco de dados

DROP DATABASE nome_do_banco;

"""#*CREATE TABLE*#"""

#Criando uma tabela
CREATE TABLE nome_da_tabela (
    informações1 INT,
    informações2 VARCHAR(30),
    informações3 DATE,
    informações4 DECIMAL
);

"""#*ALTER TABLE*#"""

#Alterando a tabela


#Adicionando uma nova coluna
ALTER TABLE nome_da_tabela ADD informação tipo;
#informação ex. email
#tipo VARCHAR(255)

#Excluir uma coluna
ALTER TABLE nome_da_tabela DROP COLUMN nome_da_coluna;

#Alterar o texto
ALTER TABLE nome_da_tabela ADD nome_da_coluna tipo;

"""#*DROP TABLE*#"""

#Excluir tabela

DROP TABLE nome_da_tabela;

#Deleta os dados da tabela
TRUNCATE TABLE nome_da_tabela;

"""#*EXERCÍCIO 02*#

Crie uma base de dados chamada “minha_base_dedados”;

● Insira as tabelas abaixo:

✔ Professor: id, nome, sobrenome, id_disciplina, cpf, senha

✔ Disciplinas: id, nome, id_professor

 ✔ Alunos: id, nome, sobrenome, cpf, senha.

● Insira pelo menos cinco registros em cada tabela.

 ● Adicione a coluna turma, na tabela aluno.

● Exclua as tabelas.

● Exclua o banco de dados.
"""

SELECT * from Autores
SELECT * FROM Livros

SELECT Editora from Livros;
SELECT * FROM Livros ORDER BY Titulo
SELECT Titulo, Editora, Edicao, codAutor FROM Livros ORDER BY Titulo;
SELECT Editora FROM Livros order by editora;
SELECT L.Titulo from Livros L WHERE L.NumeroPagina > 300;
SELECT L.Titulo FROM Livros L WHERE L.NumeroPagina BETWEEN 200 AND 300;
SELECT L.Titulo FROM Livros L WHERE L.Titulo LIKE 'F%';
SELECT A.nome FROM Autores A WHERE A.nome LIKE '%Araújo';
SELECT L.Titulo FROM Livros L WHERE L.Titulo LIKE '%Informática%';
SELECT COUNT (A.codAutor) FROM Autores A;
SELECT COUNT (L.codLivro) FROM Livros L;
SELECT AVG(L.NumeroPagina) FROM Livros L;
SELECT L.Titulo, A.nome FROM Livros L INNER JOIN Autores A ON L.codAutor = A.codAutor;
SELECT MAX(L.Titulo) FROM Livros L;