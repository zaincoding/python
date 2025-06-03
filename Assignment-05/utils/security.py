import hashlib, base64
from cryptography.fernet import Fernet, InvalidToken

def create_encryption_key(user_password: str) -> str:
    hashed = hashlib.sha256(user_password.encode()).digest()
    return base64.urlsafe_b64encode(hashed).decode()

def encrypt_message(plain_text: str, user_password: str) -> str:
    key = create_encryption_key(user_password)
    fernet = Fernet(key)
    return fernet.encrypt(plain_text.encode()).decode()

def decrypt_message(encrypted_text: str, user_password: str) -> str:
    try:
        key = create_encryption_key(user_password)
        fernet = Fernet(key)
        return fernet.decrypt(encrypted_text.encode()).decode()
    except InvalidToken:
        return "Invalid key: or corrupted data."

MAX_ATTEMPTS = 3
