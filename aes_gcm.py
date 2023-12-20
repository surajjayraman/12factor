# more modern mode of operations for stream ciphers
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

def AES_GCM_encrypt(plaintext, AES_key, nonce):

    AES_GCM_cipher =  AES.new(AES_key, AES.MODE_GCM, nonce=nonce)
    ciphertext = AES_GCM_cipher.encrypt(plaintext)
    return ciphertext

def AES_GCM_decrypt(ciphertext, AES_key, nonce):

    AES_GCM_cipher =  AES.new(AES_key, AES.MODE_GCM, nonce=nonce)
    decrypted_plaintext = AES_GCM_cipher.decrypt(ciphertext)
    return decrypted_plaintext




