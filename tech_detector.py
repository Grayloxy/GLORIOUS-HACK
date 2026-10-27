
import urllib.request
import urllib.error

def main():
    print("\n" + "=" * 42)
    print("      GLORIOUS TECHFORGE")
    print("      WEBSITE TECHNOLOGY DETECTOR")
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
            print("\n--- TECHNOLOGY CLUES ---")

            clues = [
                "Server",
                "X-Powered-By",
                "Via",
                "X-Generator",
                "X-AspNet-Version",
                "CF-Ray"
            ]

            found = False

            for name in clues:
                value = headers.get(name)
                if value:
                    print(f"{name}: {value}")
                    found = True

            if not found:
                print("No common technology clues exposed in headers.")

            print("\nNote: Headers may be hidden or misleading.")

    except (urllib.error.URLError, TimeoutError, ValueError) as error:
        print("\nCould not check website:", error)

if __name__ == "__main__":
    main()
