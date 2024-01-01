from Crypto.Cipher import AES
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.hash import HMAC, SHA256
from Crypto.Random import get_random_bytes

def generate_mac(symmetric_key, nonce, plaintext):

    symmetric_cipher =  AES.new(symmetric_key, AES.MODE_GCM, nonce=nonce)
    mac = symmetric_cipher.encrypt(plaintext)

    return mac

def generate_hmac(symmetric_key, nonce, plaintext):

    hmac_object = HMAC.new(symmetric_key, plaintext, digestmod=SHA256)
    hmac_digest = hmac_object.digest()
    symmetric_cipher = AES.new(symmetric_key, AES.MODE_CTR, nonce=nonce)
    ciphertext = symmetric_cipher.encrypt(plaintext)
    ciphertext_with_digest = ciphertext + hmac_digest

    return ciphertext_with_digest

def generate_signature(private_key, plaintext):

    RSA_private_key = RSA.import_key(private_key)
    sha256_hash = SHA256.new(plaintext)
    digital_signature = pkcs1_15.new(RSA_private_key).sign(sha256_hash)

    return digital_signature

def verify_signature(public_key, plaintext, digital_signature):

    RSA_public_key = RSA.import_key(public_key)
    verification_sha256_hash = SHA256.new(plaintext)






