import os
from ecdsa import SigningKey, VerifyingKey, NIST256p, BadSignatureError


class ECCCipher:
    def __init__(self):
        self.base_dir = os.path.dirname(os.path.abspath(__file__))
        self.keys_dir = os.path.join(self.base_dir, "keys")
        os.makedirs(self.keys_dir, exist_ok=True)

        self.private_key_path = os.path.join(self.keys_dir, "privateKey.pem")
        self.public_key_path = os.path.join(self.keys_dir, "publicKey.pem")

    def generate_keys(self):
        private_key = SigningKey.generate(curve=NIST256p)
        public_key = private_key.get_verifying_key()

        with open(self.private_key_path, "wb") as f:
            f.write(private_key.to_pem())

        with open(self.public_key_path, "wb") as f:
            f.write(public_key.to_pem())

        return True

    def load_keys(self):
        if not os.path.exists(self.private_key_path) or not os.path.exists(self.public_key_path):
            raise FileNotFoundError("Chưa có key ECC. Hãy generate key trước.")

        with open(self.private_key_path, "rb") as f:
            private_key = SigningKey.from_pem(f.read())

        with open(self.public_key_path, "rb") as f:
            public_key = VerifyingKey.from_pem(f.read())

        return private_key, public_key

    def sign(self, message, private_key):
        if isinstance(message, str):
            message = message.encode("utf-8")
        return private_key.sign(message)

    def verify(self, message, signature, public_key):
        if isinstance(message, str):
            message = message.encode("utf-8")
        try:
            return public_key.verify(signature, message)
        except BadSignatureError:
            return False