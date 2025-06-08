import re

with open("iban_text_noblank.txt", "r", encoding="utf-8") as f:
    text = f.read()

# Split at end of sentence punctuation followed by whitespace
sentences = re.split(r'(?<=[.!?])\s+', text)

# Clean each sentence and remove empties
cleaned = [s.strip() for s in sentences if s.strip()]

# Save to new file
with open("iban_text_split_sentences.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(cleaned))

print(f"✅ Split and saved {len(cleaned)} sentences to iban_text_split_sentences.txt")
