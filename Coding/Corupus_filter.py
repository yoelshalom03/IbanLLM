import re
import nltk
from nltk.corpus import words

# Download words if not already done
# nltk.download('words')

INPUT_FILE = "iban_lyrics_corpus.txt"
OUTPUT_FILE = "iban_cleaned.txt"

english_words = set(w.lower() for w in words.words())

guitar_chords = {"a", "b", "c", "d", "e", "f", "g", "am", "bm", "cm", "dm", "em", "fm", "gm", "a#", "c#", "d#", "f#", "g#"}

def is_english_line(line):
    tokens = re.findall(r"\b\w+\b", line.lower())
    if not tokens:
        return False
    english_count = sum(1 for token in tokens if token in english_words)
    ratio = english_count / len(tokens)
    return ratio >= 0.9

def is_guitar_chord_line(line):
    tokens = re.findall(r"[A-Ga-g][#b]?m?", line)
    if len(tokens) >= 3 and all(t.lower() in guitar_chords for t in tokens):
        return True
    return False

def is_numbered_list(line):
    return bool(re.match(r"^\s*[\d]+\s*[\.\)]", line.strip()))

def is_symbol_junk(line):
    # Remove lines that are just symbols or special formatting
    line = line.strip()
    if re.fullmatch(r"[-=~_*#]+", line):
        return True
    if len(line) < 5:
        return False
    # Kill lines starting with hashtags or intro tags
    return line.startswith("#") or "[intro" in line.lower() or "[chorus" in line.lower()

def is_junk(line):
    line = line.strip()

    if len(line) < 5:
        return True
    if "http" in line or "www." in line:
        return True
    if is_english_line(line):
        return True
    if is_guitar_chord_line(line):
        return True
    if is_numbered_list(line):
        return True
    if is_symbol_junk(line):
        return True

    junk_phrases = [
        "please support", "semoga", "sumber", "support us", "share this",
        "all rights reserved", "download", "lyrics provided", "album",
        "tracklist", "komposer", "penyanyi", "artist", "label", "official",
        "produced by", "year:", "title:", "lagu ini", "lagu ni",
        "intro", "outro", "ending", "chord gitar", "guitar chord","lirik","more on","read more",
        "credit goes","repeat","more on","welcome"
    ]

    for phrase in junk_phrases:
        if phrase in line.lower():
            return True

    if re.match(r"^(title|track|album|year|by|komposer|produced|genre)\s*:", line.lower()):
        return True

    return False

def clean_corpus():
    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        lines = f.readlines()

    cleaned = []
    for line in lines:
        if not is_junk(line):
            cleaned.append(line.strip())

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(cleaned))

    print(f"✅ Cleaned corpus saved to: {OUTPUT_FILE}")
    print(f"📉 Original lines: {len(lines)} → Cleaned lines: {len(cleaned)}")

clean_corpus()

