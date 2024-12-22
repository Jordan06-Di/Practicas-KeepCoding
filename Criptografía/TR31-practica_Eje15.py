from psec import tr31

# Documentado en este fichero
# https://github.com/knovichikhin/psec/blob/master/psec/tr31.py

# Luigi y Felipe hemos compartido una clave (KEK) -- KEK:
# A1A10101010101010101010101010103 --> ZMK
# TR31 (Key Block): D0144D0AB005000061653A93F145C3A99375BAADE92C5BB69523F8D15EA97FE416BF3AA266F69626488B2A66F2D21F44AE1C1DF8790688802F13FB925CB47737D0861DA2C9D75D30

header, key = tr31.unwrap(
    kpbk=bytes.fromhex("A1A10101010101010101010101010102"),
    key_block="D0144D0AB005000042766B9265B2DF93AE6E29B58135B77A2F616C8D515ACDBE6A5626F79FA7B4071E9EE1423C6D7970FA2B965D18B23922B5B2E5657495E03CD857FD37018E111B"
)
print("Clave=", key.hex())

print("Key Version ID: " + header.version_id)
print("Algoritmo: " + header.algorithm)
print("Modo de uso: " + header.mode_of_use)
print("Uso de la clave: " + header.key_usage)
print("Exportabilidad: " + header.exportability)

header2, key2 = tr31.unwrap(
    kpbk=bytes.fromhex("A1A10101010101010101010101010102"),
    key_block="D0144D0AB005000042766B9265B2DF93AE6E29B58135B77A2F616C8D515ACDBE6A5626F79FA7B4071E9EE1423C6D7970FA2B965D18B23922B5B2E5657495E03CD857FD37018E111B"
)
print("Clave=", key2.hex())

print("Key Version ID: " + header2.version_id)
print("Algoritmo: " + header2.algorithm)
print("Modo de uso: " + header2.mode_of_use)
print("Uso de la clave: " + header2.key_usage)
print("Exportabilidad: " + header2.exportability)
















