CREATE TABLE scrape_requests (
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT COMMENT 'Primary Key',
    url VARCHAR(2083) NOT NULL COMMENT 'URL solicitada',  -- Longitud máxima recomendada para URLs
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP COMMENT 'Fecha y hora de la solicitud',
    success BOOLEAN NOT NULL COMMENT 'Indica si el scraping fue exitoso',
    data_size INT NOT NULL COMMENT 'Tamaño de los datos extraídos en bytes',
    scraped_data TEXT COMMENT 'Datos extraídos en formato texto',  -- Puede cambiarse a JSON si es necesario
    scrape_type VARCHAR(255) NOT NULL COMMENT 'Tipo de scraping (links, imágenes, etc.)',
    save_to_file BOOLEAN DEFAULT FALSE COMMENT 'Si se guarda en archivo'
);


CREATE TABLE users (
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT COMMENT 'Primary Key',
    username VARCHAR(191) NOT NULL UNIQUE,  -- Reducido a 191 caracteres
    email VARCHAR(191) NOT NULL UNIQUE,     -- Reducido a 191 caracteres
    token TEXT NOT NULL,                    -- No indexado
    active BOOLEAN DEFAULT TRUE,            -- Indica si el usuario está activo
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


INSERT INTO users (username, email, token, active)
VALUES
('usuario_example', 
 'usuario@example.com', 
 'd517b42a1d9459776347b24b89a84a17e4b849a5783174b37adb09d6031d', 
 TRUE);
