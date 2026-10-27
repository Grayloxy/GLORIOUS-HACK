import hmac

print("=" * 38)
print("GLORIOUS TECHFORGE")
print("HASH COMPARISON CHECKER")
print("=" * 38)

first = input("Enter the original SHA-256 hash: ").strip().lower()
second = input("Enter the new SHA-256 hash: ").strip().lower()

if len(first) != 64 or len(second) != 64:
    print("Error: SHA-256 hashes must contain 64 hexadecimal characters.")
elif any(c not in "0123456789abcdef" for c in first + second):
    print("Error: Hashes must contain only hexadecimal characters.")
elif hmac.compare_digest(first, second):
    print("MATCH: The hashes are identical.")
else:
    print("MISMATCH: The hashes are different.")
