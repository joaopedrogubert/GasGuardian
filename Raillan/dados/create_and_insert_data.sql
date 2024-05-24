

-- Criar a tabela Tanques
CREATE TABLE IF NOT EXISTS Tanques (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    capacidadeMaxima REAL NOT NULL,
    porcentagemAlerta REAL NOT NULL,
    tipoCombustivel_nome TEXT NOT NULL,
    volumeAtual REAL NOT NULL,
    FOREIGN KEY (tipoCombustivel_nome) REFERENCES TipoCombustivel (nome)
);

-- Inserir dados na tabela Tanques
INSERT INTO Tanques (capacidadeMaxima, porcentagemAlerta, tipoCombustivel_nome, volumeAtual) VALUES (15000, 20.00, 'Gasolina', 8000);
INSERT INTO Tanques (capacidadeMaxima, porcentagemAlerta, tipoCombustivel_nome, volumeAtual) VALUES (10000, 20.00, 'Diesel', 5000);
INSERT INTO Tanques (capacidadeMaxima, porcentagemAlerta, tipoCombustivel_nome, volumeAtual) VALUES (12000, 30.00, 'Etanol', 4000);
INSERT INTO Tanques (capacidadeMaxima, porcentagemAlerta, tipoCombustivel_nome, volumeAtual) VALUES (18000, 15.00, 'Gasolina Aditivada', 9000);
INSERT INTO Tanques (capacidadeMaxima, porcentagemAlerta, tipoCombustivel_nome, volumeAtual) VALUES (20000, 10.00, 'Diesel S-10', 15000);

-- Criar a tabela Usuarios
CREATE TABLE IF NOT EXISTS Usuarios (
    cpf TEXT PRIMARY KEY,
    email TEXT NOT NULL,
    nome TEXT NOT NULL,
    telefone TEXT NOT NULL,
    senha TEXT NOT NULL,
    isGestor BOOLEAN NOT NULL
);

-- Inserir dados na tabela Usuarios
INSERT INTO Usuarios (cpf, email, nome, telefone, senha, isGestor) VALUES ('12345678900', 'user1@example.com', 'Usuario 1', '555-1111', 'senha1', 0);
INSERT INTO Usuarios (cpf, email, nome, telefone, senha, isGestor) VALUES ('23456789012', 'user2@example.com', 'Usuario 2', '555-2222', 'senha2', 0);
INSERT INTO Usuarios (cpf, email, nome, telefone, senha, isGestor) VALUES ('34567890123', 'user3@example.com', 'Usuario 3', '555-3333', 'senha3', 0);
INSERT INTO Usuarios (cpf, email, nome, telefone, senha, isGestor) VALUES ('45678901234', 'user4@example.com', 'Usuario 4', '555-4444', 'senha4', 1);
INSERT INTO Usuarios (cpf, email, nome, telefone, senha, isGestor) VALUES ('56789012345', 'user5@example.com', 'Usuario 5', '555-5555', 'senha5', 0);
INSERT INTO Usuarios (cpf, email, nome, telefone, senha, isGestor) VALUES ('67890123456', 'user6@example.com', 'Usuario 6', '555-6666', 'senha6', 0);
INSERT INTO Usuarios (cpf, email, nome, telefone, senha, isGestor) VALUES ('78901234567', 'user7@example.com', 'Usuario 7', '555-7777', 'senha7', 0);
INSERT INTO Usuarios (cpf, email, nome, telefone, senha, isGestor) VALUES ('89012345678', 'user8@example.com', 'Usuario 8', '555-8888', 'senha8', 0);
INSERT INTO Usuarios (cpf, email, nome, telefone, senha, isGestor) VALUES ('90123456789', 'user9@example.com', 'Usuario 9', '555-9999', 'senha9', 1);
INSERT INTO Usuarios (cpf, email, nome, telefone, senha, isGestor) VALUES ('01234567890', 'user10@example.com', 'Usuario 10', '555-1010', 'senha10', 0);

-- Criar a tabela Posto
CREATE TABLE IF NOT EXISTS Posto (
    cnpj TEXT PRIMARY KEY,
    chavePix TEXT NOT NULL,
    nomePosto TEXT NOT NULL
);

-- Inserir dados na tabela Posto
INSERT INTO Posto (cnpj, chavePix, nomePosto) VALUES ('12345678000100', 'chavepix@example.com', 'Posto 1');

-- Criar a tabela Bombas
CREATE TABLE IF NOT EXISTS Bombas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    autoAbastecimento BOOLEAN NOT NULL,
    tipoCombustivel_nome TEXT NOT NULL,
    bombaAtiva BOOLEAN NOT NULL,
    FOREIGN KEY (tipoCombustivel_nome) REFERENCES TipoCombustivel (nome)
);

-- Inserir dados na tabela Bombas
INSERT INTO Bombas (autoAbastecimento, tipoCombustivel_nome, bombaAtiva) VALUES (1, 'Gasolina', 1);
INSERT INTO Bombas (autoAbastecimento, tipoCombustivel_nome, bombaAtiva) VALUES (0, 'Diesel', 1);
INSERT INTO Bombas (autoAbastecimento, tipoCombustivel_nome, bombaAtiva) VALUES (1, 'Etanol', 1);
INSERT INTO Bombas (autoAbastecimento, tipoCombustivel_nome, bombaAtiva) VALUES (0, 'GNV', 1);
INSERT INTO Bombas (autoAbastecimento, tipoCombustivel_nome, bombaAtiva) VALUES (1, 'Gasolina Aditivada', 1);

-- Criar a tabela Abastecimentos
CREATE TABLE IF NOT EXISTS Abastecimentos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    bombaId INTEGER NOT NULL,
    data TEXT NOT NULL,
    litros REAL NOT NULL,
    valorTotal REAL NOT NULL,
    FOREIGN KEY (bombaId) REFERENCES Bombas (id)
);

-- Inserir dados na tabela Abastecimentos
INSERT INTO Abastecimentos (bombaId, data, litros, valorTotal) VALUES (1, '2024-05-20', 50.0, 274.5);
INSERT INTO Abastecimentos (bombaId, data, litros, valorTotal) VALUES (2, '2024-05-21', 40.0, 151.6);
INSERT INTO Abastecimentos (bombaId, data, litros, valorTotal) VALUES (3, '2024-05-22', 60.0, 197.4);
INSERT INTO Abastecimentos (bombaId, data, litros, valorTotal) VALUES (4, '2024-05-23', 30.0, 86.7);
INSERT INTO Abastecimentos (bombaId, data, litros, valorTotal) VALUES (5, '2024-05-24', 45.0, 278.6);
INSERT INTO Abastecimentos (bombaId, data, litros, valorTotal) VALUES (1, '2024-05-25', 55.0, 302.95);
INSERT INTO Abastecimentos (bombaId, data, litros, valorTotal) VALUES (2, '2024-05-26', 35.0, 132.65);
INSERT INTO Abastecimentos (bombaId, data, litros, valorTotal) VALUES (3, '2024-05-27', 70.0, 230.3);
INSERT INTO Abastecimentos (bombaId, data, litros, valorTotal) VALUES (4, '2024-05-28', 25.0, 72.25);
INSERT INTO Abastecimentos (bombaId, data, litros, valorTotal) VALUES (5, '2024-05-29', 40.0, 247.6);
