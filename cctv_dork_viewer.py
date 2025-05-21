import requests
from bs4 import BeautifulSoup
from rich.console import Console
from rich.table import Table
from termcolor import cprint

console = Console()

def show_banner():
    cprint("""
     █████╗      █████╗ 
    ██╔══██╗    ██╔══██╗
    ███████║    ███████║  CCTV DORK VIEWER
    ██╔══██║    ██╔══██║     Made in Abdullah
    ██║  ██║    ██║  ██║
    ╚═╝  ╚═╝    ╚═╝  ╚═╝
    """, "red")

dorks = [
    'inurl:"/view.shtml"',
    'intitle:"Live View / - AXIS"',
    'inurl:/mjpg/video.mjpg',
    'intitle:"IP Camera [root]"'
]

def search_dork(dork, max_results=5):
    url = f"https://www.google.com/search?q={dork}"
    headers = {"User-Agent": "Mozilla/5.0"}
    try:
        res = requests.get(url, headers=headers)
        soup = BeautifulSoup(res.text, "html.parser")
        links = []
        for g in soup.find_all('a'):
            href = g.get('href')
            if href and "http" in href and "google" not in href:
                links.append(href)
                if len(links) >= max_results:
                    break
        return links
    except Exception as e:
        console.print(f"[red]Error:[/red] {e}")
        return []

def main():
    show_banner()
    table = Table(title="CCTV Links Found", show_lines=True)
    table.add_column("Dork")
    table.add_column("Found Link")
    for dork in dorks:
        console.print(f"[green]Searching:[/green] {dork}")
        results = search_dork(dork)
        for link in results:
            table.add_row(dork, link)
    console.print(table)

if __name__ == "__main__":
    main()
