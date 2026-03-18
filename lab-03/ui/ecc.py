from PyQt5 import QtCore, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(700, 400)
        self.centralwidget = QtWidgets.QWidget(MainWindow)

        self.lbl_title = QtWidgets.QLabel("ECC SIGNATURE", self.centralwidget)
        self.lbl_title.setGeometry(QtCore.QRect(250, 20, 220, 30))
        font = self.lbl_title.font()
        font.setPointSize(14)
        font.setBold(True)
        self.lbl_title.setFont(font)

        self.btn_gen_keys = QtWidgets.QPushButton("Generate Keys", self.centralwidget)
        self.btn_gen_keys.setGeometry(QtCore.QRect(540, 20, 120, 30))

        self.lbl_info = QtWidgets.QLabel("Information:", self.centralwidget)
        self.lbl_info.setGeometry(QtCore.QRect(40, 90, 100, 20))
        self.txt_info = QtWidgets.QTextEdit(self.centralwidget)
        self.txt_info.setGeometry(QtCore.QRect(140, 80, 500, 80))

        self.lbl_sign = QtWidgets.QLabel("Signature:", self.centralwidget)
        self.lbl_sign.setGeometry(QtCore.QRect(40, 190, 100, 20))
        self.txt_sign = QtWidgets.QTextEdit(self.centralwidget)
        self.txt_sign.setGeometry(QtCore.QRect(140, 180, 500, 100))

        self.btn_sign = QtWidgets.QPushButton("Sign", self.centralwidget)
        self.btn_sign.setGeometry(QtCore.QRect(220, 310, 100, 30))

        self.btn_verify = QtWidgets.QPushButton("Verify", self.centralwidget)
        self.btn_verify.setGeometry(QtCore.QRect(380, 310, 100, 30))

        MainWindow.setCentralWidget(self.centralwidget)
        MainWindow.setWindowTitle("ECC Cipher")