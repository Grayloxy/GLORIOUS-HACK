
from datetime import datetime
from pathlib import Path

REPORT_DIR = Path.home() / "GLORIOUS-HACK" / "reports"
REPORT_DIR.mkdir(parents=True, exist_ok=True)

print("=" * 38)
print("      GLORIOUS TECHFORGE")
print("       SECURITY REPORTS")
print("=" * 38)

print("1. Record a security learning note")
print("2. View saved reports")

choice = input("\nChoose an option: ").strip()

if choice == "1":
    title = input("Report title: ").strip()
    note = input("What did you test or learn? ").strip()

    if not title or not note:
        print("Title and note cannot be empty.")
    else:
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = REPORT_DIR / f"report_{timestamp}.txt"

        content = (
            "GLORIOUS TECHFORGE - SECURITY REPORT\n"
            f"Date: {datetime.now().isoformat(timespec='seconds')}\n"
            f"Title: {title}\n"
            f"Notes: {note}\n"
            "Scope: Educational or authorised testing only\n"
        )

        filename.write_text(content, encoding="utf-8")
        print("\nReport saved to:")
        print(filename)

elif choice == "2":
    reports = sorted(REPORT_DIR.glob("*.txt"))

    if not reports:
        print("No reports saved yet.")
    else:
        for report in reports:
            print(f"\n--- {report.name} ---")
            print(report.read_text(encoding="utf-8"))

else:
    print("Invalid option.")

print("\nGLORIOUS TECHFORGE | Step 14")
