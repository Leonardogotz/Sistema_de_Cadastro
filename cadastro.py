from PyQt5 import  uic,QtWidgets

def funcao_principal():
    linha1 = interface.lineEdit.text()
    linha2 = interface.lineEdit_2.text()
    linha3 = interface.lineEdit_3.text()
    
    if interface.radioButton.isChecked() :
        print("Perfil Suprimentos selecionada")
    elif interface.radioButton_2.isChecked() :
        print("Perfil Contabilidade selecionada")
    elif interface.radioButton_3.isChecked() :
        print("Categoria Comercial selecionada")    
    else :
        print("Categoria Alimentos selecionada")

    print("Nome do Usuário:",linha1)
    print("CPF:",linha2)
    print("Código do Sistema:",linha3)
    

app=QtWidgets.QApplication([])
interface=uic.loadUi("interface.ui")
interface.pushButton.clicked.connect(funcao_principal)

interface.show()
app.exec()