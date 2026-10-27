
from pathlib import Path
from datetime import datetime
import urllib.request
import urllib.error
import time

HISTORY = Path(__file__).resolve().parent / "uptime_history.txt"


def main():
    print("\n=== GLORIOUS TECHFORGE ===")
    print("WEBSITE UPTIME HISTORY")
    url = input("Enter website URL (or H to view history): ").strip()

    if url.lower() == "h":
        if HISTORY.exists():
            print(HISTORY.read_text(encoding="utf-8"))
        else:
            print("No history saved yet.")
        return

    if not url.startswith(("https://", "http://")):
        url = "https://" + url

    started = time.time()
    try:
        request = urllib.request.Request(
            url, headers={"User-Agent": "GloriousTechforge/1.0"}
        )
        with urllib.request.urlopen(request, timeout=10) as response:
            status = response.status
        elapsed = round((time.time() - started) * 1000)

        result = f"UP | HTTP {status} | {elapsed} ms"
    except (urllib.error.URLError, TimeoutError, ValueError) as error:
        elapsed = round((time.time() - started) * 1000)
        result = f"FAILED | {elapsed} ms | {error}"

    entry = f"{datetime.now().isoformat(timespec='seconds')} | {url} | {result}\n"
    with HISTORY.open("a", encoding="utf-8") as file:
        file.write(entry)

    print("\nResult:", result)
    print("Saved to:", HISTORY.name)


if __name__ == "__main__":
    main()
