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
    linha3 = interface.lineEdit_3.text()

    perfil = ""
    
    if interface.radioButton.isChecked() :
        print("Perfil Suprimentos selecionado")
        perfil ="Suprimentos"
    elif interface.radioButton_2.isChecked() :
        print("Perfil Contabilidade selecionado")
        perfil ="Contabilidade"
    elif interface.radioButton_3.isChecked() :
        print("Perfil Comercial selecionado")
        perfil ="Comercial"    
    else :
        print("Perfil Logistica selecionado")
        perfil ="Logistica"

    print("Nome do Usuário:",linha1)
    print("CPF:",linha2)
    print("Código do Sistema:",linha3)

    cursor = banco.cursor()
    comando_SQL = "INSERT INTO cadastro (usuario, cpf, codigo, perfil) VALUES (%s,%s,%s,%s)"
    dados = (str(linha1),str(linha2),str(linha3),perfil)
    cursor.execute(comando_SQL,dados)
    banco.commit()
    interface.lineEdit.setText("")
    interface.lineEdit_2.setText("")
    interface.lineEdit_3.setText("")
    
    sucesso.show()

def fechar_pagina():
    sucesso.close()

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
interface.pushButton.clicked.connect(funcao_principal)
interface.pushButton_2.clicked.connect(lista_usuarios)
lista.pushButton.clicked.connect(deletar_dados)
sucesso.pushButton.clicked.connect(fechar_pagina)


interface.show()
app.exec()