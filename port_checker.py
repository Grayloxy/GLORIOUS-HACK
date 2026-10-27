import socket

print("=" * 35)
print(" GLORIOUS TECHFORGE")
print(" Basic Port Checker")
print("=" * 35)

host = input("Enter test host (localhost): ").strip()
if not host:
    host = "localhost"

ports = [22, 53, 80, 443, 8080]

for port in ports:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    result = sock.connect_ex((host, port))

    if result == 0:
        print(f"Port {port}: OPEN")
    else:
        print(f"Port {port}: Closed or filtered")

    sock.close()

print("Security learning: Step 2 complete!")
