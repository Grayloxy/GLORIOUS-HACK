import urllib.request
import urllib.error
from urllib.parse import urlparse


def main():
    print("\n=== GLORIOUS TECHFORGE ===")
    print("WEBSITE LINK STATUS CHECKER")
    print("=" * 36)

    url = input("Enter a public URL: ").strip()

    if not url.startswith(("https://", "http://")):
        url = "https://" + url

    parsed = urlparse(url)
    if not parsed.hostname:
        print("Invalid URL.")
        return

    request = urllib.request.Request(
        url,
        headers={"User-Agent": "GloriousTechforge/1.0"},
        method="GET"
    )

    try:
        with urllib.request.urlopen(request, timeout=10) as response:
            print("\nStatus: ONLINE")
            print("HTTP code:", response.status)
            print("Final URL:", response.url)

    except urllib.error.HTTPError as error:
        print("\nThe server responded.")
        print("HTTP code:", error.code)
        print("Final URL:", error.url)

    except (urllib.error.URLError, TimeoutError, ValueError) as error:
        print("\nStatus: CHECK FAILED")
        print("Reason:", error)


if __name__ == "__main__":
    main()
