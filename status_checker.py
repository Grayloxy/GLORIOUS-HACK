import urllib.request
import urllib.error

print("=" * 38)
print("GLORIOUS TECHFORGE")
print("WEBSITE STATUS CHECKER")
print("=" * 38)

url = input("Enter a website URL: ").strip()

if not url.startswith(("https://", "http://")):
    url = "https://" + url

try:
    request = urllib.request.Request(
        url,
        headers={"User-Agent": "GLORIOUS-TECHFORGE"}
    )
    with urllib.request.urlopen(request, timeout=10) as response:
        print("Website is reachable.")
        print("HTTP status:", response.status)

except urllib.error.HTTPError as error:
    print("Website responded with HTTP status:", error.code)
except Exception as error:
    print("Could not check website:", error)
