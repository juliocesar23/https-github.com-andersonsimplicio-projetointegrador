# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cliente.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from controller.validador import *
from controller.validador import AlertaCpfCnpj
from views.func import *

class Ui_Dialog(object):


    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(816, 686)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(130, 20, 81, 16))
        self.label_2.setObjectName("label_2")
        self.cmpInscricaoEstadual = QtWidgets.QLineEdit(Dialog)
        self.cmpInscricaoEstadual.setGeometry(QtCore.QRect(270, 90, 141, 20))
        self.cmpInscricaoEstadual.setObjectName("cmpInscricaoEstadual")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(510, 140, 81, 16))
        self.label_7.setObjectName("label_7")
        self.btnLimpar = QtWidgets.QPushButton(Dialog)
        self.btnLimpar.setGeometry(QtCore.QRect(410, 350, 75, 23))
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
        self.cmpCnpjCpf = QtWidgets.QLineEdit(Dialog)
        self.cmpCnpjCpf.setGeometry(QtCore.QRect(120, 90, 141, 20))
        self.cmpCnpjCpf.setObjectName("cmpCnpjCpf")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(500, 20, 101, 16))
        self.label_3.setObjectName("label_3")
        self.radioFisica = QtWidgets.QRadioButton(Dialog)
        self.radioFisica.setGeometry(QtCore.QRect(30, 90, 82, 17))
        self.radioFisica.setObjectName("radioFisica")
        self.label_26 = QtWidgets.QLabel(Dialog)
        self.label_26.setGeometry(QtCore.QRect(30, 140, 81, 16))
        self.label_26.setObjectName("label_26")
        self.label_28 = QtWidgets.QLabel(Dialog)
        self.label_28.setGeometry(QtCore.QRect(160, 190, 71, 16))
        self.label_28.setObjectName("label_28")
        self.cmpUf = QtWidgets.QLineEdit(Dialog)
        self.cmpUf.setGeometry(QtCore.QRect(470, 210, 31, 20))
        self.cmpUf.setObjectName("cmpUf")
        self.radioSuspenso = QtWidgets.QRadioButton(Dialog)
        self.radioSuspenso.setGeometry(QtCore.QRect(30, 300, 82, 17))
        self.radioSuspenso.setObjectName("radioSuspenso")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(270, 70, 111, 16))
        self.label_5.setObjectName("label_5")
        self.label_31 = QtWidgets.QLabel(Dialog)
        self.label_31.setGeometry(QtCore.QRect(380, 190, 91, 16))
        self.label_31.setObjectName("label_31")
        self.cmpTelefone2 = QtWidgets.QLineEdit(Dialog)
        self.cmpTelefone2.setGeometry(QtCore.QRect(250, 260, 131, 20))
        self.cmpTelefone2.setObjectName("cmpTelefone2")
        self.label_14 = QtWidgets.QLabel(Dialog)
        self.label_14.setGeometry(QtCore.QRect(110, 240, 71, 16))
        self.label_14.setObjectName("label_14")
        self.label_25 = QtWidgets.QLabel(Dialog)
        self.label_25.setGeometry(QtCore.QRect(140, 140, 71, 16))
        self.label_25.setObjectName("label_25")
        self.radioInativo = QtWidgets.QRadioButton(Dialog)
        self.radioInativo.setGeometry(QtCore.QRect(30, 280, 82, 17))
        self.radioInativo.setObjectName("radioInativo")
        self.cmpBairro = QtWidgets.QLineEdit(Dialog)
        self.cmpBairro.setGeometry(QtCore.QRect(30, 210, 121, 20))
        self.cmpBairro.setObjectName("cmpBairro")
        self.cmpCodMunicipio = QtWidgets.QLineEdit(Dialog)
        self.cmpCodMunicipio.setGeometry(QtCore.QRect(380, 210, 81, 20))
        self.cmpCodMunicipio.setObjectName("cmpCodMunicipio")
        self.cmpCidade = QtWidgets.QLineEdit(Dialog)
        self.cmpCidade.setGeometry(QtCore.QRect(160, 210, 211, 20))
        self.cmpCidade.setObjectName("cmpCidade")
        self.toolButton_2 = QtWidgets.QToolButton(Dialog)
        self.toolButton_2.setGeometry(QtCore.QRect(90, 40, 25, 19))
        self.toolButton_2.setObjectName("toolButton_2")
        self.label_23 = QtWidgets.QLabel(Dialog)
        self.label_23.setGeometry(QtCore.QRect(390, 280, 111, 16))
        self.label_23.setObjectName("label_23")
        self.cmpRazaoSocial = QtWidgets.QLineEdit(Dialog)
        self.cmpRazaoSocial.setGeometry(QtCore.QRect(130, 40, 361, 20))
        self.cmpRazaoSocial.setObjectName("cmpRazaoSocial")
        self.label_17 = QtWidgets.QLabel(Dialog)
        self.label_17.setGeometry(QtCore.QRect(250, 240, 71, 16))
        self.label_17.setObjectName("label_17")
        self.btnCancelar = QtWidgets.QPushButton(Dialog)
        self.btnCancelar.setGeometry(QtCore.QRect(320, 350, 75, 23))
        self.btnCancelar.setObjectName("btnCancelar")
        self.label_29 = QtWidgets.QLabel(Dialog)
        self.label_29.setGeometry(QtCore.QRect(470, 190, 81, 20))
        self.label_29.setObjectName("label_29")
        self.cmpEmailComercial = QtWidgets.QLineEdit(Dialog)
        self.cmpEmailComercial.setGeometry(QtCore.QRect(390, 300, 271, 20))
        self.cmpEmailComercial.setText("")
        self.cmpEmailComercial.setObjectName("cmpEmailComercial")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 20, 41, 16))
        self.label.setObjectName("label")
        self.label_30 = QtWidgets.QLabel(Dialog)
        self.label_30.setGeometry(QtCore.QRect(30, 190, 71, 16))
        self.label_30.setObjectName("label_30")
        self.cmpPais = QtWidgets.QLineEdit(Dialog)
        self.cmpPais.setGeometry(QtCore.QRect(510, 210, 121, 20))
        self.cmpPais.setObjectName("cmpPais")
        self.radioAtivo = QtWidgets.QRadioButton(Dialog)
        self.radioAtivo.setGeometry(QtCore.QRect(30, 260, 82, 17))
        self.radioAtivo.setObjectName("radioAtivo")
        self.radioAtivo.setChecked(True)
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(420, 70, 121, 16))
        self.label_6.setObjectName("label_6")
        self.cmpNomeFantasia = QtWidgets.QLineEdit(Dialog)
        self.cmpNomeFantasia.setGeometry(QtCore.QRect(500, 40, 241, 20))
        self.cmpNomeFantasia.setObjectName("cmpNomeFantasia")
        self.cmpCodigo = QtWidgets.QLineEdit(Dialog)
        self.cmpCodigo.setGeometry(QtCore.QRect(30, 40, 51, 20))
        self.cmpCodigo.setObjectName("cmpCodigo")
        self.cmpEndereco = QtWidgets.QLineEdit(Dialog)
        self.cmpEndereco.setGeometry(QtCore.QRect(140, 160, 361, 20))
        self.cmpEndereco.setText("")
        self.cmpEndereco.setObjectName("cmpEndereco")
        self.cmpEmailXml = QtWidgets.QLineEdit(Dialog)
        self.cmpEmailXml.setGeometry(QtCore.QRect(110, 300, 271, 20))
        self.cmpEmailXml.setText("")
        self.cmpEmailXml.setObjectName("cmpEmailXml")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(130, 70, 71, 16))
        self.label_4.setObjectName("label_4")
        self.label_32 = QtWidgets.QLabel(Dialog)
        self.label_32.setGeometry(QtCore.QRect(510, 190, 71, 16))
        self.label_32.setObjectName("label_32")
        self.cmpTelefone1 = QtWidgets.QLineEdit(Dialog)
        self.cmpTelefone1.setGeometry(QtCore.QRect(110, 260, 131, 20))
        self.cmpTelefone1.setObjectName("cmpTelefone1")
        self.label_24 = QtWidgets.QLabel(Dialog)
        self.label_24.setGeometry(QtCore.QRect(30, 70, 91, 16))
        self.label_24.setObjectName("label_24")
        self.cmpCep = QtWidgets.QLineEdit(Dialog)
        self.cmpCep.setGeometry(QtCore.QRect(30, 160, 101, 20))
        self.cmpCep.setObjectName("cmpCep")
        self.label_27 = QtWidgets.QLabel(Dialog)
        self.label_27.setGeometry(QtCore.QRect(600, 140, 91, 16))
        self.label_27.setObjectName("label_27")
        self.label_33 = QtWidgets.QLabel(Dialog)
        self.label_33.setGeometry(QtCore.QRect(30, 240, 81, 16))
        self.label_33.setObjectName("label_33")
        self.cmpInscricaoEstadual_2 = QtWidgets.QLineEdit(Dialog)
        self.cmpInscricaoEstadual_2.setGeometry(QtCore.QRect(420, 90, 141, 20))
        self.cmpInscricaoEstadual_2.setObjectName("cmpInscricaoEstadual_2")
        self.radioJuridica = QtWidgets.QRadioButton(Dialog)
        self.radioJuridica.setGeometry(QtCore.QRect(30, 110, 82, 17))
        self.radioJuridica.setObjectName("radioJuridica")
        self.cmpComplemento = QtWidgets.QLineEdit(Dialog)
        self.cmpComplemento.setGeometry(QtCore.QRect(600, 160, 81, 20))
        self.cmpComplemento.setText("")
        self.cmpComplemento.setObjectName("cmpComplemento")

        self.btnSalvar = QtWidgets.QPushButton(Dialog)

        self.btnSalvar.setGeometry(QtCore.QRect(230, 350, 75, 23))
        self.btnSalvar.setObjectName("btnSalvar")


        self.cmpNum = QtWidgets.QLineEdit(Dialog)
        self.cmpNum.setGeometry(QtCore.QRect(510, 160, 81, 20))
        self.cmpNum.setObjectName("cmpNum")
        self.label_18 = QtWidgets.QLabel(Dialog)
        self.label_18.setGeometry(QtCore.QRect(110, 280, 111, 16))
        self.label_18.setObjectName("label_18")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        #Controles dos botoes
        self.btnSalvar.clicked.connect( self.validar)


    def validar(self):
            if self.radioFisica.isChecked() :
                if validar_cpf(self.cmpCnpjCpf.text()) != False:
                     print("cpf:")
            elif self.radioJuridica.isChecked():
                if validar_cnpj(self.cmpCnpjCpf.text()) != False:
                     print("cnpj:")
            else:
                AlertaCpfCnpj()



    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Cadastro Fornecedor"))
        self.label_2.setText(_translate("Dialog", "Razão Social"))
        self.label_7.setText(_translate("Dialog", "Nº"))
        self.btnLimpar.setText(_translate("Dialog", "Limpar"))
        self.label_3.setText(_translate("Dialog", "Nome Fantasia"))
        self.radioFisica.setText(_translate("Dialog", "Física"))
        self.label_26.setText(_translate("Dialog", "CEP"))
        self.label_28.setText(_translate("Dialog", "Cidade"))
        self.radioSuspenso.setText(_translate("Dialog", "Suspenso"))
        self.label_5.setText(_translate("Dialog", "Inscrição Estadual"))
        self.label_31.setText(_translate("Dialog", "Cód. Município"))
        self.label_14.setText(_translate("Dialog", "Telefone 1"))
        self.label_25.setText(_translate("Dialog", "Endereço"))
        self.radioInativo.setText(_translate("Dialog", "Inativo"))
        self.toolButton_2.setText(_translate("Dialog", "..."))
        self.label_23.setText(_translate("Dialog", "e-mail Comercial"))
        self.label_17.setText(_translate("Dialog", "Telefone 2"))
        self.btnCancelar.setText(_translate("Dialog", "Cancelar"))
        self.label_29.setText(_translate("Dialog", "UF"))
        self.label.setText(_translate("Dialog", "Código"))
        self.label_30.setText(_translate("Dialog", "Bairro"))
        self.radioAtivo.setText(_translate("Dialog", "Ativo"))
        self.label_6.setText(_translate("Dialog", "Inscrição Municipal"))
        self.label_4.setText(_translate("Dialog", "CNPJ / CPF"))
        self.label_32.setText(_translate("Dialog", "País"))
        self.label_24.setText(_translate("Dialog", "Tipo de Pessoa:"))
        self.label_27.setText(_translate("Dialog", "Complemento"))
        self.label_33.setText(_translate("Dialog", "Status"))
        self.radioJuridica.setText(_translate("Dialog", "Jurídica"))
        self.btnSalvar.setText(_translate("Dialog", "Salvar"))
        self.label_18.setText(_translate("Dialog", "e-mail XML"))






