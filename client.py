import socket
from crypto_utils import encrypt_message, decrypt_message

def start_client():
    host = '127.0.0.1'
    port = 5555
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))

    msg = input("Enter message (e.g. SetA-Two): ")
    encrypted = encrypt_message(msg)
    client.send(encrypted)

    try:
        while True:
            response = client.recv(1024)
            if not response:
                break
            print("[Server]:", decrypt_message(response))
    except:
        pass
    finally:
        client.close()

if __name__ == "__main__":
    start_client()
