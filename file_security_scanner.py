import hashlib
import os

def calculate_hash(filepath, algorithm="sha256"):
    digest = hashlib.new(algorithm)

    with open(filepath, "rb") as file:
        for chunk in iter(lambda: file.read(65536), b""):
            digest.update(chunk)

    return digest.hexdigest()


def main():
    while True:
        print("\n" + "=" * 42)
        print("       GLORIOUS TECHFORGE")
        print("       FILE SECURITY SCANNER")
        print("=" * 42)
        print("1. Scan a file")
        print("2. Compare a file with a known SHA-256 hash")
        print("0. Back / Exit")

        choice = input("\nChoose an option: ").strip()

        if choice == "1":
            path = input("Enter the file path: ").strip().strip('"')

            if not os.path.isfile(path):
                print("File not found. Check the path and try again.")
            else:
                try:
                    result = calculate_hash(path)
                    print("\nFile:", os.path.basename(path))
                    print("Size:", os.path.getsize(path), "bytes")
                    print("SHA-256:", result)
                    print("Integrity fingerprint generated.")
                    print("Note: A hash alone cannot prove a file is safe.")
                except (OSError, ValueError) as error:
                    print("Could not scan file:", error)

        elif choice == "2":
            path = input("Enter the file path: ").strip().strip('"')
            expected = input("Enter the trusted SHA-256 hash: ").strip().lower()

            if not os.path.isfile(path):
                print("File not found. Check the path and try again.")
            elif len(expected) != 64 or any(
                char not in "0123456789abcdef" for char in expected
            ):
                print("Invalid SHA-256 hash. It must contain 64 hexadecimal characters.")
            else:
                try:
                    actual = calculate_hash(path)
                    if actual == expected:
                        print("MATCH: The file matches the supplied hash.")
                    else:
                        print("MISMATCH: The file differs from the supplied hash.")
                except OSError as error:
                    print("Could not compare file:", error)

        elif choice == "0":
            break

        else:
            print("Invalid option.")

        input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()
