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


