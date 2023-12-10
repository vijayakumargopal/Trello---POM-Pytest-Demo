from cryptography.fernet import Fernet
from utilities.read_input import fetch_data_from_input_data
import sys

my_fernet_key = fetch_data_from_input_data("fernet_key")

def encrypt_me(password):
    fernet = Fernet(my_fernet_key)
    return fernet.encrypt(password.encode())


def decrypt_me(password):
    fernet = Fernet(my_fernet_key)
    return fernet.decrypt(password).decode()


if __name__=="__main__":
    if sys.argv[1] == "encrypt":
        encrypted_data = encrypt_me(sys.argv[2])
        print(encrypted_data)
    if sys.argv[1] == "decrypt":
        decrypted_data = decrypt_me(sys.argv[2])
        print(decrypted_data)

