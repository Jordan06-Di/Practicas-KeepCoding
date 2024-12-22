from Crypto.PublicKey import RSA
from Crypto.Signature.pkcs1_15 import PKCS115_SigScheme
from Crypto.Hash import SHA256
import binascii
import os

#Cargamos la clave PRIVADA porque generamos una firma
my_path = os.path.abspath(os.getcwd())
path_file_priv = my_path + "\\clave-rsa-oaep-priv.pem"
keypriv = RSA.importKey(open(path_file_priv).read())

mensaje_bytes = bytes("El equipo está preparado para seguir con el proceso, necesitaremos más recursos.","utf-8")
hash = SHA256.new(mensaje_bytes)

signer=PKCS115_SigScheme(keypriv)
firma = signer.sign(hash)
print("Firma: ", firma.hex())
