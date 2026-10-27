import hashlib
from pathlib import Path

print("=" * 38)
print("GLORIOUS TECHFORGE")
print("FILE HASH GENERATOR")
print("=" * 38)

filename = input("Enter file path: ").strip()
path = Path(filename).expanduser()

if not path.is_file():
    print("File not found.")
else:
    digest = hashlib.sha256()

    with path.open("rb") as file:
        for chunk in iter(lambda: file.read(4096), b""):
            digest.update(chunk)

    print("File:", path.name)
    print("SHA-256:", digest.hexdigest())
