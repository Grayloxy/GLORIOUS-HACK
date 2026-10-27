
import urllib.request
import urllib.error

def main():
    print("\n" + "=" * 42)
    print("      GLORIOUS TECHFORGE")
    print("      WEBSITE COOKIE INSPECTOR")
    print("=" * 42)

    url = input("Enter website URL: ").strip()

    if not url.startswith(("https://", "http://")):
        url = "https://" + url

    request = urllib.request.Request(
        url,
        headers={"User-Agent": "GloriousTechforge-Audit/1.0"}
    )

    try:
        with urllib.request.urlopen(request, timeout=15) as response:
            cookies = response.headers.get_all("Set-Cookie") or []

            print("\nWebsite:", response.url)
            print("HTTP status:", response.status)
            print("Cookies received:", len(cookies))

            if not cookies:
                print("No Set-Cookie headers were returned.")
                return

            for number, cookie in enumerate(cookies, start=1):
                parts = [part.strip() for part in cookie.split(";")]
                name = parts[0].split("=", 1)[0] if parts else "Unknown"
                attributes = [p.lower() for p in parts[1:]]

                print(f"\nCookie {number}: {name}")
                print("Secure:", any(p == "secure" for p in attributes))
                print("HttpOnly:", any(p == "httponly" for p in attributes))
                print("SameSite:", next(
                    (p.split("=", 1)[1] for p in attributes
                     if p.startswith("samesite=")),
                    "Not specified"
                ))

            print("\nNote: This checks response cookies only.")

    except urllib.error.HTTPError as error:
        print("\nHTTP status:", error.code)
        print("The server returned an HTTP error.")
        error.close()

    except (urllib.error.URLError, TimeoutError, ValueError) as error:
        print("\nRequest failed:", error)

if __name__ == "__main__":
    main()
