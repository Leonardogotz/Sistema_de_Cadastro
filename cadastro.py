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
    

app=QtWidgets.QApplication([])
interface=uic.loadUi("interface.ui")
interface.pushButton.clicked.connect(funcao_principal)

interface.show()
app.exec()