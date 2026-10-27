import time
import urllib.request

print("=" * 38)
print("GLORIOUS TECHFORGE")
print("WEBSITE RESPONSE-TIME CHECKER")
print("=" * 38)

url = input("Enter website URL: ").strip()

if not url.startswith(("https://", "http://")):
    url = "https://" + url

try:
    request = urllib.request.Request(
        url,
        headers={"User-Agent": "GLORIOUS-TECHFORGE"}
    )

    start = time.perf_counter()

    with urllib.request.urlopen(request, timeout=15) as response:
        elapsed = (time.perf_counter() - start) * 1000
        print("HTTP status:", response.status)
        print(f"Response time: {elapsed:.2f} ms")

except Exception as error:
    print("Check failed:", error)
