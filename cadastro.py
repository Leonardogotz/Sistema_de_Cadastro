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
    
    if interface.checkBox.isChecked() :
        print("Setor compras selecionado")
        codigo_1 ="Suprimentos"


    elif interface.checkBox_2.isChecked() :
        print("Setor administrativo selecionado")
        codigo_1 ="Contabilidade"
        
    elif interface.checkBox_3.isChecked() :
        print("Setor estoque selecionado")
        codigo_1 ="Comercial"

    elif interface.checkBox_4.isChecked() :
        print("Setor vendas selecionado")
        codigo_1 ="Logistica"

    
    codigo_2= ""

    if (interface.checkBox.isChecked() and interface.checkBox_2.isChecked()):
            codigo_2 = "Contabilidade"
    if (interface.checkBox.isChecked() and interface.checkBox_3.isChecked()):
            codigo_2 = "Comercial"
    if (interface.checkBox.isChecked() and interface.checkBox_4.isChecked()):
            codigo_2 = "Logistica"
    if (interface.checkBox_2.isChecked() and interface.checkBox_3.isChecked()):
            codigo_2 = "Comercial"
    if (interface.checkBox_2.isChecked() and interface.checkBox_4.isChecked()):
            codigo_2 = "Logistica"
    if (interface.checkBox_3.isChecked() and interface.checkBox_4.isChecked()):
            codigo_2 = "Logistica"


    
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
    
    
    if perfil == "":
         erro2.show()
    else:
        print(perfil)
    
        if codigo_1 == "":
            erro2.show()
        else:
            print(codigo_1)
            print(codigo_2)
        
        
            if linha1 == "":
                erro2.show()
            else:
                print("Nome do Usuário:",linha1)

                if linha2 == "":
                    erro2.show()
                else:
                    print("CPF:", linha2)

            
                    if interface.radioButton.isChecked() and (interface.checkBox_2.isChecked() or interface.checkBox_4.isChecked()):
                        erro.show()
                    elif interface.radioButton_2.isChecked() and (interface.checkBox.isChecked() or interface.checkBox_3.isChecked()):
                        erro.show()
                    elif interface.radioButton_3.isChecked() and (interface.checkBox_2.isChecked() or interface.checkBox_3.isChecked()):
                        erro.show()
                    elif interface.radioButton_4.isChecked() and (interface.checkBox.isChecked() or interface.checkBox_4.isChecked()):
                        erro.show()          
                    else: 
                        cursor = banco.cursor()
                        comando_SQL = "INSERT INTO cadastro (usuario, cpf, codigo_1, codigo_2, perfil) VALUES (%s,%s,%s,%s,%s)"
                        dados = (str(linha1),str(linha2), codigo_1, codigo_2, perfil)
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
    lista.tableWidget.setColumnCount(6)

    for i in range(0, len(dados_lidos)):
        for j in range(0, 6):
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
erro2=uic.loadUi("erro_dados.ui")
teladeentrada=uic.loadUi("teladeentrada.ui")
perfil_conflitos=uic.loadUi("conflitos.ui")
interface.pushButton.clicked.connect(funcao_principal)
interface.pushButton_2.clicked.connect(lista_usuarios)
interface.pushButton_3.clicked.connect(interface.close)
lista.pushButton.clicked.connect(deletar_dados)
lista.pushButton_2.clicked.connect(lista.close)
sucesso.pushButton.clicked.connect(fechar_pagina)
erro.pushButton.clicked.connect(fechar_erro)
erro2.pushButton.clicked.connect(erro2.close)
teladeentrada.consulta.clicked.connect(lista_usuarios)
teladeentrada.cadastro.clicked.connect(interface.show)
teladeentrada.sair2.clicked.connect(perfil_conflitos.show)
teladeentrada.sair.clicked.connect(teladeentrada.close)
perfil_conflitos.sair.clicked.connect(perfil_conflitos.close)


teladeentrada.show()
app.exec()