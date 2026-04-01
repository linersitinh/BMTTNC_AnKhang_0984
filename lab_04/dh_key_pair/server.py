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
    parameters = dh.generate_parameters(generator=2, key_size=2048)
    private_key = parameters.generate_private_key()
    public_key = private_key.public_key()

    public_pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )

    with open("server_public_key.pem", "wb") as f:
        f.write(public_pem)

    print("[SERVER] Da tao server_public_key.pem")

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(1)
    print(f"[SERVER] Dang cho client tai {HOST}:{PORT}")

    conn, addr = server.accept()
    print(f"[SERVER] Client ket noi: {addr}")

    params_pem = parameters.parameter_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.ParameterFormat.PKCS3
    )
    conn.sendall(f"{len(params_pem)}\n".encode())
    conn.sendall(params_pem)

    conn.sendall(f"{len(public_pem)}\n".encode())
    conn.sendall(public_pem)

    client_pub_len = int(recv_until_newline(conn).decode())
    client_pub_pem = recv_exact(conn, client_pub_len)

    client_public_key = serialization.load_pem_public_key(client_pub_pem)

    shared_key = private_key.exchange(client_public_key)

    derived_key = HKDF(
        algorithm=hashes.SHA256(),
        length=32,
        salt=None,
        info=b"lab04-dh-key"
    ).derive(shared_key)

    secret_message = "Thong diep bi mat duoc chia se thanh cong!"
    conn.sendall(f"{secret_message}\n".encode())

    print("[SERVER] Shared key (hex):", derived_key.hex())
    print("[SERVER] Da gui thong diep bi mat")

    conn.close()
    server.close()

if __name__ == "__main__":
    main()