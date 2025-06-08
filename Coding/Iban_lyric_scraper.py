import requests
from bs4 import BeautifulSoup
import time

BASE_URL = "https://liriklagu-iban-sarawak.blogspot.com"
LISTING_URL = BASE_URL + "/p/sitemap.html"
OUTPUT_FILE = "iban_lyrics_corpus.txt"



def get_all_song_links_from_archive(start_url):
    song_links = set()
    next_page = start_url

    while next_page:
        print(f"🔍 Visiting: {next_page}")
        res = requests.get(next_page)
        soup = BeautifulSoup(res.text, "html.parser")
        links = soup.find_all("a", href=True)

        for link in links:
            href = link["href"]
            if (
                href.startswith("http") and 
                "liriklagu-iban-sarawak.blogspot.com" in href and
                "/search?" not in href and  # skip pagination links
                "#" not in href and
                href not in song_links
            ):
                song_links.add(href)

        # Find "Older Posts" button
        next_btn = soup.find("a", string=lambda s: s and ("Older Posts" in s or "Next" in s))
        next_page = next_btn["href"] if next_btn else None
        time.sleep(1)

    print(f"✅ Total unique posts found: {len(song_links)}")
    return list(song_links)


def scrape_lyrics(url):
    try:
        res = requests.get(url, timeout=10)
        soup = BeautifulSoup(res.text, "html.parser")
        container = soup.find("div", class_="post-body entry-content")
        if not container:
            return []

        # Grab all text, keep line breaks where possible
        raw_text = container.get_text(separator="\n").strip()
        lines = raw_text.split("\n")

        clean_lines = []
        for line in lines:
            line = line.strip()

            # Filter logic
            if len(line) < 6:
                continue
            if any(kw in line.lower() for kw in ["lirik lagu", "judul", "artist", "download", "sumber"]):
                continue
            if line.endswith(":"):
                continue
            if line.count(" ") < 1:  # likely a single word or label
                continue

            clean_lines.append(line)

        # If majority of page is junk, skip it
        if len(clean_lines) < 4:
            return []

        return clean_lines

    except Exception as e:
        print(f"❌ Error scraping {url}: {e}")
        return []



def main():
    all_links = get_all_song_links_from_archive("https://liriklagu-iban-sarawak.blogspot.com/")
    total_lines = []

    for url in all_links:
        print(f"🎵 Scraping {url}")
        lyrics = scrape_lyrics(url)
        total_lines.extend(lyrics)
        time.sleep(1)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(total_lines))

    print(f"\n🎉 DONE: Collected {len(total_lines)} clean Iban lines into {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
