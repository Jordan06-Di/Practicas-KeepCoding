from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives.hashes import SHA512
from cryptography.hazmat.backends import default_backend
import binascii

# Clave del keystore "cifrado-sim-aes-256"
key = bytes.fromhex("A2CFF885901A5449E9C448BA5B948A8C4EE377152B3F1ACFA0148FB3A426DB72")
id = bytes.fromhex("e43bb4067cbcfab3bec54437b84bef4623e345682d89de9948fbb0afedc461a3")
salt = None 

hkdf = HKDF(
    algorithm=SHA512(),
    length=32,
    salt=salt,
    info=id,
    backend=default_backend()
)

key_derivada = hkdf.derive(key)
key_derivada_hex = binascii.hexlify(key_derivada).decode()

print("Clave derivada:", key_derivada_hex)
