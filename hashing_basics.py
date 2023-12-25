import hashlib

def hash(plaintext):

    md5_hash = hashlib.md5(plaintext).hexdigest()
    sha1_hash = hashlib.sha1(plaintext).hexdigest()
    sha256_hash = hashlib.sha256(plaintext).hexdigest()

    print("MD5 Hash: ", md5_hash)
    print("SHA1 Hash: ", sha1_hash)
    print("SHA256 Hash: ", sha256_hash)


plaintext = input("Enter plain text: ").encode("ASCII")
hash(plaintext)

# check for password match
def sha256_hash_password(example_password, input_password):

    example_sha256_hash = hashlib.sha256(example_password).hexdigest()
    input_sha256_hash = hashlib.sha256(input_password).hexdigest()

    print("Example password: ", example_password.decode("ASCII"))
    print("Example SHA256 hash: ", example_sha256_hash)
    print("Input password: ",input_password)
    print("Input SHA256 hash", input_sha256_hash)

    if (example_sha256_hash == input_sha256_hash ):
        print("Passwords Match!")
    else:
        print("Passwords do not match")



example_password = input("Enter example password: ").encode("ASCII")
input_password = input("Enter input password: ").encode("ASCII")

sha256_hash_password(example_password, input_password)
