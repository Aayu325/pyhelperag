import random
import string
import secrets

def generate_password(length=12):
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(chars) for _ in range(length))

def generate_token(n=32):
    return secrets.token_hex(n)
