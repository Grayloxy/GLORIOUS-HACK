import urllib.request
import urllib.error

print("=" * 38)
print("GLORIOUS TECHFORGE")
print("WEBSITE REDIRECT CHECKER")
print("=" * 38)

url = input("Enter website URL: ").strip()

if not url.startswith(("https://", "http://")):
    url = "https://" + url

try:
    request = urllib.request.Request(
        url,
        headers={"User-Agent": "GLORIOUS-TECHFORGE"}
    )

    opener = urllib.request.build_opener()
    response = opener.open(request, timeout=15)

    print("Final URL:", response.geturl())
    print("HTTP status:", response.status)

    if response.geturl() != url:
        print("The website redirected to another URL.")
    else:
        print("No URL change detected.")

    response.close()

except Exception as error:
    print("Check failed:", error)
