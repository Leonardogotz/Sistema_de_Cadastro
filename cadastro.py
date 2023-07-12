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

    codigo = ""
    
    if interface.checkBox.isChecked() :
        print("Setor compras selecionado")
        codigo ="Compras"
    elif interface.checkBox_2.isChecked() :
        print("Setor administrativo selecionado")
        codigo ="Administrativo"
    elif interface.checkBox_3.isChecked() :
        print("Setor estoque selecionado")
        codigo ="Estoque"    
    elif interface.checkBox_4.isChecked() :
        print("Setor vendas selecionado")
        codigo ="Vendas"

    
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
    elif interface.radioButton_4.isChecked() :
        print("Perfil Logistica selecionado")
        perfil ="Logistica"

    print("Nome do Usuário:",linha1)
    print("CPF:",linha2)

    
    if interface.checkBox.isChecked() and interface.radioButton_2.isChecked() or interface.radioButton_4.isChecked():
        erro.show()
    elif interface.checkBox_2.isChecked() and interface.radioButton.isChecked() or interface.radioButton_3.isChecked():
        erro.show()
    elif interface.checkBox_3.isChecked() and interface.radioButton_2.isChecked() or interface.radioButton_3.isChecked():
        erro.show()
    elif interface.checkBox_4.isChecked() and interface.radioButton_2.isChecked() or interface.radioButton_4.isChecked():
        erro.show()          
    else: 
        cursor = banco.cursor()
        comando_SQL = "INSERT INTO cadastro (usuario, cpf, codigo, perfil) VALUES (%s,%s,%s,%s)"
        dados = (str(linha1),str(linha2),codigo,perfil)
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
interface.pushButton.clicked.connect(funcao_principal)
interface.pushButton_2.clicked.connect(lista_usuarios)
lista.pushButton.clicked.connect(deletar_dados)
sucesso.pushButton.clicked.connect(fechar_pagina)
erro.pushButton.clicked.connect(fechar_erro)


interface.show()
app.exec()