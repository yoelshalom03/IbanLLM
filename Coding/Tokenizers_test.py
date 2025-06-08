from transformers import LlamaTokenizer

# Load your SentencePiece tokenizer
tokenizer = LlamaTokenizer(vocab_file="iban_sp.model")

# Test encoding
text = "ngintu pengawa"
output = tokenizer(text)

print("Input IDs:", output["input_ids"])
print("Tokens:", tokenizer.convert_ids_to_tokens(output["input_ids"]))



