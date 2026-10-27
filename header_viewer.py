
import urllib.request
import urllib.error

def main():
    print("\n" + "=" * 42)
    print("      GLORIOUS TECHFORGE")
    print("      HTTP HEADER VIEWER")
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
        with urllib.request.urlopen(request, timeout=15) as response:
            print("\nFinal URL:", response.url)
            print("HTTP status:", response.status)
            print("\n--- RESPONSE HEADERS ---")

            for name, value in response.headers.items():
                print(f"{name}: {value}")

    except urllib.error.HTTPError as error:
        print("\nHTTP status:", error.code)
        print("--- RESPONSE HEADERS ---")

        for name, value in error.headers.items():
            print(f"{name}: {value}")

        error.close()

    except (urllib.error.URLError, TimeoutError, ValueError) as error:
        print("\nRequest failed:", error)

if __name__ == "__main__":
    main()
