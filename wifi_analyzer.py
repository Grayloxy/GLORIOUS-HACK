import socket
import subprocess

def command_output(command):
    try:
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            timeout=5
        )
        return result.stdout.strip()
    except (FileNotFoundError, subprocess.TimeoutExpired, OSError):
        return ""

def main():
    while True:
        print("\n" + "=" * 40)
        print("      GLORIOUS TECHFORGE")
        print("      NETWORK ANALYZER")
        print("=" * 40)
        print("1. Network summary")
        print("2. Internet connectivity test")
        print("3. DNS lookup test")
        print("4. Show network properties")
        print("0. Back / Exit")

        choice = input("\nChoose an option: ").strip()

        if choice == "1":
            print("\n--- NETWORK SUMMARY ---")
            print("Connection: Mobile data (expected; verify manually)")
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                sock.connect(("1.1.1.1", 80))
                print("Local IP:", sock.getsockname()[0])
                sock.close()
            except OSError:
                print("Local IP: Unavailable")

            print("Mobile network type:",
                  command_output(["getprop", "gsm.network.type"]) or "Unavailable")
            print("Wi-Fi interface:",
                  command_output(["getprop", "wifi.interface"]) or "Not exposed")
            print("Note: Android may restrict gateway and interface details.")

        elif choice == "2":
            print("\n--- INTERNET TEST ---")
            try:
                with socket.create_connection(("1.1.1.1", 443), timeout=5):
                    print("Internet connectivity: Reachable")
            except OSError:
                print("Internet connectivity: Could not verify")

            try:
                socket.gethostbyname("example.com")
                print("DNS resolution: Working")
            except OSError:
                print("DNS resolution: Failed")

        elif choice == "3":
            domain = input("Enter a domain (e.g. example.com): ").strip()
            domain = domain.removeprefix("https://").removeprefix("http://")
            domain = domain.split("/")[0].split(":")[0]

            try:
                for item in sorted({
                    result[4][0]
                    for result in socket.getaddrinfo(domain, None)
                }):
                    print(item)
            except (socket.gaierror, OSError, ValueError):
                print("Lookup failed. Check the domain or connection.")

        elif choice == "4":
            for prop in (
                "gsm.network.type",
                "gsm.operator.alpha",
                "gsm.operator.numeric",
                "wifi.interface",
                "net.dns1",
                "net.dns2"
            ):
                value = command_output(["getprop", prop])
                print(f"{prop}: {value or 'Unavailable'}")

        elif choice == "0":
            break
        else:
            print("Invalid option.")

        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
