import socket, threading, time
from datetime import datetime
from crypto_utils import encrypt_message, decrypt_message

collection = {
    "SetA": [{"One": 1, "Two": 2}],
    "SetB": [{"Three": 3, "Four": 4}],
    "SetC": [{"Five": 5, "Six": 6}],
    "SetD": [{"Seven": 7, "Eight": 8}],
    "SetE": [{"Nine": 9, "Ten": 10}]
}

def handle_client(conn, addr):
    print(f"[+] Connected to {addr}")
    try:
        encrypted_data = conn.recv(1024)
        data = decrypt_message(encrypted_data)
        print(f"[Client]: {data}")

        if '-' not in data:
            conn.send(encrypt_message("EMPTY"))
            return

        set_name, key = data.split('-')

        if set_name in collection:
            subset = collection[set_name][0]
            if key in subset:
                times = subset[key]
                for _ in range(times):
                    msg = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    conn.send(encrypt_message(msg))
                    time.sleep(1)
            else:
                conn.send(encrypt_message("EMPTY"))
        else:
            conn.send(encrypt_message("EMPTY"))

    except Exception as e:
        print("[Error]:", e)
    finally:
        conn.close()

def start_server():
    host = '127.0.0.1'
    port = 5555
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen()
    print(f"[SERVER] Listening on {host}:{port}")

    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()

if __name__ == "__main__":
    start_server()
