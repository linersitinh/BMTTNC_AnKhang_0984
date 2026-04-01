import os
import rsa


class RSACipher:
    def __init__(self):
        self.base_dir = os.path.dirname(os.path.abspath(__file__))
        self.keys_dir = os.path.join(self.base_dir, "keys")
        os.makedirs(self.keys_dir, exist_ok=True)

        self.public_key_path = os.path.join(self.keys_dir, "publicKey.pem")
        self.private_key_path = os.path.join(self.keys_dir, "privateKey.pem")

    def generate_keys(self):
        public_key, private_key = rsa.newkeys(2048)

        with open(self.public_key_path, "wb") as f:
            f.write(public_key.save_pkcs1("PEM"))

        with open(self.private_key_path, "wb") as f:
            f.write(private_key.save_pkcs1("PEM"))

        return True

    def load_keys(self):
        if not os.path.exists(self.private_key_path) or not os.path.exists(self.public_key_path):
            raise FileNotFoundError("Chưa có key. Hãy generate key trước.")

        with open(self.private_key_path, "rb") as f:
            private_key = rsa.PrivateKey.load_pkcs1(f.read())

        with open(self.public_key_path, "rb") as f:
            public_key = rsa.PublicKey.load_pkcs1(f.read())

        return private_key, public_key

    def encrypt(self, message, key):
        if isinstance(message, str):
            message = message.encode("utf-8")
        return rsa.encrypt(message, key)

    def decrypt(self, ciphertext, key):
        decrypted = rsa.decrypt(ciphertext, key)
        return decrypted.decode("utf-8")

    def sign(self, message, private_key):
        if isinstance(message, str):
            message = message.encode("utf-8")
        return rsa.sign(message, private_key, "SHA-256")

    def verify(self, message, signature, public_key):
        if isinstance(message, str):
            message = message.encode("utf-8")
        try:
            rsa.verify(message, signature, public_key)
            return True
        except rsa.VerificationError:
            return False