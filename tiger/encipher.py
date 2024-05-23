"""
加密器
使用Python的cryptography库进行AES文件加密
pip install cryptography
"""
from cryptography.fernet import Fernet

# 生成一个密钥
# key = Fernet.generate_key()
key = b"2tsLuCBqM3Nw3stNCcRjBCh5AvTyGN7AF7IOwKgM7bs="

# 使用密钥创建一个Fernet对象
cipher_suite = Fernet(key)


# 加密文件
def encrypt_file(file_name):
    with open(file_name, "rb") as file:
        file_data = file.read()

    encrypted_data = cipher_suite.encrypt(file_data)

    _file_name = file_name + ".enc"
    with open(_file_name, "wb") as file:
        file.write(encrypted_data)

    return _file_name


# 解密文件
def decrypt_file(file_name):
    with open(file_name, "rb") as file:
        encrypted_data = file.read()

    decrypted_data = cipher_suite.decrypt(encrypted_data)

    _file_name = file_name.replace(".enc", "")
    with open(_file_name, "wb") as file:
        file.write(decrypted_data)

    return _file_name


if __name__ == "__main__":
    encrypt_file("example.txt")
    decrypt_file("example.txt.enc")
