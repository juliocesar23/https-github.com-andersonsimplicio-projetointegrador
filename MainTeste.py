from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QDialog

from views import OpEscolha

if __name__ == '__main__':
    import sys
    App = QApplication(sys.argv)


    dialog = QDialog()
    col = OpEscolha.Ui_OpCadastro()
    col.setupUi(dialog,"Cadastro")
    #ca = cadastrodialog.Ui_Dialog()
    #ca.setupUi(dialog)
    dialog.show()
    sys.exit(dialog.exec_())

'''
def window():
    app = QApplication(sys.argv)
    w = QWidget()
    b = QPushButton(w)
    b.setText("Hello World!")
    b.move(50, 50)
    b.clicked.connect(showdialog)
    w.setWindowTitle("PyQt Dialog demo")
    w.show()
    sys.exit(app.exec_())


def showdialog():
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Warning)
    msg.setText("Atenção")
    msg.setInformativeText("Você deve escolher:\n Pessoa Física \n Pessoa Juridica")
    msg.setWindowTitle("Erro Para Salvar")
    msg.setDetailedText("É obrigatório a selecção de pessoa física ou Juridica para o cadastro")
    msg.show()
    msg.exec_()


    Alerta = QDialog()
    btnOk = QPushButton("ok", Alerta)
    btnOk.move(55,80)
    Alerta.setWindowTitle("Alerta")
    Alerta.setFixedSize(190,120)
    labelAlerta = QLabel(Alerta)
    labelAlerta.setText("")
    labelAlerta.move(10,20)
    Alerta.setWindowModality(QtCore.Qt.ApplicationModal)
    Alerta.exec_()
    '''



