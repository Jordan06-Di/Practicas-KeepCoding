from Crypto.Hash import SHA3_256

# Texto en claro
texto = "En KeepCoding aprendemos cómo protegernos con criptografía."

# hash SHA3-256
hash_resultado = SHA3_256.new()
hash_resultado.update(texto.encode('utf-8'))
hash_hex = hash_resultado.hexdigest()

print("hash SHA3 Keccak de 256 bits:", hash_hex)
