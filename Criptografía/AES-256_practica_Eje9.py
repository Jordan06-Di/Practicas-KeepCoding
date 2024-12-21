from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import os

# Clave AES(en hexadecimal)
clave_aes_hex = "A2CFF885901A5449E9C448BA5B948A8C4EE377152B3F1ACFA0148FB3A426DB72"
clave_aes = bytes.fromhex(clave_aes_hex)

bloque_ceros=bytes([0] * 16) #Ceros binarios
iv_ceros=bytes([0] * 16) #Ceros binarios

#KCV(SHA-256)
def calcular_kcv_sha256(clave):
    digest = hashes.Hash(hashes.SHA256())
    digest.update(clave)
    hash_sha256 = digest.finalize()
    return hash_sha256[:3]  # Primeros 3 bytes del hash

#KCV(AES)
def calcular_kcv_aes(clave, iv, bloque):
    cipher = Cipher(algorithms.AES(clave), modes.CBC(iv))
    encryptor = cipher.encryptor()
    cifrado = encryptor.update(bloque) + encryptor.finalize()
    return cifrado[:3]  # Primeros 3 bytes del cifrado

kcv_sha256 = calcular_kcv_sha256(clave_aes)
kcv_aes = calcular_kcv_aes(clave_aes, iv_ceros, bloque_ceros)

print("Clave AES:", clave_aes_hex)
print("KCV(SHA-256):", kcv_sha256.hex().upper())
print("KCV(AES):", kcv_aes.hex().upper())
