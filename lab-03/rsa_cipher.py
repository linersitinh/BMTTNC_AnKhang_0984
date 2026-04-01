import sys
import requests
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui.rsa import Ui_MainWindow


class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btn_gen_keys.clicked.connect(self.call_api_gen_keys)
        self.ui.btn_encrypt.clicked.connect(self.call_api_encrypt)
        self.ui.btn_decrypt.clicked.connect(self.call_api_decrypt)
        self.ui.btn_sign.clicked.connect(self.call_api_sign)
        self.ui.btn_verify.clicked.connect(self.call_api_verify)

    def call_api_gen_keys(self):
        url = "http://127.0.0.1:5000/api/rsa/generate_keys"
        try:
            response = requests.get(url)
            data = response.json()

            if response.status_code == 200:
                QMessageBox.information(self, "Success", data["message"])
            else:
                QMessageBox.warning(self, "Error", data.get("error", "Unknown error"))
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

    def call_api_encrypt(self):
        url = "http://127.0.0.1:5000/api/rsa/encrypt"
        payload = {
            "message": self.ui.txt_plain_text.toPlainText(),
            "key_type": "public"
        }

        try:
            response = requests.post(url, json=payload)
            data = response.json()

            if response.status_code == 200:
                self.ui.txt_cipher_text.setText(data["encrypted_message"])
                QMessageBox.information(self, "Success", "Encrypted successfully")
            else:
                QMessageBox.warning(self, "Error", data.get("error", "Unknown error"))
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

    def call_api_decrypt(self):
        url = "http://127.0.0.1:5000/api/rsa/decrypt"
        payload = {
            "ciphertext": self.ui.txt_cipher_text.toPlainText(),
            "key_type": "private"
        }

        try:
            response = requests.post(url, json=payload)
            data = response.json()

            if response.status_code == 200:
                self.ui.txt_plain_text.setText(data["decrypted_message"])
                QMessageBox.information(self, "Success", "Decrypted successfully")
            else:
                QMessageBox.warning(self, "Error", data.get("error", "Unknown error"))
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

    def call_api_sign(self):
        url = "http://127.0.0.1:5000/api/rsa/sign"
        payload = {
            "message": self.ui.txt_info.toPlainText()
        }

        try:
            response = requests.post(url, json=payload)
            data = response.json()

            if response.status_code == 200:
                self.ui.txt_sign.setText(data["signature"])
                QMessageBox.information(self, "Success", "Signed successfully")
            else:
                QMessageBox.warning(self, "Error", data.get("error", "Unknown error"))
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

    def call_api_verify(self):
        url = "http://127.0.0.1:5000/api/rsa/verify"
        payload = {
            "message": self.ui.txt_info.toPlainText(),
            "signature": self.ui.txt_sign.toPlainText()
        }

        try:
            response = requests.post(url, json=payload)
            data = response.json()

            if response.status_code == 200:
                if data["is_verified"]:
                    QMessageBox.information(self, "Verify", "Verified successfully")
                else:
                    QMessageBox.warning(self, "Verify", "Verified fail")
            else:
                QMessageBox.warning(self, "Error", data.get("error", "Unknown error"))
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())