import hashlib
from pathlib import Path

print("=" * 38)
print("GLORIOUS TECHFORGE")
print("FILE INTEGRITY CHECKER")
print("=" * 38)

filename = input("Enter the path to your file: ").strip()
path = Path(filename).expanduser()

if not path.is_file():
    print("File not found. Check the path and try again.")
else:
    sha256 = hashlib.sha256()

    with path.open("rb") as file:
        for chunk in iter(lambda: file.read(4096), b""):
            sha256.update(chunk)

    print("File:", path.name)
    print("SHA-256:", sha256.hexdigest())
    print("Save this hash to compare it after future changes.")
