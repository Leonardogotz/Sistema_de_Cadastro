# Sistema_de_Cadastro


*LINK PARA VIDEO EXPLICANDO A APLICAÇÃO: https://youtu.be/b8a7vqOclts*

Estamos criando um sistema de cadastro de colaboradores de uma empresa,
onde cada usuario tem permissões especificas dentro do sistema de uma empresa,
podendo conflitar ou não umas com as outras, definindo isso em matrizes de SoD
conforme passados pelo professor em aula.

Passo a passo do código:

1-  Programado em Python - Colaborando entre Pycharm e VSCode

2-  Banco de dados SQL: WampServer

3-  Diversas bibliotecas: PyQt5, Pandas, PyMySql, openpyxl, mysql 

4-  Parte gráfica desenvolvida com Qt Designer e integrado em funções dentro do programa principal.

5-  Idealizado com tela de entrada, e acessos para Cadastro, Consulta, Conflitos de cadastro/perfil.
    Cada tela com icones e acesso e ações que foram linkadas com o programa, otimizando suas funções.
    Buscando uma interação limpa e eficiente pro usuario final

6-  Incluido na função de consulta, possibilidades de deletar um cadastro errado, e/ou exportar a 
    planilha inteira para um arquivo externo de extensão XLSX.



Etapas:

Configurar o banco de dados e liberar no codigo o padrão de login e senha.
Foi escrito linhas de comando para automatizar este processo dentro do WAMP.
{#criacao de banco de dados sql no wamp
import mysql.connector
banco = mysql.connector.connect( host="localhost", user="root", passwd="" )
cursor = banco.cursor()
cursor.execute("CREATE DATABASE cadastro")
print("Conexão com o Banco de Dados aberta com sucesso!")
banco.commit()
banco.close()
banco2 = mysql.connector.connect( host="localhost", user="root", passwd="", database="cadastro" )
cursor2 = banco2.cursor()
cursor2.execute(""" create table cadastro (
    id INT NOT NULL AUTO_INCREMENT,
    usuario VARCHAR(20),
    cpf VARCHAR(12),
    codigo_1 VARCHAR(20),
    codigo_2 VARCHAR(20),
    perfil VARCHAR(20),
    PRIMARY KEY (id,cpf)
); """)
print("Tabela criada com sucesso!")
banco2.commit()
banco2.close()
}

Database - cadastro.db 
Tabela - cadastro
Ultilizamos o Wampserver para a criação do banco de dados, o qual pode ser instalado nesse link 
(https://www.wampserver.com/en/download-wampserver-64bits/), após isso, com o Wampserver aberto, 
ele aparecerá no canto inferior direito, vamos clicar nele, ir em MySQL e abrir o console, se 
pedir uma senha é só apertar a tecla ENTER.

Após configurar nossa aplicação em python, nos criamos nosso banco de dados em SQL(cadastro.db e cadastro table), para que as informações dos usuarios fiquem salvas para futura analise dos perfis.

Criamos a interface do nosso cadastro de usuarios usando o Qt Designer,
podendo ser instalado a biblioteca pelo cmd/terminal do computador ultilizando os comandos, *pip install PyQt5* e *pip install pyqt5-tools*,
após feito o designer salvamos o arquivo UI dentro da pasta do projeto, sendo um arquivo para cada janela visual(*.UI)
Então foi linkado os acessos do programa, e dentro do codigo o link aos botões e ações.

Após salvar o arquivo dentro da pasta, começamos a configurar o nosso arquivo python para receber a interface criada
e tambem passar as instruções para o sistema reconhecer os botões inseridos.

Após confirmar que o banco de dados e a tabela foi criada. 
E vamos inserir os dados na tabela conforme o código que esta na função principal.

Ações - Executar o aplicativo, rodando o Cadastro.py
        Cadastrar os usuarios com seu codigo e peril compativel
        Entrar com numero e CPF no banco de dados.
        Ao escolher dois setore/codigos diferentes, 2 registros são incluidos levando em consideração a não conflitancia.
        Cadatro efetuado com sucesso - Pop up aparece e permite fechar a janela.
        Cadastro errado precisa ser refeito e ou excluido.
        Exportação da tabela cadastrada para gerar uma planilha de excel.




