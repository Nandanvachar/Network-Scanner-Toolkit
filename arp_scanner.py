import subprocess
import platform

def arp_scan():
    try:
        command = "arp -a" if platform.system().lower() == "windows" else "arp -n"
        
        result = subprocess.run(
            command,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        print("\nIP Address\t\tMAC Address")
        print("-" * 40)
        
        print(result.stdout)

    except Exception as e:
        print(f"[ERROR] {e}")

if __name__ == "__main__":
    arp_scan()
