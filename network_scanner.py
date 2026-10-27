
import socket
import subprocess

print("=" * 35)
print(" GLORIOUS TECHFORGE")
print(" Network Information Scanner")
print("=" * 35)

try:
    hostname = socket.gethostname()
    print("Device hostname:", hostname)

    result = subprocess.run(
        ["ip", "route"],
        capture_output=True,
        text=True,
        timeout=5
    )

    if result.stdout.strip():
        print("\nNetwork route information:")
        print(result.stdout)
    else:
        print("No route information available.")

except FileNotFoundError:
    print("The Android 'ip' utility is unavailable.")
except Exception as error:
    print("Error:", error)

print("\nSecurity learning: Step 6 complete!")
