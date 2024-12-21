from Crypto.Cipher import ChaCha20_Poly1305
from base64 import b64decode, b64encode
from Crypto.Random import get_random_bytes
import json

try:

    textoPlano_bytes = bytes('KeepCoding te enseña a codificar y a cifrar', 'UTF-8')
    clave = bytes.fromhex('AF9DF30474898787A45605CCB9B936D33B780D03CABC81719D52383480DC3120') #Clave hmac256 del keyStore

    #Importante NUNCA debe fijarse el nonce
    nonce_mensaje_bytes=b64decode("9Yccn/f5nJJhAt2S")

    #Con la clave y con el nonce se cifra. El nonce debe ser único por mensaje
    #Hoy decido que no tenga datos asociados
    datos_asociados = bytes('', 'utf-8')

    cipher = ChaCha20_Poly1305.new(key=clave, nonce=nonce_mensaje_bytes)
    #Por ser cifrado autenticado hacemos un update (lo mismo ocurria en AES-GCM)
    cipher.update(datos_asociados)
    texto_cifrado, tag = cipher.encrypt_and_digest(textoPlano_bytes)
    print("nonce:", b64encode(nonce_mensaje_bytes).decode())
    print("Encrypt Text:", b64encode(texto_cifrado).decode())
    print("Datos asociados:", b64encode(datos_asociados).decode())
    print("Tag:", b64encode(tag).decode())


#     #Descifrado...

    decipher = ChaCha20_Poly1305.new(key=clave, nonce=nonce_mensaje_bytes)
    decipher.update(datos_asociados)
    plaintext = decipher.decrypt_and_verify(texto_cifrado,tag)
    print('Datos cifrados en claro = ',plaintext.decode('utf-8'))
except (ValueError, KeyError) as error: 
     print("Problemas al descifrar....")
     print("El motivo del error es: ", error)