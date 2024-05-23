-- Criar a tabela TipoCombustivel
CREATE TABLE IF NOT EXISTS TipoCombustivel (
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    preco REAL NOT NULL
);

-- Inserir dados na tabela TipoCombustivel
INSERT INTO TipoCombustivel (id, nome, preco) VALUES (1, 'Gasolina', 5.49);
INSERT INTO TipoCombustivel (id, nome, preco) VALUES (2, 'Diesel', 3.79);
INSERT INTO TipoCombustivel (id, nome, preco) VALUES (3, 'Etanol', 3.29);
INSERT INTO TipoCombustivel (id, nome, preco) VALUES (4, 'GNV', 2.89);
INSERT INTO TipoCombustivel (id, nome, preco) VALUES (5, 'Querosene', 4.99);
INSERT INTO TipoCombustivel (id, nome, preco) VALUES (6, 'Biodiesel', 4.59);
INSERT INTO TipoCombustivel (id, nome, preco) VALUES (7, 'Gasolina Aditivada', 6.19);
INSERT INTO TipoCombustivel (id, nome, preco) VALUES (8, 'Diesel S-10', 4.09);
INSERT INTO TipoCombustivel (id, nome, preco) VALUES (9, 'Diesel S-500', 3.89);
INSERT INTO TipoCombustivel (id, nome, preco) VALUES (10, 'Óleo Combustível', 2.99);

-- Criar a tabela Tanques
CREATE TABLE IF NOT EXISTS Tanques (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    capacidadeMaxima REAL NOT NULL,
    porcentagemAlerta REAL NOT NULL,
    tipoCombustivel_id INTEGER NOT NULL,
    volumeAtual REAL NOT NULL,
    FOREIGN KEY (tipoCombustivel_id) REFERENCES TipoCombustivel (id)
);

-- Inserir dados na tabela Tanques
INSERT INTO Tanques (capacidadeMaxima, porcentagemAlerta, tipoCombustivel_id, volumeAtual) VALUES (10000, 20, 1, 5000);
INSERT INTO Tanques (capacidadeMaxima, porcentagemAlerta, tipoCombustivel_id, volumeAtual) VALUES (15000, 25, 2, 8000);
INSERT INTO Tanques (capacidadeMaxima, porcentagemAlerta, tipoCombustivel_id, volumeAtual) VALUES (12000, 30, 3, 4000);
INSERT INTO Tanques (capacidadeMaxima, porcentagemAlerta, tipoCombustivel_id, volumeAtual) VALUES (18000, 15, 4, 9000);
INSERT INTO Tanques (capacidadeMaxima, porcentagemAlerta, tipoCombustivel_id, volumeAtual) VALUES (20000, 10, 5, 15000);
INSERT INTO Tanques (capacidadeMaxima, porcentagemAlerta, tipoCombustivel_id, volumeAtual) VALUES (14000, 22, 6, 7000);
INSERT INTO Tanques (capacidadeMaxima, porcentagemAlerta, tipoCombustivel_id, volumeAtual) VALUES (16000, 18, 7, 6000);
INSERT INTO Tanques (capacidadeMaxima, porcentagemAlerta, tipoCombustivel_id, volumeAtual) VALUES (13000, 20, 8, 3000);
INSERT INTO Tanques (capacidadeMaxima, porcentagemAlerta, tipoCombustivel_id, volumeAtual) VALUES (11000, 25, 9, 8000);
INSERT INTO Tanques (capacidadeMaxima, porcentagemAlerta, tipoCombustivel_id, volumeAtual) VALUES (19000, 30, 10, 10000);
