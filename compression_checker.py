
import urllib.request
import urllib.error

def main():
    print("\n" + "=" * 42)
    print("      GLORIOUS TECHFORGE")
    print("      WEBSITE COMPRESSION CHECKER")
    print("=" * 42)

    url = input("Enter website URL: ").strip()

    if not url.startswith(("https://", "http://")):
        url = "https://" + url

    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": "GloriousTechforge-Audit/1.0",
            "Accept-Encoding": "gzip, br, deflate"
        }
    )

    try:
        with urllib.request.urlopen(request, timeout=15) as response:
            encoding = response.headers.get(
                "Content-Encoding", "Not specified"
            )

            print("\nWebsite:", response.url)
            print("HTTP status:", response.status)
            print("Content-Encoding:", encoding)

            if encoding.lower() in ("gzip", "br", "deflate"):
                print("Compression: Reported by server")
            else:
                print("Compression: No supported encoding reported")

            print("\nNote: This checks response headers, not actual size savings.")

    except urllib.error.HTTPError as error:
        print("\nHTTP status:", error.code)
        print("Content-Encoding:",
              error.headers.get("Content-Encoding", "Not specified"))
        error.close()

    except (urllib.error.URLError, TimeoutError, ValueError) as error:
        print("\nRequest failed:", error)

if __name__ == "__main__":
    main()
