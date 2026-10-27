from pathlib import Path
import subprocess
import sys

BASE_DIR = Path(__file__).resolve().parent

TOOLS = {
    "1": ("Network Information", "network_info.py",
          "View basic network information"),
    "2": ("Port Checker", "port_checker.py",
          "Check a specified host and port"),
    "3": ("Password Strength Checker", "password_checker.py",
          "Evaluate password strength"),
    "4": ("Website Header Checker", "website_checker.py",
          "Inspect website response headers"),
    "5": ("Password Generator", "password_generator.py",
          "Generate a random password"),
    "6": ("Network Scanner", "network_scanner.py",
          "Inspect a network you are authorized to test"),
    "7": ("DNS Lookup", "dns_lookup.py",
          "Look up domain name information"),
    "8": ("Security Reports", "report_tool.py",
          "Create or view security reports"),
    "9": ("Website Status Checker", "status_checker.py",
          "Check whether a website responds"),
    "10": ("Website Response-Time Checker", "response_time.py",
           "Measure website response time"),
    "11": ("SSL Certificate Checker", "ssl_checker.py",
           "Inspect a website certificate"),
    "12": ("Website Redirect Checker", "redirect_checker.py",
           "Inspect website redirects"),
    "13": ("Security Audit Logger", "audit_logger.py",
           "Record security audit events"),
    "14": ("File Integrity Checker", "integrity_checker.py",
           "Check whether a file has changed"),
    "15": ("Hash Comparison Checker", "hash_compare.py",
           "Compare file hashes"),
    "16": ("File Hash Generator", "file_hash.py",
           "Generate a file hash"),
    "17": ("Custom Password Generator", "custom_password.py",
           "Generate a password using your settings"),
    "18": ("Password Generator + Auto-Copy", "password_copy.py",
           "Generate and copy a password"),
    "19": ("Website Uptime History", "uptime_history.py",
           "Record website availability checks"),
    "20": ("Website History Viewer", "history_viewer.py",
           "View saved website check history"),
    "21": ("IP & DNS Intelligence", "ip_dns_tool.py",
           "Look up IP addresses and DNS information"),
    "22": ("Website Link Status Checker", "link_status_checker.py",
           "Check the response status of a public URL"),
    "23": ("Wi-Fi Network Analyzer", "wifi_analyzer.py",
           "Inspect local network and connectivity details"),
    "24": ("File Security Scanner", "file_security_scanner.py",
           "Generate and compare SHA-256 file hashes"),
"25": ("Malware Indicator Checker", "malware_checker.py",
       "Compare file hashes against local indicators"),
"26": ("Security Header Checker", "security_headers.py",
       "Check website HTTP security headers"),
"27": ("Website Technology Detector", "tech_detector.py",
       "Inspect public technology clues in HTTP headers"),
"28": ("Website Availability Monitor", "availability_monitor.py",
       "Check website response status and response time"),
"29": ("HTTP Header Viewer", "header_viewer.py",
       "View publicly exposed HTTP response headers"),
"30": ("Content-Type Checker", "content_type_checker.py",
       "Inspect a website's declared content type"),
"31": ("Cookie Inspector", "cookie_inspector.py",
       "Inspect public cookie security attributes"),
"32": ("Compression Checker", "compression_checker.py",
       "Inspect website response compression headers"),
"33": ("HTTP Methods Checker", "http_methods_checker.py",
       "Inspect methods advertised by a website"),
"34": ("TLS Certificate Checker", "tls_checker.py",
       "Inspect HTTPS certificate and TLS details"),
"35": ("DNS Security Checker", "dns_security_checker.py",
       "Inspect basic DNS security records"),
"36": ("Robots.txt Checker", "robots_checker.py",
       "Inspect public website crawler rules"),
"37": ("Sitemap Checker", "sitemap_checker.py",
       "Check for a public XML sitemap"),
"38": ("Security.txt Checker", "security_txt_checker.py",
       "Check public vulnerability-reporting information"),
"39": ("Website Link Checker", "link_checker.py",
       "List links found on a public webpage"),
"40": ("Metadata Inspector", "metadata_inspector.py",
       "Inspect public webpage metadata"),
}


def show_header():
    print("\n" + "=" * 54)
    print("             GLORIOUS TECHFORGE")
    print("               SECURITY TOOLKIT")
    print("=" * 54)


def show_menu():
    ready = 0
    missing = []

    show_header()
    print("Choose a tool:\n")

    for number, (name, filename, description) in TOOLS.items():
        script = BASE_DIR / filename
        if script.is_file():
            status = "[READY]"
            ready += 1
        else:
            status = "[MISSING]"
            missing.append((number, filename))

        print(f"{number:>2}. {name} {status}")
        print(f"    {description}")

    print("\n" + "-" * 54)
    print(f"Scripts ready: {ready}/{len(TOOLS)}")
    print("Type a tool number to launch it.")
    print("Type C to check all tool files.")
    print("Type 0 to exit.")
    return missing


def check_files():
    print("\n--- TOOL FILE CHECK ---")
    for number, (name, filename, _) in TOOLS.items():
        script = BASE_DIR / filename
        status = "OK" if script.is_file() else "MISSING"
        print(f"{number:>2}. {status:<7} {filename}")
    print("\nCheck complete.")


def launch_tool(number):
    name, filename, _ = TOOLS[number]
    script = BASE_DIR / filename

    if not script.is_file():
        print(f"\nERROR: {filename} was not found.")
        print(f"Expected location: {script}")
        print("Check the filename or restore the missing script.")
        return

    print(f"\nLaunching {name}...\n")
    try:
        result = subprocess.run(
            [sys.executable, str(script)],
            cwd=str(BASE_DIR),
            check=False
        )
        if result.returncode == 0:
            print(f"\n{name} closed normally.")
        else:
            print(f"\nWARNING: {name} exited with code "
                  f"{result.returncode}.")
            print("Review the error above before trying again.")
    except KeyboardInterrupt:
        print(f"\n{name} was interrupted by the user.")
    except OSError as error:
        print(f"\nCould not launch {name}: {error}")


def main():
    while True:
        missing = show_menu()
        choice = input("\nChoose a tool: ").strip().lower()

        if choice == "0":
            print("\nStay curious. Stay ethical. Goodbye!")
            break

        if choice == "c":
            check_files()
            input("\nPress Enter to return to the menu...")
            continue

        if choice not in TOOLS:
            print("\nInvalid choice. Enter a listed number, C, or 0.")
            input("Press Enter to try again...")
            continue

        launch_tool(choice)
        input("\nPress Enter to return to the main menu...")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nGLORIOUS TECHFORGE closed. Stay curious. Stay ethical.")
    except Exception as error:
        print(f"\nUnexpected menu error: {error}")
        print("Your backup is glorious.py.backup")
