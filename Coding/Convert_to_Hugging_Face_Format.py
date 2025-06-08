from transformers import LlamaTokenizer
import os

# 1. Load your trained SentencePiece tokenizer
tokenizer = LlamaTokenizer(vocab_file="iban_sp.model")

# 2. Set special tokens (match what you defined during training)
tokenizer.pad_token = "<pad>"
tokenizer.unk_token = "<unk>"
tokenizer.bos_token = "<s>"
tokenizer.eos_token = "</s>"

# 3. Choose a folder to save in
save_path = "hf_iban_tokenizer_sp"
os.makedirs(save_path, exist_ok=True)

# 4. Save it Hugging Face–style
tokenizer.save_pretrained(save_path)

print(f"Tokenizer saved to: {save_path}")

