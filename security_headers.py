import urllib.request
import urllib.error

def main():
    print("\n" + "=" * 42)
    print("      GLORIOUS TECHFORGE")
    print("      SECURITY HEADER CHECKER")
    print("=" * 42)

    url = input("Enter website URL: ").strip()

    if not url.startswith(("https://", "http://")):
        url = "https://" + url

    request = urllib.request.Request(
        url,
        headers={"User-Agent": "GloriousTechforge-Audit/1.0"},
        method="GET"
    )

    try:
        with urllib.request.urlopen(request, timeout=10) as response:
            headers = response.headers
            print("\nWebsite:", response.url)
            print("HTTP status:", response.status)

            checks = {
                "Content-Security-Policy":
                    "Helps control which resources can load",
                "Strict-Transport-Security":
                    "Helps enforce HTTPS",
                "X-Content-Type-Options":
                    "Helps prevent MIME-type sniffing",
                "X-Frame-Options":
                    "Helps reduce clickjacking risks",
                "Referrer-Policy":
                    "Controls referrer information",
                "Permissions-Policy":
                    "Controls access to browser features"
            }

            print("\n--- HEADER RESULTS ---")

            for name, explanation in checks.items():
                if headers.get(name):
                    print("[PRESENT]", name)
                else:
                    print("[MISSING]", name)
                    print("          ", explanation)

            print("\nNote: Missing headers are not proof of a vulnerability.")

    except (urllib.error.URLError, TimeoutError, ValueError) as error:
        print("\nCould not check website:", error)

if __name__ == "__main__":
    main()
