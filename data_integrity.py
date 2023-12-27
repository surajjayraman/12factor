import hashlib


def calculate_checksum(file_path):

    with open(file_path, "rb") as f:

        file_hash = hashlib.sha256()

        while chunk := f.read(4096):

            file_hash.update(chunk)
    
    return file_hash.hexdigest()




