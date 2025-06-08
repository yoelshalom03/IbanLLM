import nltk
from nltk.corpus import words
import re

nltk.download('words')
english_vocab = set(words.words())

def is_mostly_english(text_block, threshold=0.8):
    tokens = re.findall(r'\b\w+\b', text_block.lower())
    if not tokens:
        return False
    english_count = sum(1 for word in tokens if word in english_vocab)
    return (english_count / len(tokens)) > threshold

with open("iban_corpus_blog.txt", "r", encoding="utf-8") as f:
    content = f.read()

# Split articles by double newline
articles = content.split("\n\n")
clean_articles = []

for article in articles:
    if not is_mostly_english(article):  # Keep only if NOT mostly English
        clean_articles.append(article.strip())

with open("iban_corpus_blog_clean.txt", "w", encoding="utf-8") as f:
    f.write("\n\n".join(clean_articles))



