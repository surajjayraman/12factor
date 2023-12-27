import hashlib


def calculate_checksum(file_path):

    with open(file_path, "rb") as f:
        file_hash = hashlib.sha256()


