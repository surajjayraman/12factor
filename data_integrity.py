import hashlib


def calculate_checksum(file_path):

    with open(file_path, "rb") as f:

        file_hash = hashlib.sha256()

        while chunk := f.read(4096):

            file_hash.update(chunk)
    
    return file_hash.hexdigest()

file_path = "example_file.txt"

checksum = calculate_checksum(file_path)

print("The checksum of ", file_path, " is ", checksum)

with open(file_path, "w") as f:
    f.write("This file has been modified")


