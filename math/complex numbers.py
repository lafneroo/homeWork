z1 = 2-3j
z2 = 4+7j

Zplus = z1 + z2
Zmin = z1 - z2
Zmul = z1 * z2
Zdiv = z1 / z2
ZconjMul = z1 * z1.conjugate()

print(f"z1 + z2 = {Zplus}")
print(f"z1 - z2 = {Zmin}")
print(f"z1 * z2 = {Zmul}")
print(f"z1 / z2 = ({Zdiv:.1f})")
print(f"z1 * z2* = {ZconjMul}")