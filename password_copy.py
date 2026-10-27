import secrets
import string
import subprocess

print("=" * 38)
print("GLORIOUS TECHFORGE")
print("PASSWORD GENERATOR + AUTO-COPY")
print("=" * 38)

try:
    length = int(input("Password length (8-128): "))

    if not 8 <= length <= 128:
        print("Choose a length between 8 and 128.")
    else:
        chars = string.ascii_letters + string.digits + "!@#$%&*?"
        password = "".join(secrets.choice(chars) for _ in range(length))

        print("Generated password:", password)

        try:
            subprocess.run(
                ["termux-clipboard-set"],
                input=password,
                text=True,
                check=True
            )
            print("Password copied to clipboard!")
            print("Paste it only into a trusted password manager.")
        except Exception:
            print("Clipboard copy failed. Copy it manually.")
except ValueError:
    print("Please enter a valid whole number.")
