import requests
from bs4 import BeautifulSoup
import re
import os

banner = r"""
     █████╗      █████╗
    ██╔══██╗    ██╔══██╗
    ███████║    ███████║   CCTV IP VIEWER
    ██╔══██║    ██╔══██║     Made in MD Abdullah
    ██║  ██║    ██║  ██║
    ╚═╝  ╚═╝    ╚═╝  ╚═╝
"""

dorks = [
    'inurl:"/view.shtml"',
    'intitle:"Live View / - AXIS"',
    'inurl:/mjpg/video.mjpg',
    'intitle:"IP Camera "'
]

headers = {
    "User-Agent": "Mozilla/5.0"
}

def search_dork(dork):
    print(f"\nSearching: {dork}")
    url = f"https://www.bing.com/search?q={dork}"
    try:
        r = requests.get(url, headers=headers)
        soup = BeautifulSoup(r.text, 'html.parser')
        links = soup.find_all('a', href=True)
        found = []
        for link in links:
            href = link['href']
            if re.match(r'https?://', href):
                found.append(href)
        return found
    except Exception as e:
        print(f"Error: {e}")
        return []

def main():
    os.system("clear")
    print(banner)
    print("\n\033[1;32mCollecting Live Camera IPs...\033[0m")
    print("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
    print("┃ Dork                       ┃ Found IP/Domain              ┃")
    print("┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩")
    for dork in dorks:
        results = search_dork(dork)
        if results:
            for link in results[:3]:  # Top 3 results
                domain = re.findall(r"https?://([^/]+)", link)
                domain = domain[0] if domain else "N/A"
                print(f"│ {dork.ljust(26)} │ {domain.ljust(28)} │")
        else:
            print(f"│ {dork.ljust(26)} │ No results                  │")
    print("└────────────────────────────┴──────────────────────────────┘")

if __name__ == "__main__":
    main()
