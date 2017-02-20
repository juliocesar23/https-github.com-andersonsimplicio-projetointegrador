from PyQt4 import QtGui
# from mainwindow import Ui_MainWindow

class Login(QtGui.QDialog):
    def __init__(self, parent=None):
        super(Login, self).__init__(parent)
        self.textName = QtGui.QLineEdit(self)
        self.textPass = QtGui.QLineEdit(self)
        self.buttonLogin = QtGui.QPushButton('Login', self)
        self.buttonLogin.clicked.connect(self.handleLogin)
        layout = QtGui.QVBoxLayout(self)
        layout.addWidget(self.textName)
        layout.addWidget(self.textPass)
        layout.addWidget(self.buttonLogin)

    def handleLogin(self):
        if (self.textName.text() == 'foo' and
            self.textPass.text() == 'bar'):
            self.accept()
        else:
            QtGui.QMessageBox.warning(
                self, 'Error', 'Bad user or password')

class Window(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        # self.ui = Ui_MainWindow()
        # self.ui.setupUi(self)

if __name__ == '__main__':

    import sys
    app = QtGui.QApplication(sys.argv)
    login = Login()

    if login.exec_() == QtGui.QDialog.Accepted:
        window = Window()
        window.show()
        sys.exit(app.exec_())

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



