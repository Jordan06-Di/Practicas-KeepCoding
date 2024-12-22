from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
import base64
import binascii


key = bytes.fromhex("E2CFF885901B3449E9C448BA5B948A8C4EE322152B3F1ACFA0148FB3A426DB74")
nonce = base64.b64decode("9Yccn/f5nJJhAt2S")
texto_para_cifrar = "He descubierto el error y no volveré a hacerlo mal"

padder = padding.PKCS7(128).padder()
padded_data = padder.update(texto_para_cifrar.encode()) + padder.finalize()


cipher = Cipher(algorithms.AES(key), modes.GCM(nonce), backend=default_backend())
encryptor = cipher.encryptor()
ciphertext = encryptor.update(padded_data) + encryptor.finalize()
tag = encryptor.tag 

ciphertext_hex = binascii.hexlify(ciphertext).decode()
ciphertext_base64 = base64.b64encode(ciphertext).decode()

tag_hex = binascii.hexlify(tag).decode()
tag_base64 = base64.b64encode(tag).decode()

print("Texto cifrado en hexadecimal:", ciphertext_hex)
print("Texto cifrado en base64:", ciphertext_base64)
print("Tag de autenticación en hexadecimal:", tag_hex)
print("Tag de autenticación en base64:", tag_base64)

# Descifrado
cipher = Cipher(algorithms.AES(key), modes.GCM(nonce, tag), backend=default_backend())
decryptor = cipher.decryptor()

deciphered_padded_data = decryptor.update(ciphertext) + decryptor.finalize()

# Eliminar el padding
unpadder = padding.PKCS7(128).unpadder()
texto_deciphered = unpadder.update(deciphered_padded_data) + unpadder.finalize()

print("Texto descifrado:", texto_deciphered.decode())

