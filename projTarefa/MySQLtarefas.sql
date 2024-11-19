CREATE DATABASE db_tarefas;

USE db_tarefas;

CREATE TABLE tbl_usuario (
	usu_id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    usu_nme VARCHAR(30) NOT NULL,
    usu_email VARCHAR(25) NOT NULL
);

CREATE TABLE tbl_tarefa(
	tar_id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    tar_descr VARCHAR(50) NOT NULL,
    tar_setor VARCHAR(30) NOT NULL,
    tar_status VARCHAR(25) NOT NULL,
    tar_prioridade VARCHAR(15) NOT NULL,
    tar_data DATE NOT NULL
);