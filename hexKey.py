def find_key(original, transformed):
    key = ''.join(f"\\x{ord(o) ^ ord(t):02X}" for o, t in zip(original, transformed))
    return key

original = "iron"
transformed = "gold"

found_key = find_key(original, transformed)

print(f"Original: {original}")
print(f"Transformed: {transformed}")
print(f"Found Key: {found_key}")

