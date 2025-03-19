from Crypto.PublicKey import RSA
from Crypto.Signature import pss
from Crypto.Hash import SHA256
import base64

def generate_keys():
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    return private_key, public_key


def hash_file(file_path):
    hasher = SHA256.new()
    with open(file_path, 'rb') as f:
        hasher.update(f.read())
    return hasher


def sign_hash(private_key, hash_object):
    private_key = RSA.import_key(private_key)
    signer = pss.new(private_key)
    signature = signer.sign(hash_object)
    return base64.b64encode(signature).decode()


def verify_signature(public_key, hash_object, signature):
    public_key = RSA.import_key(public_key)
    verifier = pss.new(public_key)
    try:
        verifier.verify(hash_object, base64.b64decode(signature))
        return True
    except (ValueError, TypeError):
        return False
    

private_key, public_key = generate_keys()

with open("private.pem", "wb") as f:
    f.write(private_key)
with open("public.pem", "wb") as f:
    f.write(public_key)

print("Pu:", public_key)
print("Pr:", private_key)
file_path = "S.txt"
hash_object = hash_file(file_path)
signature = sign_hash(private_key, hash_object)

print("Hash (file):", hash_object.hexdigest())
print("Sign:", signature)

is_valid = verify_signature(public_key, hash_object, signature)
print("Verify Signature:", "Successfully" if is_valid else "Unsuccessfully")