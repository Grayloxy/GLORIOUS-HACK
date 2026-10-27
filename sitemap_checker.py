
import urllib.request
import urllib.error
from urllib.parse import urlparse

def main():
    print("\n" + "=" * 42)
    print("      GLORIOUS TECHFORGE")
    print("      WEBSITE SITEMAP CHECKER")
    print("=" * 42)

    raw_url = input("Enter website URL: ").strip()

    if not raw_url.startswith(("https://", "http://")):
        raw_url = "https://" + raw_url

    parsed = urlparse(raw_url)

    if not parsed.hostname:
        print("Invalid website URL.")
        return

    sitemap_url = f"{parsed.scheme}://{parsed.netloc}/sitemap.xml"
    request = urllib.request.Request(
        sitemap_url,
        headers={"User-Agent": "GloriousTechforge-Audit/1.0"}
    )

    try:
        with urllib.request.urlopen(request, timeout=15) as response:
            content = response.read(2000).decode("utf-8", errors="replace")

            print("\nSitemap URL:", sitemap_url)
            print("HTTP status:", response.status)
            print("Content type:", response.headers.get(
                "Content-Type", "Not provided"
            ))
            print("\n--- CONTENT PREVIEW ---")
            print(content if content.strip() else "(Empty response)")

            if "<urlset" in content or "<sitemapindex" in content:
                print("\nXML sitemap markers detected.")
            else:
                print("\nStandard sitemap XML markers not detected in preview.")

    except urllib.error.HTTPError as error:
        print("\nHTTP status:", error.code)
        print("The sitemap could not be retrieved at this path.")
        error.close()

    except (urllib.error.URLError, TimeoutError, ValueError) as error:
        print("\nRequest failed:", error)

if __name__ == "__main__":
    main()
