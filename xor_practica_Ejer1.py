#XOR de datos binarios
def xor_data(binary_data_1, binary_data_2):
    return bytes([b1 ^ b2 for b1, b2 in zip(binary_data_1, binary_data_2)])


k1 = bytes.fromhex("B1EF2ACFE2BAEEFF")
k2 = bytes.fromhex("91BA13BA21AABB12")

print(xor_data(k1,k2).hex())

K1=0xB1EF2ACFE2BAEEFF
K2=0xB98A15BA31AEBB3F
KEY=(hex(K1^K2))
print(KEY[2:])


