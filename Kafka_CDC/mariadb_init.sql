CREATE DATABASE change_data_capture;

USE change_data_capture;

CREATE TABLE estudiantes (
    id                  INT AUTO_INCREMENT PRIMARY KEY,
    nombre              VARCHAR(100) NOT NULL,
    apellido            VARCHAR(100) NOT NULL,
    correo              VARCHAR(150) UNIQUE NOT NULL,
    fecha_nacimiento    DATE,
    carrera             VARCHAR(100),
    semestre            INT
);
