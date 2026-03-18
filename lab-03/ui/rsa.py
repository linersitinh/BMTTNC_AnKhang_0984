from PyQt5 import QtCore, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 500)
        self.centralwidget = QtWidgets.QWidget(MainWindow)

        self.lbl_title = QtWidgets.QLabel("RSA CIPHER", self.centralwidget)
        self.lbl_title.setGeometry(QtCore.QRect(360, 20, 200, 30))
        font = self.lbl_title.font()
        font.setPointSize(14)
        font.setBold(True)
        self.lbl_title.setFont(font)

        self.btn_gen_keys = QtWidgets.QPushButton("Generate Keys", self.centralwidget)
        self.btn_gen_keys.setGeometry(QtCore.QRect(720, 20, 120, 30))

        self.lbl_plain = QtWidgets.QLabel("Plain Text:", self.centralwidget)
        self.lbl_plain.setGeometry(QtCore.QRect(40, 90, 100, 20))
        self.txt_plain_text = QtWidgets.QTextEdit(self.centralwidget)
        self.txt_plain_text.setGeometry(QtCore.QRect(140, 80, 300, 80))

        self.lbl_cipher = QtWidgets.QLabel("CipherText:", self.centralwidget)
        self.lbl_cipher.setGeometry(QtCore.QRect(40, 190, 100, 20))
        self.txt_cipher_text = QtWidgets.QTextEdit(self.centralwidget)
        self.txt_cipher_text.setGeometry(QtCore.QRect(140, 180, 300, 80))

        self.btn_encrypt = QtWidgets.QPushButton("Encrypt", self.centralwidget)
        self.btn_encrypt.setGeometry(QtCore.QRect(140, 280, 100, 30))

        self.btn_decrypt = QtWidgets.QPushButton("Decrypt", self.centralwidget)
        self.btn_decrypt.setGeometry(QtCore.QRect(340, 280, 100, 30))

        self.lbl_info = QtWidgets.QLabel("Information:", self.centralwidget)
        self.lbl_info.setGeometry(QtCore.QRect(500, 90, 100, 20))
        self.txt_info = QtWidgets.QTextEdit(self.centralwidget)
        self.txt_info.setGeometry(QtCore.QRect(600, 80, 240, 80))

        self.lbl_sign = QtWidgets.QLabel("Signature:", self.centralwidget)
        self.lbl_sign.setGeometry(QtCore.QRect(500, 190, 100, 20))
        self.txt_sign = QtWidgets.QTextEdit(self.centralwidget)
        self.txt_sign.setGeometry(QtCore.QRect(600, 180, 240, 80))

        self.btn_sign = QtWidgets.QPushButton("Sign", self.centralwidget)
        self.btn_sign.setGeometry(QtCore.QRect(600, 280, 100, 30))

        self.btn_verify = QtWidgets.QPushButton("Verify", self.centralwidget)
        self.btn_verify.setGeometry(QtCore.QRect(740, 280, 100, 30))

        MainWindow.setCentralWidget(self.centralwidget)
        MainWindow.setWindowTitle("RSA Cipher")