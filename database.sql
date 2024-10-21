create database db_trabalho;
use db_trabalho;

create table tbl_colaborador(
	id int auto_increment primary key,
	nome varchar(500),
    email varchar(500),
    cpf char(11) unique,
    telefone varchar(11) unique
    
);

create table tbl_vagas(
	id int auto_increment primary key,
    cargo_vaga varchar(500),
    descricao varchar(500),
    requisitos text
	
);

create table tbl_vaga_colaborador(
	id int auto_increment primary key,
    id_vaga int,
	id_colaborador int,
    
    foreign key (id_vaga) references tbl_vagas(id),
    foreign key (id_colaborador) references tbl_colaborador(id)
);