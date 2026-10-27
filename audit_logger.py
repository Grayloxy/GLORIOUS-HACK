from datetime import datetime
from pathlib import Path

folder = Path.home() / "GLORIOUS-HACK" / "reports"
folder.mkdir(parents=True, exist_ok=True)

log_file = folder / "audit_log.txt"

print("=" * 38)
print("GLORIOUS TECHFORGE")
print("SECURITY AUDIT LOGGER")
print("=" * 38)

activity = input("What security check did you perform? ").strip()

if activity:
    timestamp = datetime.now().astimezone().strftime("%Y-%m-%d %H:%M:%S %Z")

    with log_file.open("a", encoding="utf-8") as file:
        file.write(f"[{timestamp}] {activity}\n")

    print("Activity recorded successfully.")
    print("Log location:", log_file)
else:
    print("No activity entered. Nothing recorded.")
