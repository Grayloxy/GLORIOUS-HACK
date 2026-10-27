import socket
import urllib.request

print("=" * 35)
print(" GLORIOUS TECHFORGE")
print(" Network Information Tool")
print("=" * 35)

try:
    print("Device hostname:", socket.gethostname())

    with urllib.request.urlopen(
        "https://example.com", timeout=10
    ) as response:
        print("Internet connection: Working")
        print("HTTP status:", response.status)

except Exception as error:
    print("Connection check failed:", error)

print("=" * 35)
print("Security learning: Step 1 complete!")
