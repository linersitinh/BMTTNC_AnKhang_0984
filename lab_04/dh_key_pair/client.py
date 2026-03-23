import socket

from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.kdf.hkdf import HKDF

HOST = "127.0.0.1"
PORT = 6000

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
            raise ConnectionError("Mat ket noi")
        data += chunk
    return data

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((HOST, PORT))

    params_len = int(recv_until_newline(sock).decode())
    params_pem = recv_exact(sock, params_len)
    parameters = serialization.load_pem_parameters(params_pem)

    server_pub_len = int(recv_until_newline(sock).decode())
    server_pub_pem = recv_exact(sock, server_pub_len)

    server_public_key = serialization.load_pem_public_key(server_pub_pem)

    client_private_key = parameters.generate_private_key()
    client_public_key = client_private_key.public_key()

    client_pub_pem = client_public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )

    sock.sendall(f"{len(client_pub_pem)}\n".encode())
    sock.sendall(client_pub_pem)

    shared_key = client_private_key.exchange(server_public_key)

    derived_key = HKDF(
        algorithm=hashes.SHA256(),
        length=32,
        salt=None,
        info=b"lab04-dh-key"
    ).derive(shared_key)

    secret_message = recv_until_newline(sock).decode()

    print("[CLIENT] Shared key (hex):", derived_key.hex())
    print("[CLIENT] Thong diep bi mat:", secret_message)

    sock.close()

if __name__ == "__main__":
    main()