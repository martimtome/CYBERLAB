import hashlib

def sha256_hash(password):
    encoded = password.encode()
    hash_object = hashlib.sha256(encoded)
    return hash_object.hexdigest()

def sha1_hash(password):
    encoded = password.encode()
    hash_object = hashlib.sha1(encoded)
    return hash_object.hexdigest()

def md5_hash(password):
    encoded = password.encode()
    hash_object = hashlib.md5(encoded)
    return hash_object.hexdigest()


