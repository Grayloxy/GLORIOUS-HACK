import urllib.request

print("=== GLORIOUS TECHFORGE ===")
print("Website Security Header Checker")

url = input("Enter website URL: ").strip()

if not url.startswith("https://"):
    print("Please enter a URL beginning with https://")
else:
    try:
        request = urllib.request.Request(
            url, headers={"User-Agent": "GloriousSecurityLab/1.0"}
        )

        with urllib.request.urlopen(request, timeout=10) as response:
            headers = response.headers

            print("\nWebsite:", url)
            print("HTTP status:", response.status)

            checks = [
                "Strict-Transport-Security",
                "Content-Security-Policy",
                "X-Content-Type-Options",
                "X-Frame-Options",
            ]

            for header in checks:
                if header in headers:
                    print(f"[FOUND] {header}")
                else:
                    print(f"[NOT FOUND] {header}")

    except Exception as error:
        print("Could not check website:", error)

print("\nSecurity learning: Step 4 complete!")

