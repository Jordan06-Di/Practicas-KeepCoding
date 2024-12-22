from cryptography.hazmat.primitives.asymmetric import ed25519
from cryptography.hazmat.primitives import hashes
import binascii
import os


my_path = os.path.abspath(os.getcwd())
path_file_priv = my_path + "\\ed25519-priv.gpg"

with open(path_file_priv, "rb") as f:
    private_key_bytes = f.read()

private_key = ed25519.Ed25519PrivateKey.from_private_bytes(private_key_bytes)
mensaje_bytes = bytes("El equipo está preparado para seguir con el proceso, necesitaremos más recursos.", "utf-8")

hash = hashes.Hash(hashes.SHA256())
hash.update(mensaje_bytes)
mensaje_hash = hash.finalize()

firma = private_key.sign(mensaje_bytes)

print("Firma Ed25519: ", firma.hex())

