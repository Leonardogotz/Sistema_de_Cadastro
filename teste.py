""" create table cadastro (
    id INT NOT NULL AUTO_INCREMENT,
    usuario VARCHAR(20),
    cpf VARCHAR(12),
    codigo VARCHAR(20),
    perfil VARCHAR(20),
    PRIMARY KEY (id,cpf)
); """

#INSERT INTO cadastro (usuario,cpf,codigo,perfil) VALUES ("Leandro Costa",23545867415,"SAP","Suprimentos");