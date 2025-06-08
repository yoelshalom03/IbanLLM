import requests
from bs4 import BeautifulSoup
import time

# Base URL of the Ibanpedia website
BASE_URL = "https://ibanpedia.wordpress.com/"

# Headers to mimic a browser visit
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

def get_article_links():
    """
    Fetches all article links from the Ibanpedia homepage.
    """
    response = requests.get(BASE_URL, headers=HEADERS)
    soup = BeautifulSoup(response.content, "html.parser")
    links = []

    # Find all article links
    for a_tag in soup.find_all("a", href=True):
        href = a_tag['href']
        if href.startswith(BASE_URL) and href != BASE_URL:
            links.append(href)

    return list(set(links))  # Remove duplicates

def extract_iban_text(url):
    """
    Extracts the main content text from a given article URL.
    """
    response = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(response.content, "html.parser")

    # Assuming the main content is within <div class="entry-content">
    content_div = soup.find("div", class_="entry-content")
    if content_div:
        paragraphs = content_div.find_all("p")
        text = "\n".join([para.get_text(strip=True) for para in paragraphs])
        return text
    return ""

def main():
    article_links = get_article_links()
    print(f"Found {len(article_links)} articles.")

    with open("iban_corpus_blog.txt", "w", encoding="utf-8") as file:
        for idx, link in enumerate(article_links, 1):
            print(f"Processing ({idx}/{len(article_links)}): {link}")
            text = extract_iban_text(link)
            if text:
                file.write(text + "\n\n")
            time.sleep(1)  # Be polite and avoid overwhelming the server

    print("Scraping completed. The Iban corpus has been saved to 'iban_corpus_blog.txt'.")

if __name__ == "__main__":
    main()
