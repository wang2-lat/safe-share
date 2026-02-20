from cryptography.fernet import Fernet
import base64

def encrypt_content(content: str) -> tuple[bytes, str]:
    """Encrypt content and return encrypted data + key"""
    key = Fernet.generate_key()
    fernet = Fernet(key)
    encrypted = fernet.encrypt(content.encode())
    return encrypted, key.decode()

def decrypt_content(encrypted_data: bytes, key: str) -> str:
    """Decrypt content using provided key"""
    fernet = Fernet(key.encode())
    decrypted = fernet.decrypt(encrypted_data)
    return decrypted.decode()
