
import socket
import ipaddress
import urllib.request
import json

def main():
    print("=" * 40)
    print("       GLORIOUS TECHFORGE")
    print("       IP & DNS INTELLIGENCE")
    print("=" * 40)
    print("1. Domain IP lookup")
    print("2. DNS records (A, AAAA, MX, NS, TXT)")
    print("3. Public IP information")
    print("0. Back to main menu")

    choice = input("\nChoose an option: ").strip()

    if choice == "1":
        domain = input("Enter domain (e.g. example.com): ").strip()
        domain = domain.removeprefix("https://").removeprefix("http://")
        domain = domain.split("/")[0].split(":")[0]

        try:
            results = socket.getaddrinfo(domain, None)
            addresses = sorted({item[4][0] for item in results})
            print("\nIP addresses:")
            for address in addresses:
                print(" -", address)
        except (socket.gaierror, ValueError, OSError):
            print("Lookup failed. Check the domain and internet connection.")

    elif choice == "2":
        domain = input("Enter domain (e.g. example.com): ").strip()
        domain = domain.removeprefix("https://").removeprefix("http://")
        domain = domain.split("/")[0].split(":")[0]

        try:
            ipaddress.ip_address(domain)
            print("Please enter a domain name, not an IP address.")
            return
        except ValueError:
            pass

        try:
            import subprocess
            result = subprocess.run(
                ["nslookup", "-type=ANY", domain],
                capture_output=True, text=True, timeout=10
            )
            print(result.stdout or result.stderr)
            print("Note: Some DNS servers do not provide all record types.")
        except (FileNotFoundError, subprocess.TimeoutExpired):
            print("DNS lookup tool unavailable or timed out.")

    elif choice == "3":
        try:
            request = urllib.request.Request(
                "https://ipinfo.io/json",
                headers={"User-Agent": "GloriousTechforge/1.0"}
            )
            with urllib.request.urlopen(request, timeout=10) as response:
                data = json.loads(response.read().decode())

            print("\nPublic IP information:")
            for field in ("ip", "city", "region", "country", "org", "timezone"):
                if field in data:
                    print(f"{field.title()}: {data[field]}")
            print("\nLocation is approximate and may reflect your ISP or VPN.")
        except Exception as error:
            print("Could not retrieve public IP information:", error)

    elif choice == "0":
        return
    else:
        print("Invalid option.")

if __name__ == "__main__":
    main()
