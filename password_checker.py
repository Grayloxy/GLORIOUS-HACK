import getpass
import string

print("=== GLORIOUS TECHFORGE ===")
print("Password Strength Checker")

password = getpass.getpass("Enter a test password: ")
score = 0

if len(password) >= 12:
    score += 2
elif len(password) >= 8:
    score += 1

if any(c.islower() for c in password):
    score += 1
if any(c.isupper() for c in password):
    score += 1
if any(c.isdigit() for c in password):
    score += 1
if any(c in string.punctuation for c in password):
    score += 1

if score <= 2:
    print("Result: Weak")
elif score <= 4:
    print("Result: Moderate")
else:
    print("Result: Stronger by basic checks")

print("Security learning: Step 3 complete!")
