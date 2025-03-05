CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE
);


-- Insertar un usuario
INSERT INTO usuarios (nombre, email) 
VALUES ('Lucas', 'lucas@example.com');

-- Insertar otro usuario
INSERT INTO usuarios (nombre, email) 
VALUES ('Marta', 'marta@example.com');

-- Insertar más usuarios
INSERT INTO usuarios (nombre, email) 
VALUES ('Carlos', 'carlos@example.com');

INSERT INTO usuarios (nombre, email) 
VALUES ('Ana', 'ana@example.com');

-- Insertar un usuario con un nombre largo
INSERT INTO usuarios (nombre, email) 
VALUES ('Julieta María López', 'julieta@example.com');
