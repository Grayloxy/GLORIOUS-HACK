
import subprocess

def lookup(record, domain):
    try:
        result = subprocess.run(
            ["nslookup", "-type=" + record, domain],
            capture_output=True,
            text=True,
            timeout=10
        )
        return result.stdout + result.stderr
    except (OSError, subprocess.TimeoutExpired) as error:
        return str(error)

def main():
    print("\n" + "=" * 42)
    print("      GLORIOUS TECHFORGE")
    print("      DNS SECURITY CHECKER")
    print("=" * 42)

    domain = input("Enter domain (e.g. example.com): ").strip()

    if not domain or "/" in domain or " " in domain:
        print("Please enter a domain name only.")
        return

    print("\nChecking:", domain)

    for record in ("TXT", "DNSKEY"):
        result = lookup(record, domain)
        print(f"\n--- {record} RECORD QUERY ---")

        if result.strip():
            print(result.strip())
        else:
            print("No response text returned.")

    print("\nNote:")
    print("- TXT results may contain SPF or other policies.")
    print("- DMARC is normally queried at _dmarc.yourdomain.")
    print("- A failed DNSKEY lookup alone does not prove DNSSEC is disabled.")

if __name__ == "__main__":
    main()
