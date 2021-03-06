# -*- coding: utf-8 -*-
# Form implementation generated from reading ui file 'fornecedordialog.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from controller.validador import *
from controller.validador import AlertaCpfCnpj, confirmar
from views.func import *
from Model import clienteDB as clientebd

class Ui_Dialog(object):
    def setupUi(self,Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1001, 615)
        self.D = Dialog
        self.cmpCodigo = QtWidgets.QLineEdit(Dialog)
        self.cmpCodigo.setGeometry(QtCore.QRect(50, 50, 51, 20))
        self.cmpCodigo.setObjectName("cmpCodigo")
        self.toolButton_2 = QtWidgets.QToolButton(Dialog)
        self.toolButton_2.setGeometry(QtCore.QRect(110, 50, 25, 19))
        self.toolButton_2.setObjectName("toolButton_2")
        self.cmpRazaoSocial = QtWidgets.QLineEdit(Dialog)
        self.cmpRazaoSocial.setGeometry(QtCore.QRect(150, 50, 361, 20))
        self.cmpRazaoSocial.setObjectName("cmpRazaoSocial")
        self.cmpNomeFantasia = QtWidgets.QLineEdit(Dialog)
        self.cmpNomeFantasia.setGeometry(QtCore.QRect(520, 50, 241, 20))
        self.cmpNomeFantasia.setObjectName("cmpNomeFantasia")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(50, 70, 81, 61))
        self.groupBox.setObjectName("groupBox")
        self.radioFisica = QtWidgets.QRadioButton(self.groupBox)
        self.radioFisica.setGeometry(QtCore.QRect(10, 20, 82, 17))
        self.radioFisica.setObjectName("radioFisica")
        self.radioJuridica = QtWidgets.QRadioButton(self.groupBox)
        self.radioJuridica.setGeometry(QtCore.QRect(10, 40, 82, 17))
        self.radioJuridica.setObjectName("radioJuridica")
        self.cmpCnpjCpf = QtWidgets.QLineEdit(Dialog)
        self.cmpCnpjCpf.setGeometry(QtCore.QRect(150, 100, 141, 20))
        self.cmpCnpjCpf.setObjectName("cmpCnpjCpf")

        self.cmpInscricaoEstadual = QtWidgets.QLineEdit(Dialog)
        self.cmpInscricaoEstadual.setGeometry(QtCore.QRect(300, 100, 141, 20))
        self.cmpInscricaoEstadual.setObjectName("cmpInscricaoEstadual")

        self.cmpInscricaoMunicipal = QtWidgets.QLineEdit(Dialog)
        self.cmpInscricaoMunicipal.setGeometry(QtCore.QRect(450, 100, 141, 20))
        self.cmpInscricaoMunicipal.setObjectName("cmpInscricaoMunicipal")

        self.cmpCep = QtWidgets.QLineEdit(Dialog)
        self.cmpCep.setGeometry(QtCore.QRect(50, 170, 101, 20))
        self.cmpCep.setObjectName("cmpCep")
        self.cmpEndereco = QtWidgets.QLineEdit(Dialog)
        self.cmpEndereco.setGeometry(QtCore.QRect(160, 170, 361, 20))
        self.cmpEndereco.setText("")
        self.cmpEndereco.setObjectName("cmpEndereco")
        self.cmpNum = QtWidgets.QLineEdit(Dialog)
        self.cmpNum.setGeometry(QtCore.QRect(530, 170, 81, 20))
        self.cmpNum.setObjectName("cmpNum")
        self.cmpComplemento = QtWidgets.QLineEdit(Dialog)
        self.cmpComplemento.setGeometry(QtCore.QRect(620, 170, 81, 20))
        self.cmpComplemento.setText("")
        self.cmpComplemento.setObjectName("cmpComplemento")
        self.cmpBairro = QtWidgets.QLineEdit(Dialog)
        self.cmpBairro.setGeometry(QtCore.QRect(50, 220, 121, 20))
        self.cmpBairro.setObjectName("cmpBairro")
        self.cmpCidade = QtWidgets.QLineEdit(Dialog)
        self.cmpCidade.setGeometry(QtCore.QRect(180, 220, 211, 20))
        self.cmpCidade.setObjectName("cmpCidade")
        self.cmpCodMunicipio = QtWidgets.QLineEdit(Dialog)
        self.cmpCodMunicipio.setGeometry(QtCore.QRect(400, 220, 81, 20))
        self.cmpCodMunicipio.setObjectName("cmpCodMunicipio")
        self.cmpUf = QtWidgets.QLineEdit(Dialog)
        self.cmpUf.setGeometry(QtCore.QRect(490, 220, 31, 20))
        self.cmpUf.setObjectName("cmpUf")
        self.cmpPais = QtWidgets.QLineEdit(Dialog)
        self.cmpPais.setGeometry(QtCore.QRect(530, 220, 121, 20))
        self.cmpPais.setObjectName("cmpPais")
        self.groupBox_2 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_2.setGeometry(QtCore.QRect(50, 250, 81, 91))
        self.groupBox_2.setObjectName("groupBox_2")
        self.radioSuspenso = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioSuspenso.setGeometry(QtCore.QRect(10, 60, 82, 17))
        self.radioSuspenso.setObjectName("radioSuspenso")
        self.radioInativo = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioInativo.setGeometry(QtCore.QRect(10, 40, 82, 17))
        self.radioInativo.setObjectName("radioInativo")
        self.radioAtivo = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioAtivo.setGeometry(QtCore.QRect(10, 20, 82, 17))
        self.radioAtivo.setObjectName("radioAtivo")
        self.cmpTelefone1 = QtWidgets.QLineEdit(Dialog)
        self.cmpTelefone1.setGeometry(QtCore.QRect(140, 270, 131, 20))
        self.cmpTelefone1.setObjectName("cmpTelefone1")
        self.cmpTelefone2 = QtWidgets.QLineEdit(Dialog)
        self.cmpTelefone2.setGeometry(QtCore.QRect(280, 270, 131, 20))
        self.cmpTelefone2.setObjectName("cmpTelefone2")
        self.cmpEmailXml = QtWidgets.QLineEdit(Dialog)
        self.cmpEmailXml.setGeometry(QtCore.QRect(140, 310, 271, 20))
        self.cmpEmailXml.setText("")
        self.cmpEmailXml.setObjectName("cmpEmailXml")
        self.cmpEmailComercial = QtWidgets.QLineEdit(Dialog)
        self.cmpEmailComercial.setGeometry(QtCore.QRect(420, 310, 271, 20))
        self.cmpEmailComercial.setText("")
        self.cmpEmailComercial.setObjectName("cmpEmailComercial")
        self.label_23 = QtWidgets.QLabel(Dialog)
        self.label_23.setGeometry(QtCore.QRect(420, 290, 111, 16))
        self.label_23.setObjectName("label_23")
        self.label_30 = QtWidgets.QLabel(Dialog)
        self.label_30.setGeometry(QtCore.QRect(50, 200, 71, 16))
        self.label_30.setObjectName("label_30")
        self.label_17 = QtWidgets.QLabel(Dialog)
        self.label_17.setGeometry(QtCore.QRect(280, 250, 71, 16))
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(Dialog)
        self.label_18.setGeometry(QtCore.QRect(140, 290, 111, 16))
        self.label_18.setObjectName("label_18")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(300, 80, 111, 16))
        self.label_5.setObjectName("label_5")
        self.btnLimpar = QtWidgets.QPushButton(Dialog)
        self.btnLimpar.setGeometry(QtCore.QRect(430, 360, 75, 23))
        self.btnLimpar.setStyleSheet("QPushButton::menu-indicator {\n"
"    image: url(download.png);\n"
"    subcontrol-position: right center;\n"
"    subcontrol-origin: padding;\n"
"    left: -2px;\n"
"}")
        self.btnLimpar.setCheckable(False)
        self.btnLimpar.setAutoRepeat(False)
        self.btnLimpar.setAutoExclusive(False)
        self.btnLimpar.setAutoDefault(False)
        self.btnLimpar.setDefault(False)
        self.btnLimpar.setFlat(False)
        self.btnLimpar.setObjectName("btnLimpar")
        self.label_31 = QtWidgets.QLabel(Dialog)
        self.label_31.setGeometry(QtCore.QRect(400, 200, 91, 16))
        self.label_31.setObjectName("label_31")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(450, 80, 121, 16))
        self.label_6.setObjectName("label_6")
        self.label_25 = QtWidgets.QLabel(Dialog)
        self.label_25.setGeometry(QtCore.QRect(160, 150, 71, 16))
        self.label_25.setObjectName("label_25")
        self.btnCancelar = QtWidgets.QPushButton(Dialog)
        self.btnCancelar.setGeometry(QtCore.QRect(340, 360, 75, 23))
        self.btnCancelar.setObjectName("btnCancelar")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(160, 80, 71, 16))
        self.label_4.setObjectName("label_4")
        self.label_32 = QtWidgets.QLabel(Dialog)
        self.label_32.setGeometry(QtCore.QRect(530, 200, 71, 16))
        self.label_32.setObjectName("label_32")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(150, 30, 81, 16))
        self.label_2.setObjectName("label_2")
        self.label_27 = QtWidgets.QLabel(Dialog)
        self.label_27.setGeometry(QtCore.QRect(620, 150, 91, 16))
        self.label_27.setObjectName("label_27")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(50, 30, 41, 16))
        self.label.setObjectName("label")
        self.label_29 = QtWidgets.QLabel(Dialog)
        self.label_29.setGeometry(QtCore.QRect(490, 200, 81, 20))
        self.label_29.setObjectName("label_29")
        self.label_26 = QtWidgets.QLabel(Dialog)
        self.label_26.setGeometry(QtCore.QRect(50, 150, 81, 16))
        self.label_26.setObjectName("label_26")
        self.btnSalvar = QtWidgets.QPushButton(Dialog)
        self.btnSalvar.setGeometry(QtCore.QRect(250, 360, 75, 23))
        self.btnSalvar.setObjectName("btnSalvar")
        self.label_14 = QtWidgets.QLabel(Dialog)
        self.label_14.setGeometry(QtCore.QRect(140, 250, 71, 16))
        self.label_14.setObjectName("label_14")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(530, 150, 81, 16))
        self.label_7.setObjectName("label_7")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(520, 30, 101, 16))
        self.label_3.setObjectName("label_3")
        self.label_28 = QtWidgets.QLabel(Dialog)
        self.label_28.setGeometry(QtCore.QRect(180, 200, 71, 16))
        self.label_28.setObjectName("label_28")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        # Controles dos botoes
        self.valido = False
        self.btnSalvar.clicked.connect(self.validar)
        self.btnSalvar.clicked.connect(self.CadastroSalvar)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Cadastro Cliente"))
        self.label_23.setText(_translate("Dialog", "e-mail Comercial"))
        self.label_30.setText(_translate("Dialog", "Bairro"))
        self.label_17.setText(_translate("Dialog", "Telefone 2"))
        self.label_18.setText(_translate("Dialog", "e-mail XML"))
        self.label_5.setText(_translate("Dialog", "Inscrição Estadual"))
        self.groupBox.setTitle(_translate("Dialog", "Pessoa:"))
        self.radioFisica.setText(_translate("Dialog", "Física"))
        self.radioJuridica.setText(_translate("Dialog", "Jurídica"))
        self.btnLimpar.setText(_translate("Dialog", "Limpar"))
        self.label_31.setText(_translate("Dialog", "Cód. Município"))
        self.label_6.setText(_translate("Dialog", "Inscrição Municipal"))
        self.label_25.setText(_translate("Dialog", "Endereço"))
        self.btnCancelar.setText(_translate("Dialog", "Cancelar"))
        self.label_4.setText(_translate("Dialog", "CNPJ / CPF"))
        self.label_32.setText(_translate("Dialog", "País"))
        self.toolButton_2.setText(_translate("Dialog", "..."))
        self.label_2.setText(_translate("Dialog", "Razão Social"))
        self.label_27.setText(_translate("Dialog", "Complemento"))
        self.label.setText(_translate("Dialog", "Código"))
        self.label_29.setText(_translate("Dialog", "UF"))
        self.label_26.setText(_translate("Dialog", "CEP"))
        self.groupBox_2.setTitle(_translate("Dialog", "Status"))
        self.radioSuspenso.setText(_translate("Dialog", "Suspenso"))
        self.radioInativo.setText(_translate("Dialog", "Inativo"))
        self.radioAtivo.setText(_translate("Dialog", "Ativo"))
        self.btnSalvar.setText(_translate("Dialog", "Salvar"))
        self.label_14.setText(_translate("Dialog", "Telefone 1"))
        self.label_7.setText(_translate("Dialog", "Nº"))
        self.label_3.setText(_translate("Dialog", "Nome Fantasia"))
        self.label_28.setText(_translate("Dialog", "Cidade"))





    def validar(self):
        if self.radioFisica.isChecked():
            if validar_cpf(self.cmpCnpjCpf.text()) != False:
                self.documento = self.cmpCnpjCpf.text()
                self.valido = True
        elif self.radioJuridica.isChecked():
            if validar_cnpj(self.cmpCnpjCpf.text()) != False:
                self.documento = self.cmpCnpjCpf.text()
                self.valido = True
        else:
            AlertaCpfCnpj()
            self.valido = False

    def CadastroSalvar(self):
        dadosLista = []  # Captura uma lista de dados referente ao cliente
        endercoLista = []  # lista de dados referente apenas ao endereco do cliente

        if self.valido == True:
            dadosLista.append(int(self.cmpCodigo.text()))
            dadosLista.append(self.cmpRazaoSocial.text())
            dadosLista.append(self.cmpNomeFantasia.text())

            if self.radioFisica.isChecked():
                dadosLista.append(self.documento)#cpf
                dadosLista.append("vazio")#cnpj
                dadosLista.append(0)#caso seja pessoa física será registrado como zero
            else:
                dadosLista.append("vazio")  # cpf
                dadosLista.append(self.documento)  # cnpj
                dadosLista.append(1)  # caso seja pessoa juridica será registrado como um

            # cadastra o status
            if self.radioAtivo.isChecked():
                dadosLista.append(1)  # Ativo

            elif self.radioInativo.isChecked():
                dadosLista.append(0)  # Inativo

            else:
                dadosLista.append(-1)  # Suspenso

            dadosLista.append(self.cmpInscricaoEstadual.text())
            dadosLista.append(self.cmpInscricaoMunicipal.text())
            dadosLista.append(self.cmpEmailComercial.text())
            dadosLista.append(self.cmpEmailXml.text())
            dadosLista.append(self.cmpTelefone1.text())
            dadosLista.append(self.cmpTelefone2.text())



            print(dadosLista)
            # cadastro de endereco
            endercoLista.append(int(self.cmpCodigo.text()))#Cod_cliente referido endereço 1
            endercoLista.append(int(self.cmpCodMunicipio.text()))#Codigo do municipio 2
            endercoLista.append(int(self.cmpNum.text()))#Numero da casa 3
            endercoLista.append(self.cmpEndereco.text())#4
            endercoLista.append(self.cmpCidade.text())#5
            endercoLista.append(self.cmpBairro.text())#6
            endercoLista.append(self.cmpPais.text())  # 7
            endercoLista.append(self.cmpUf.text())#8
            endercoLista.append(self.cmpComplemento.text())#9
            endercoLista.append(self.cmpCep.text())  # 10
            print(endercoLista)





                


            if confirmar():
                clibd = clientebd.clienteBD()
                clibd.insert(dadosLista,endercoLista)
                self.D.accept()


