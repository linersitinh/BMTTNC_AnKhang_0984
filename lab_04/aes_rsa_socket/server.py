from pathlib import Path
import socket
import threading

from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding

BASE_DIR = Path(__file__).resolve().parent

HOST = "127.0.0.1"
PORT = 5000

PRIVATE_KEY_PATH = BASE_DIR / "server_private_key.pem"

with open(PRIVATE_KEY_PATH, "rb") as f:
    private_key = serialization.load_pem_private_key(
        f.read(),
        password=None
    )

clients = []
clients_lock = threading.Lock()


def recv_until_newline(conn):
    data = b""
    while not data.endswith(b"\n"):
        chunk = conn.recv(1)
        if not chunk:
            break
        data += chunk
    return data.strip()


def recv_exact(conn, size):
    data = b""
    while len(data) < size:
        chunk = conn.recv(size - len(data))
        if not chunk:
            raise ConnectionError("Mất kết nối")
        data += chunk
    return data


def broadcast(sender_conn, sender_name, plaintext):
    with clients_lock:
        dead_clients = []

        for conn, addr, fernet, name in clients:
            if conn == sender_conn:
                continue

            try:
                encrypted_msg = fernet.encrypt(f"{sender_name}: {plaintext}".encode("utf-8"))
                conn.sendall(len(encrypted_msg).to_bytes(4, "big"))
                conn.sendall(encrypted_msg)
            except Exception:
                dead_clients.append((conn, addr, fernet, name))

        for item in dead_clients:
            if item in clients:
                clients.remove(item)


def handle_client(conn, addr):
    client_name = f"{addr[0]}:{addr[1]}"
    fernet = None

    try:
        # Nhận AES/Fernet key đã được client mã hóa bằng RSA public key
        enc_key_len = int(recv_until_newline(conn).decode())
        encrypted_fernet_key = recv_exact(conn, enc_key_len)

        # Server dùng private key để giải mã
        fernet_key = private_key.decrypt(
            encrypted_fernet_key,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )

        fernet = Fernet(fernet_key)

        # Nhận tên client
        name_len = int(recv_until_newline(conn).decode())
        enc_name = recv_exact(conn, name_len)
        client_name = fernet.decrypt(enc_name).decode("utf-8")

        with clients_lock:
            clients.append((conn, addr, fernet, client_name))

        print(f"[SERVER] {client_name} đã kết nối")

        while True:
            raw_len = conn.recv(4)
            if not raw_len:
                break

            msg_len = int.from_bytes(raw_len, "big")
            encrypted_msg = recv_exact(conn, msg_len)
            plaintext = fernet.decrypt(encrypted_msg).decode("utf-8")

            print(f"[SERVER] {client_name}: {plaintext}")
            broadcast(conn, client_name, plaintext)

    except Exception as e:
        print(f"[SERVER] Lỗi với {client_name}: {e}")

    finally:
        with clients_lock:
            clients[:] = [c for c in clients if c[0] != conn]

        conn.close()
        print(f"[SERVER] {client_name} đã ngắt kết nối")


def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(5)

    print(f"[SERVER] Đang lắng nghe tại {HOST}:{PORT}")

    while True:
        conn, addr = server.accept()
        t = threading.Thread(target=handle_client, args=(conn, addr), daemon=True)
        t.start()


if __name__ == "__main__":
    main()