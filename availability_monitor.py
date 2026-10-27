
import time
import urllib.request
import urllib.error

def main():
    print("\n" + "=" * 42)
    print("      GLORIOUS TECHFORGE")
    print("      WEBSITE AVAILABILITY MONITOR")
    print("=" * 42)

    url = input("Enter website URL: ").strip()

    if not url.startswith(("https://", "http://")):
        url = "https://" + url

    request = urllib.request.Request(
        url,
        headers={"User-Agent": "GloriousTechforge-Monitor/1.0"},
        method="GET"
    )

    start = time.perf_counter()

    try:
        with urllib.request.urlopen(request, timeout=15) as response:
            elapsed = (time.perf_counter() - start) * 1000
            print("\nWebsite:", response.url)
            print("Status:", response.status)
            print("Availability: RESPONDING")
            print(f"Response time: {elapsed:.2f} ms")

    except urllib.error.HTTPError as error:
        elapsed = (time.perf_counter() - start) * 1000
        print("\nHTTP status:", error.code)
        print("Availability: SERVER RESPONDED WITH AN HTTP ERROR")
        print(f"Response time: {elapsed:.2f} ms")
        error.close()

    except (urllib.error.URLError, TimeoutError, ValueError) as error:
        elapsed = (time.perf_counter() - start) * 1000
        print("\nAvailability: COULD NOT CONFIRM")
        print("Reason:", error)
        print(f"Elapsed time: {elapsed:.2f} ms")

if __name__ == "__main__":
    main()
