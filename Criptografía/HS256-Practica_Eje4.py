import jwt

# Clave secreta
key = "Con KeepCoding aprendemos"

# JWT original
original_jwt = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c3VhcmlvIjoiRG9uIFBlcGl0byBkZSBsb3MgcGFsb3RlcyIsInJvbCI6ImlzTm9ybWFsIiwiaWF0IjoxNjY3OTMzNTMzfQ.gfhw0dDxp6oixMLXXRP97W4TDTrv0y7B5YjD0U8ixrE"

# JWT manipulado
hacked_jwt = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c3VhcmlvIjoiRG9uIFBlcGl0byBkZSBsb3MgcGFsb3RlcyIsInJvbCI6ImlzQWRtaW4iLCJpYXQiOjE2Njc5MzM1MzN9.krgBkzCBQ5WZ8JnZHuRvmnAZdg4ZMeRNv2CIAODlHRI"

try:
    # Decodificar y verificar el JWT original
    decoded_original = jwt.decode(original_jwt, key, algorithms=["HS256"])
    print("JWT original válido:", decoded_original)
except jwt.InvalidSignatureError:
    print("La firma del JWT original no es válida.")

try:
    # Decodificar y verificar el JWT manipulado
    decoded_hacked = jwt.decode(hacked_jwt, key, algorithms=["HS256"])
    print("JWT manipulado válido:", decoded_hacked)
except jwt.InvalidSignatureError:
    print("La firma del JWT manipulado no es válida.")

#Lo validamos con pyjwt
# token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c3VhcmlvIjoiRG9uIFBlcGl0byBkZSBsb3MgcGFsb3RlcyIsInJvbCI6ImlzQWRtaW4iLCJpYXQiOjE2Njc5MzM1MzN9.krgBkzCBQ5WZ8JnZHuRvmnAZdg4ZMeRNv2CIAODlHRI"

# try:
#     decoded = jwt.decode(token, key, algorithms=["HS256"])
#     print(decoded)
# except jwt.exceptions.InvalidSignatureError:
#     print("Error: La firma no es válida")


