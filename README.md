# Sistema_de_Cadastro

Estamos criando um sistema de cadastro de colaboradores de uma empresa,
onde cada usuario tem permissões especificas dentro do sistema de uma empresa,
podendo conflitar ou não umas com as outras, definindo isso em matrizes de SoD
conforme passados pelo professor em aula.

Instale essas bibliotecas antes de rodar a aplicação:

#from PyQt5 import  uic,QtWidgets
#import mysql.connector
#from pymysql import *
#import pandas.io.sql as sql
#import pandas
#import openpyxl

Passo a passo do código:

1- Criamos a interface do nosso cadastro de usuarios usando o Qt Designer,
podendo ser instalado pelo cmd do computador ultilizando os comandos, *pip install PyQt5* e *pip install pyqt5-tools*,
após feito o design salvamos o arquivo UI dentro da pasta do projeto.

2- Após salvar o arquivo dentro da pasta começamos a configurar o nosso arquivo python para receber a interface criada
e tambem passar as instruções para o sistema reconhecer os botões inseridos.

    -Nossa aplicação contém uma página inicial na qual você poderá através dela acessar as abas de cadastro de usuários, a aba onde fica listado os usuários cadastrados, a aba aonde fica a explicação dos conflitos, e um botão no qual encerra a aplicação;

    -Na aba de cadastro, o usuário poderá cadastrar o colaborador respeitando as matrizes de SoD, na qual está explicada em um tabela de instrução logo ao lado direito;

    -Na aba de listas, o usuário poderá ver as pessoas cadastradas e suas respectivas permissões, também podendo exportar essa lista em um arquivo xlsx.

    -Na aba de conflitos, está especificado cais são os conflitos entre os perfis e os códigos dos usuários.

3- Após configurar nossa aplicação em python, nos criamos nosso banco de dados em SQL, para que as informações dos usuarios fique salvo para a futura analise dos perfis futuramente.

4- Ultilizamos o Wampserver para a criação do banco de dados, o qual pode ser instalado nesse link (https://www.wampserver.com/en/download-wampserver-64bits/), após isso, com o Wampserver aberto, ele aparecerá no canto inferior direito, vamos clicar nele, ir em MySQL e abrir o console, se pedir uma senha é só apertar a tecla ENTER.

5- com o console aberto vamos na função do nosso programa principal e usaremos a seguinte função para criar o banco de dados: 

import mysql.connector

banco = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    )

cursor = banco.cursor()

cursor.execute("CREATE DATABASE cadastro")

6 - Digite "show databases" no console do Wampserver para verificar se foi realmente criado, após verificar que o banco tenha sido criado,  colocaremos o nome do banco na database da nossa função e iremos criar a tabela de cadastro.

import mysql.connector

banco = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="cadastro"
    )

cursor = banco.cursor()

cursor.execute("CREATE TABLE cadastro (id INT NOT NULL AUTO_INCREMENT, usuario VARCHAR(255), cpf INT(11), codigo VARCHAR(255), perfil VARCHAR(255))")

7 - Após isso podemos verificar se a tabela foi criada digitando "show tables", após isso o comando abaixo pode ser excluido da função:

cursor.execute("CREATE TABLE cadastro (id INT NOT NULL AUTO_INCREMENT, usuario VARCHAR(255), cpf INT(11), codigo VARCHAR(255), perfil VARCHAR(255))")

e vamos inserir os dados na tabela rodando nossa aplicação e criando o primeiro cadastro.



