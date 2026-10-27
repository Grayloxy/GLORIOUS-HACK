
import urllib.request
import urllib.error

def main():
    print("\n" + "=" * 42)
    print("      GLORIOUS TECHFORGE")
    print("      HTTP METHODS CHECKER")
    print("=" * 42)

    url = input("Enter website URL: ").strip()

    if not url.startswith(("https://", "http://")):
        url = "https://" + url

    request = urllib.request.Request(
        url,
        headers={"User-Agent": "GloriousTechforge-Audit/1.0"},
        method="OPTIONS"
    )

    try:
        with urllib.request.urlopen(request, timeout=15) as response:
            print("\nWebsite:", response.url)
            print("HTTP status:", response.status)

            allow = response.headers.get("Allow")
            public = response.headers.get("Public")

            if allow:
                print("Allow header:", allow)
            else:
                print("Allow header: Not provided")

            if public:
                print("Public header:", public)

            if not allow and not public:
                print("Advertised methods: Not disclosed")
                print("This does not mean HTTP methods are unavailable.")

    except urllib.error.HTTPError as error:
        print("\nHTTP status:", error.code)
        print("Allow header:",
              error.headers.get("Allow", "Not provided"))
        error.close()

    except (urllib.error.URLError, TimeoutError, ValueError) as error:
        print("\nRequest failed:", error)

if __name__ == "__main__":
    main()
