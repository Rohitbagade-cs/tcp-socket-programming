from cryptography.fernet import Fernet


key = b'dTxrtux_TBuWCOJPudsGgSAJhxr2AL3JLlvFmPzPDiM='  
cipher = Fernet(key)

def encrypt_message(message):
    return cipher.encrypt(message.encode())

def decrypt_message(token):
    return cipher.decrypt(token).decode()
