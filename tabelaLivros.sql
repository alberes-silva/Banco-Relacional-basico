CREATE TABLE Livros (
  codLivro INT,
  codAutor INT,
  Titulo VARCHAR(255),
  Editora VARCHAR(255),
  Edicao INT,
  NumeroPagina INT,
  CONSTRAINT livros_PK PRIMARY KEY (codLivro),
  CONSTRAINT livros_FK FOREIGN KEY (codAutor) REFERENCES Autores (codAutor)
);