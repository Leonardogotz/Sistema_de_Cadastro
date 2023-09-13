from PyQt5 import  uic,QtWidgets
import mysql.connector

banco = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="cadastro"
    )



def funcao_principal():
    linha1 = interface.lineEdit.text()
    linha2 = interface.lineEdit_2.text()

    codigo_1 = ""
    codigo_2 = ""
    codigo_3 = ""
    codigo_4 = ""
    
    if interface.checkBox.isChecked() :
        print("Setor compras selecionado")
        codigo_1 ="Suprimentos"
    else:
        codigo_1 == None


    if interface.checkBox_2.isChecked() :
        print("Setor administrativo selecionado")
        codigo_2 ="Contabilidade"
    else:
        codigo_2 == None
        
    if interface.checkBox_3.isChecked() :
        print("Setor estoque selecionado")
        codigo_3 ="Comercial"
    else:
        codigo_3 == None

    if interface.checkBox_4.isChecked() :
        print("Setor vendas selecionado")
        codigo_4 ="Logistica"
    else:
        codigo_4 == None
   
    codigos = (codigo_1,codigo_2,codigo_3,codigo_4)

    
    perfil = ""
    
    if interface.radioButton.isChecked() :
        print("Perfil Suprimentos selecionado")
        perfil ="Compras"
    elif interface.radioButton_2.isChecked() :
        print("Perfil Contabilidade selecionado")
        perfil ="Administrativo"
    elif interface.radioButton_3.isChecked() :
        print("Perfil Comercial selecionado")
        perfil ="Estoque"    
    elif interface.radioButton_4.isChecked() :
        print("Perfil Logistica selecionado")
        perfil ="Vendas"
    
    
    print(perfil)
    print(codigos)
    print("Nome do Usuário:",linha1)
    print("CPF:",linha2)

    
    if interface.radioButton.isChecked() and (interface.checkBox_2.isChecked() or interface.checkBox_4.isChecked()):
        erro.show()
    elif interface.radioButton_2.isChecked() and (interface.checkBox.isChecked() or interface.checkBox_3.isChecked()):
        erro.show()
    elif interface.radioButton_3.isChecked() and (interface.checkBox_2.isChecked() or interface.checkBox_3.isChecked()):
        erro.show()
    elif interface.radioButton_4.isChecked() and (interface.checkBox_2.isChecked() or interface.checkBox_4.isChecked()):
        erro.show()          
    else: 
        cursor = banco.cursor()
        comando_SQL = "INSERT INTO cadastro (usuario, cpf, codigos, perfil) VALUES (%s,%s,%s,%s)"
        dados = (str(linha1),str(linha2), str(codigos), perfil)
        cursor.execute(comando_SQL,dados)
        banco.commit()
        interface.lineEdit.setText("")
        interface.lineEdit_2.setText("")
    
        sucesso.show()

def fechar_pagina():
    sucesso.close()

def fechar_erro():
    erro.close()


def lista_usuarios():
    lista.show()

    cursor = banco.cursor()
    comando_SQL = "SELECT * FROM cadastro"
    cursor.execute(comando_SQL)
    dados_lidos = cursor.fetchall()

    lista.tableWidget.setRowCount(len(dados_lidos))
    lista.tableWidget.setColumnCount(5)

    for i in range(0, len(dados_lidos)):
        for j in range(0, 5):
            lista.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))


def deletar_dados():
   linha = lista.tableWidget.currentRow()
   lista.tableWidget.removeRow(linha)

   cursor = banco.cursor()
   cursor.execute("SELECT id FROM cadastro")
   dados_lidos = cursor.fetchall()
   valor_id = dados_lidos[linha][0]
   cursor.execute("DELETE FROM cadastro WHERE id="+ str(valor_id))





app=QtWidgets.QApplication([])
interface=uic.loadUi("interface.ui")
lista=uic.loadUi("lista.ui")
sucesso=uic.loadUi("sucesso.ui")
erro=uic.loadUi("erro.ui")
teladeentrada=uic.loadUi("teladeentrada.ui")
perfil_conflitos=uic.loadUi("conflitos.ui")
interface.pushButton.clicked.connect(funcao_principal)
interface.pushButton_2.clicked.connect(lista_usuarios)
interface.pushButton_3.clicked.connect(interface.close)
lista.pushButton.clicked.connect(deletar_dados)
lista.pushButton_2.clicked.connect(lista.close)
sucesso.pushButton.clicked.connect(fechar_pagina)
erro.pushButton.clicked.connect(fechar_erro)
teladeentrada.consulta.clicked.connect(lista_usuarios)
teladeentrada.cadastro.clicked.connect(interface.show)
teladeentrada.sair2.clicked.connect(perfil_conflitos.show)
teladeentrada.sair.clicked.connect(teladeentrada.close)
perfil_conflitos.sair.clicked.connect(perfil_conflitos.close)


teladeentrada.show()
app.exec()