
import urllib.request
import urllib.error
from html.parser import HTMLParser
from urllib.parse import urljoin, urlparse

class LinkParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []

    def handle_starttag(self, tag, attrs):
        if tag.lower() == "a":
            for key, value in attrs:
                if key.lower() == "href" and value:
                    self.links.append(value)
                    break

def main():
    print("\n" + "=" * 42)
    print("      GLORIOUS TECHFORGE")
    print("      WEBSITE LINK CHECKER")
    print("=" * 42)

    url = input("Enter webpage URL: ").strip()
    if not url.startswith(("https://", "http://")):
        url = "https://" + url

    parsed = urlparse(url)
    if not parsed.hostname:
        print("Invalid URL.")
        return

    request = urllib.request.Request(
        url, headers={"User-Agent": "GloriousTechforge-Audit/1.0"}
    )

    try:
        with urllib.request.urlopen(request, timeout=15) as response:
            content_type = response.headers.get("Content-Type", "")
            if "html" not in content_type.lower():
                print("The response does not appear to be HTML.")
                print("Content-Type:", content_type or "Not provided")
                return

            html = response.read(500000).decode("utf-8", errors="replace")
            parser = LinkParser()
            parser.feed(html)

            print("\nPage:", response.url)
            print("HTTP status:", response.status)
            print("Links found:", len(parser.links))
            print("\n--- LINKS ---")

            for number, link in enumerate(parser.links[:50], start=1):
                print(f"{number}. {urljoin(response.url, link)}")

            if len(parser.links) > 50:
                print("Showing first 50 links only.")

            if not parser.links:
                print("No standard HTML links found.")

    except (urllib.error.URLError, TimeoutError, ValueError) as error:
        print("\nRequest failed:", error)

if __name__ == "__main__":
    main()
