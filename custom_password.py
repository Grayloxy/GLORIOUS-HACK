import secrets
import string

print("=" * 38)
print("GLORIOUS TECHFORGE")
print("CUSTOM PASSWORD GENERATOR")
print("=" * 38)

try:
    length = int(input("Password length (8-128): "))

    if not 8 <= length <= 128:
        print("Choose a length between 8 and 128.")
    else:
        characters = string.ascii_letters + string.digits + "!@#$%&*?"
        password = "".join(
            secrets.choice(characters) for _ in range(length)
        )

        print("Generated password:", password)
        print("Store it somewhere secure.")
except ValueError:
    print("Please enter a valid whole number.")
