import socket
import threading

from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding

HOST = "127.0.0.1"
PORT = 5000

def recv_exact(conn, size):
    data = b""
    while len(data) < size:
        chunk = conn.recv(size - len(data))
        if not chunk:
            raise ConnectionError("Mat ket noi")
        data += chunk
    return data

def receive_messages(sock, fernet):
    try:
        while True:
            raw_len = sock.recv(4)
            if not raw_len:
                break
            msg_len = int.from_bytes(raw_len, "big")
            encrypted_msg = recv_exact(sock, msg_len)
            plaintext = fernet.decrypt(encrypted_msg).decode("utf-8")
            print(f"\n{plaintext}\n> ", end="", flush=True)
    except Exception:
        print("\n[CLIENT] Mat ket noi toi server")

def main():
    name = input("Nhap ten client: ").strip()

    with open("server_public_key.pem", "rb") as f:
        public_key = serialization.load_pem_public_key(f.read())

    fernet_key = Fernet.generate_key()
    fernet = Fernet(fernet_key)

    encrypted_fernet_key = public_key.encrypt(
        fernet_key,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((HOST, PORT))

    sock.sendall(f"{len(encrypted_fernet_key)}\n".encode())
    sock.sendall(encrypted_fernet_key)

    enc_name = fernet.encrypt(name.encode("utf-8"))
    sock.sendall(f"{len(enc_name)}\n".encode())
    sock.sendall(enc_name)

    threading.Thread(target=receive_messages, args=(sock, fernet), daemon=True).start()

    print("[CLIENT] Da ket noi. Nhap tin nhan:")
    while True:
        msg = input("> ").strip()
        if msg.lower() == "exit":
            break
        encrypted_msg = fernet.encrypt(msg.encode("utf-8"))
        sock.sendall(len(encrypted_msg).to_bytes(4, "big"))
        sock.sendall(encrypted_msg)

    sock.close()

if __name__ == "__main__":
    main()