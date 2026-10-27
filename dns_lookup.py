import socket

print("=" * 35)
print(" GLORIOUS TECHFORGE")
print(" DNS Lookup Tool")
print("=" * 35)

domain = input("Enter a domain (example.com): ").strip()

try:
    results = socket.getaddrinfo(domain, None)

    addresses = sorted({
        item[4][0] for item in results
    })

    print("\nIP addresses found:")

    for address in addresses:
        print("-", address)

except socket.gaierror:
    print("DNS lookup failed. Check the domain or internet.")

print("\nSecurity learning: Step 7 complete!")
