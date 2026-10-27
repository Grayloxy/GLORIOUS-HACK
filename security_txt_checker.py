
import urllib.request
import urllib.error
from urllib.parse import urlparse

def main():
    print("\n" + "=" * 42)
    print("      GLORIOUS TECHFORGE")
    print("      SECURITY.TXT CHECKER")
    print("=" * 42)

    raw_url = input("Enter website URL: ").strip()

    if not raw_url.startswith(("https://", "http://")):
        raw_url = "https://" + raw_url

    parsed = urlparse(raw_url)

    if not parsed.hostname:
        print("Invalid website URL.")
        return

    base = f"{parsed.scheme}://{parsed.netloc}"
    paths = [
        "/.well-known/security.txt",
        "/security.txt"
    ]

    for path in paths:
        target = base + path
        request = urllib.request.Request(
            target,
            headers={"User-Agent": "GloriousTechforge-Audit/1.0"}
        )

        try:
            with urllib.request.urlopen(request, timeout=12) as response:
                content = response.read(10000).decode(
                    "utf-8", errors="replace"
                )

                print("\nFile found at:", response.url)
                print("HTTP status:", response.status)
                print("\n--- FILE CONTENT ---")
                print(content if content.strip() else "(File is empty)")
                return

        except urllib.error.HTTPError as error:
            error.close()
        except (urllib.error.URLError, TimeoutError, ValueError) as error:
            print("\nRequest failed:", error)
            return

    print("\nNo security.txt file found at the two standard paths.")
    print("This does not prove the website has no security contact.")

if __name__ == "__main__":
    main()
