import socket
import ssl
from datetime import datetime, timezone
from urllib.parse import urlparse

print("=" * 38)
print("GLORIOUS TECHFORGE")
print("SSL CERTIFICATE CHECKER")
print("=" * 38)

url = input("Enter website URL: ").strip()

if not url.startswith(("https://", "http://")):
    url = "https://" + url

host = urlparse(url).hostname

if not host:
    print("Invalid website URL.")
else:
    try:
        context = ssl.create_default_context()

        with socket.create_connection((host, 443), timeout=10) as sock:
            with context.wrap_socket(sock, server_hostname=host) as secure:
                cert = secure.getpeercert()

        expiry = datetime.strptime(
            cert["notAfter"], "%b %d %H:%M:%S %Y %Z"
        ).replace(tzinfo=timezone.utc)

        print("Website:", host)
        print("Certificate verified: Yes")
        print("Expires:", expiry.strftime("%Y-%m-%d %H:%M UTC"))

        if expiry < datetime.now(timezone.utc):
            print("Warning: Certificate has expired!")
        else:
            print("Certificate is currently within its validity period.")

    except Exception as error:
        print("SSL check failed:", error)
