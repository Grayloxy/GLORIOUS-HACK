from pathlib import Path

HISTORY = Path(__file__).resolve().parent / "uptime_history.txt"


def main():
    print("\n=== GLORIOUS TECHFORGE ===")
    print("WEBSITE HISTORY VIEWER")
    print("=" * 36)

    if not HISTORY.exists():
        print("No history found yet.")
        print("Run Tool 19 first to record a website check.")
        return

    entries = HISTORY.read_text(encoding="utf-8").splitlines()

    if not entries:
        print("History is empty.")
        return

    print(f"Records saved: {len(entries)}")
    print("-" * 36)

    for entry in entries[-20:]:
        print(entry)

    print("-" * 36)
    print("Showing the latest 20 records.")


if __name__ == "__main__":
    main()

