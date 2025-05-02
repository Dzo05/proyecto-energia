CREATE TABLE Sistema (
    id_sistema INT PRIMARY KEY,
    nombre VARCHAR(100),
    descripcion TEXT
);

CREATE TABLE Agente (
    id_agente INT PRIMARY KEY,
    nombre VARCHAR(100),
    tipo VARCHAR(50)
);

CREATE TABLE Recurso (
    id_recurso INT PRIMARY KEY,
    nombre VARCHAR(100),
    tipo VARCHAR(50)
);

CREATE TABLE EntidadTiempo (
    id_tiempo INT PRIMARY KEY,
    fecha DATE,
    hora TIME,
    dia INT,
    mes INT,
    año INT
);

CREATE TABLE Metrica (
    id_metrica INT PRIMARY KEY,
    metric_id VARCHAR(50) UNIQUE,
    nombre VARCHAR(100),
    unidad VARCHAR(20),
    descripcion TEXT,
    entidad_relacionada VARCHAR(50)
);

CREATE TABLE HechosDemanda (
    id_hecho SERIAL PRIMARY KEY,
    id_sistema INT REFERENCES Sistema(id_sistema),
    id_agente INT REFERENCES Agente(id_agente),
    id_recurso INT REFERENCES Recurso(id_recurso),
    id_tiempo INT REFERENCES EntidadTiempo(id_tiempo),
    id_metrica INT REFERENCES Metrica(id_metrica),
    valor DECIMAL(15, 2),
    filtro VARCHAR(100)
);