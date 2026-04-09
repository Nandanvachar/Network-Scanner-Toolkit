import subprocess
import platform
import time

def ping_host(host):
    param = "-n" if platform.system().lower() == "windows" else "-c"
    
    try:
        start = time.time()
        result = subprocess.run(
            ["ping", param, "1", host],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            timeout=5
        )
        end = time.time()

        if result.returncode == 0:
            print(f"[+] {host} is UP (Response time: {round((end-start)*1000, 2)} ms)")
        else:
            print(f"[-] {host} is DOWN")

    except subprocess.TimeoutExpired:
        print(f"[!] {host} timed out")

if __name__ == "__main__":
    target = input("Enter IP/Hostname: ")
    ping_host(target)
