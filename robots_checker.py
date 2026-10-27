
import urllib.request
import urllib.error
from urllib.parse import urlparse

def main():
    print("\n" + "=" * 42)
    print("      GLORIOUS TECHFORGE")
    print("      ROBOTS.TXT CHECKER")
    print("=" * 42)

    raw_url = input("Enter website URL: ").strip()

    if not raw_url.startswith(("https://", "http://")):
        raw_url = "https://" + raw_url

    parsed = urlparse(raw_url)

    if not parsed.hostname:
        print("Invalid website URL.")
        return

    robots_url = f"{parsed.scheme}://{parsed.netloc}/robots.txt"
    request = urllib.request.Request(
        robots_url,
        headers={"User-Agent": "GloriousTechforge-Audit/1.0"}
    )

    try:
        with urllib.request.urlopen(request, timeout=15) as response:
            content = response.read(50000).decode("utf-8", errors="replace")
            print("\nRobots URL:", robots_url)
            print("HTTP status:", response.status)
            print("\n--- ROBOTS.TXT CONTENT ---")
            print(content if content.strip() else "(File is empty)")

    except urllib.error.HTTPError as error:
        print("\nRobots URL:", robots_url)
        print("HTTP status:", error.code)
        print("The file could not be retrieved.")
        error.close()

    except (urllib.error.URLError, TimeoutError, ValueError) as error:
        print("\nRequest failed:", error)

if __name__ == "__main__":
    main()

