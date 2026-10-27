
import urllib.request
import urllib.error

def main():
    print("\n" + "=" * 42)
    print("      GLORIOUS TECHFORGE")
    print("      CONTENT-TYPE CHECKER")
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
            content_type = response.headers.get(
                "Content-Type", "Not provided"
            )

            print("\nFinal URL:", response.url)
            print("HTTP status:", response.status)
            print("Content-Type:", content_type)

            media_type = content_type.split(";")[0].strip().lower()

            if media_type == "text/html":
                print("Detected format: HTML webpage")
            elif media_type == "application/json":
                print("Detected format: JSON data")
            elif media_type.startswith("image/"):
                print("Detected format: Image")
            elif media_type.startswith("text/"):
                print("Detected format: Text content")
            elif media_type == "application/pdf":
                print("Detected format: PDF document")
            elif media_type == "application/octet-stream":
                print("Detected format: Generic binary data")
            else:
                print("Detected format: Other or unspecified type")

    except urllib.error.HTTPError as error:
        print("\nHTTP status:", error.code)
        print("Content-Type:", error.headers.get(
            "Content-Type", "Not provided"
        ))
        error.close()

    except (urllib.error.URLError, TimeoutError, ValueError) as error:
        print("\nRequest failed:", error)

if __name__ == "__main__":
    main()
