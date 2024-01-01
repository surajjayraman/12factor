from Crypto.Cipher import AES
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.hash import HMAC, SHA256
from Crypto.Random import get_random_bytes

def generate_mac(symmetric_key, nonce, plaintext):

    symmetric_cipher =  AES.new(symmetric_key, AES.MODE_GCM, nonce=nonce)
    mac = symmetric_cipher.encrypt(plaintext)

    return mac





