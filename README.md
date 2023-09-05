# Sistema_de_Cadastro

Estamos criando um sistema de cadastro de colaboradores de uma empresa,
onde cada usuario tem permissões especificas dentro do sistema de uma empresa,
podendo conflitar ou não umas com as outras, definindo isso em matrizes de SoD
conforme passados pelo professor em aula.

Passo a passo do código:

1- Criamos a interface do nosso cadastro de usuarios usando o Qt Designer,
podendo ser instalado pelo cmd do computador ultilizando os comandos, *pip install PyQt5* e *pip install pyqt5-tools*,
após feito o designer salvamos o arquivo UI dentro da pasta do projeto.

2- Após salvar o arquivo dentro da pasta começamos a configurar o nosso arquivo python para receber a interface criada
e tambem passar as instruções para o sistema reconhecer os botões inseridos.

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

cursor.execute("CREATE TABLE cadastro (usuario VARCHAR(255), cpf INT(11), codigo VARCHAR(255), perfil VARCHAR(255))")

7 - Após isso podemos verificar se a tabela foi criada digitando "show tables", após isso o comando abaixo pode ser excluido da função:

cursor.execute("CREATE TABLE cadastro (usuario VARCHAR(255), cpf INT(11), codigo VARCHAR(255), perfil VARCHAR(255))")

e vamos inserir os dados na tabela conforme o código que esta na função principal.



