from base64 import b64decode
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import json


# Texto cifrado en base64
texto_cifrado_b64 = "TQ9SOMKc6aFS9SlxhfK9wT18UXpPCd505Xf5J/5nLI7Of/o0QKIWXg3nu1RRz4QWElezdrLAD5LO4USt3aB/i50nvvJbBiG+le1ZhpR84oI="
clave = bytes.fromhex("A2CFF885901A5449E9C448BA5B948A8C4EE377152B3F1ACFA0148FB3A426DB72")  # keystore
iv = bytes([0] * 16) #Ceros binarios

# Decodificar texto cifrado desde Base64
texto_cifrado = b64decode(texto_cifrado_b64)
cipher = AES.new(clave, AES.MODE_CBC,iv)

# Descifrar los datos
texto_descifrado_bytes = cipher.decrypt(texto_cifrado)
texto_descifrado = unpad(texto_descifrado_bytes, AES.block_size, style='pkcs7')

print(f"Texto en claro: {texto_descifrado.decode('UTF-8')}")

# Descifrar los datos usando AES-256-CBC con X.923 padding
cipher = AES.new(clave, AES.MODE_CBC, iv)
texto_descifrado_x923 = unpad(cipher.decrypt(texto_cifrado), AES.block_size, style='x923')

print("Texto descifrado en claro (X.923):", texto_descifrado_x923.decode('utf-8'))



