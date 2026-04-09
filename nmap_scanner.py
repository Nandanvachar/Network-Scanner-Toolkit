import subprocess

def nmap_scan(target):
    print("\nSelect Scan Type:")
    print("1. Host Discovery")
    print("2. Port Scan")
    print("3. Custom Port Scan")
    print("4. Service Detection")
    print("5. OS Detection")

    choice = input("Enter choice: ")

    if choice == "1":
        command = ["nmap", "-sn", target]
    elif choice == "2":
        command = ["nmap", target]
    elif choice == "3":
        ports = input("Enter ports (e.g., 80,443): ")
        command = ["nmap", "-p", ports, target]
    elif choice == "4":
        command = ["nmap", "-sV", target]
    elif choice == "5":
        command = ["nmap", "-O", target]
    else:
        print("Invalid choice")
        return

    try:
        result = subprocess.run(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            timeout=60
        )
        print("\nScan Results:\n")
        print(result.stdout)

    except subprocess.TimeoutExpired:
        print("[!] Scan timed out")
    except Exception as e:
        print(f"[ERROR] {e}")

if __name__ == "__main__":
    target = input("Enter IP/Hostname/Range: ")
    nmap_scan(target)
