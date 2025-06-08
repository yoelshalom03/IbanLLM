# Load your corpus file
with open("iban_text.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

# Strip whitespace and remove empty lines
cleaned_lines = [line.strip() for line in lines if line.strip()]

# Save to a new file or overwrite original
with open("iban_text_noblank.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(cleaned_lines))

print(f" Cleaned corpus saved as iban_text_noblank with {len(cleaned_lines)} lines.")
