import hmac
import hashlib

clave_hex = 'A212A51C997E14B4DF08D55967641B0677CA31E049E672A4B06861AA4D5826EB' #KeyStorePracticas Hmac-SHA256
clave = bytes.fromhex(clave_hex)
mensaje_en_claro = "Siempre existe más de una forma de hacerlo, y más de una solución válida."


hmac_result = hmac.new(clave, mensaje_en_claro.encode('utf-8'), hashlib.sha256)
hmac_hex = hmac_result.hexdigest()

print("HMAC-SHA256:", hmac_hex)
