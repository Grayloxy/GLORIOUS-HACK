
import socket
import ssl
from datetime import datetime, timezone
from urllib.parse import urlparse

def main():
    print("\n" + "=" * 42)
    print("      GLORIOUS TECHFORGE")
    print("      TLS CERTIFICATE CHECKER")
    print("=" * 42)

    raw_url = input("Enter website URL: ").strip()

    if not raw_url.startswith(("https://", "http://")):
        raw_url = "https://" + raw_url

    parsed = urlparse(raw_url)
    host = parsed.hostname

    if not host:
        print("Invalid website URL.")
        return

    port = parsed.port or 443
    context = ssl.create_default_context()

    try:
        with socket.create_connection((host, port), timeout=10) as sock:
            with context.wrap_socket(sock, server_hostname=host) as secure_sock:
                cert = secure_sock.getpeercert()
                print("\nWebsite:", host)
                print("TLS version:", secure_sock.version())
                print("Certificate verification: PASSED")

                subject = dict(
                    item for group in cert.get("subject", [])
                    for item in group
                )
                issuer = dict(
                    item for group in cert.get("issuer", [])
                    for item in group
                )

                print("Certificate subject:", subject.get("commonName", "Not provided"))
                print("Issuer:", issuer.get("commonName", "Not provided"))

                expiry = cert.get("notAfter")
                if expiry:
                    expiry_date = datetime.strptime(
                        expiry, "%b %d %H:%M:%S %Y %Z"
                    ).replace(tzinfo=timezone.utc)
                    print("Expires (UTC):", expiry_date.isoformat())

                    if expiry_date < datetime.now(timezone.utc):
                        print("Status: EXPIRED")
                    else:
                        print("Status: Not expired")

    except (OSError, ssl.SSLError, ValueError) as error:
        print("\nTLS check failed:", error)
        print("The certificate could not be verified successfully.")

if __name__ == "__main__":
    main()
