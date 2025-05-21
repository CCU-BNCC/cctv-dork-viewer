import requests
from bs4 import BeautifulSoup
import urllib.parse

def print_banner():
    banner = """
     █████╗      █████╗
    ██╔══██╗    ██╔══██╗
    ███████║    ███████║  CCTV DORK VIEWER
    ██╔══██║    ██╔══██║     Made in Abdullah
    ██║  ██║    ██║  ██║
    ╚═╝  ╚═╝    ╚═╝  ╚═╝
    """
    print(banner)

# এখানে ডোরক গুলো বসাও
dorks = [
    'inurl:"/view.shtml"',
    'intitle:"Live View / - AXIS"',
    'inurl:/mjpg/video.mjpg',
    'intitle:"IP Camera "'
]

def google_search(dork):
    # Google সার্চ URL তৈরি
    query = urllib.parse.quote(dork)
    url = f"https://www.google.com/search?q={query}&num=10"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
    }
    try:
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code == 200:
            return response.text
        else:
            print(f"Error: Received status code {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return None

def parse_google_results(html):
    soup = BeautifulSoup(html, 'html.parser')
    results = []
    # Google সার্চ রেজাল্টের লিংকগুলো খোঁজা
    for g in soup.find_all('div', class_='tF2Cxc'):
        a_tag = g.find('a')
        if a_tag and a_tag['href']:
            results.append(a_tag['href'])
    return results

def main():
    print_banner()

    for dork in dorks:
        print(f"Searching: {dork}\n")
        html = google_search(dork)
        if not html:
            print("Failed to get results.\n")
            continue

        links = parse_google_results(html)
        if links:
            print("Found CCTV Links:")
            print("-" * 50)
            for link in links:
                print(link)
            print("-" * 50)
        else:
            print("No links found for this dork.")
        print("\n")

if __name__ == "__main__":
    main()
