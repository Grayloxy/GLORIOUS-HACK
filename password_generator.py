import secrets
import string

print("=== GLORIOUS TECHFORGE ===")
print("Secure Password Generator")

try:
    length = int(input("Password length (12-64): "))

    if not 12 <= length <= 64:
        print("Choose a length between 12 and 64.")
    else:
        chars = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(
            secrets.choice(chars) for _ in range(length)
        )

        print("\nGenerated password:", password)
        print("Keep it private and store it safely.")

except ValueError:
    print("Please enter a whole number.")

print("\nSecurity learning: Step 5 complete!")
