
import urllib.request
import urllib.error
from html.parser import HTMLParser
from urllib.parse import urlparse

class MetadataParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.title = ""
        self.in_title = False
        self.description = ""
        self.keywords = ""

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)

        if tag.lower() == "title":
            self.in_title = True

        if tag.lower() == "meta":
            name = attrs.get("name", "").lower()
            content = attrs.get("content", "")

            if name == "description":
                self.description = content
            elif name == "keywords":
                self.keywords = content

    def handle_endtag(self, tag):
        if tag.lower() == "title":
            self.in_title = False

    def handle_data(self, data):
        if self.in_title:
            self.title += data

def main():
    print("\n" + "=" * 42)
    print("      GLORIOUS TECHFORGE")
    print("      WEBSITE METADATA INSPECTOR")
    print("=" * 42)

    url = input("Enter webpage URL: ").strip()

    if not url.startswith(("https://", "http://")):
        url = "https://" + url

    if not urlparse(url).hostname:
        print("Invalid website URL.")
        return

    request = urllib.request.Request(
        url,
        headers={"User-Agent": "GloriousTechforge-Audit/1.0"}
    )

    try:
        with urllib.request.urlopen(request, timeout=15) as response:
            content_type = response.headers.get("Content-Type", "")

            print("\nWebsite:", response.url)
            print("HTTP status:", response.status)

            if "html" not in content_type.lower():
                print("The response is not identified as HTML.")
                return

            html = response.read(500000).decode(
                "utf-8", errors="replace"
            )

            parser = MetadataParser()
            parser.feed(html)

            print("\n--- PAGE METADATA ---")
            print("Title:", parser.title.strip() or "Not found")
            print("Description:", parser.description or "Not found")
            print("Keywords:", parser.keywords or "Not found")

    except (urllib.error.URLError, TimeoutError, ValueError) as error:
        print("\nRequest failed:", error)

if __name__ == "__main__":
    main()
