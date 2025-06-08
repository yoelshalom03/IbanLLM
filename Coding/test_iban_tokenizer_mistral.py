from transformers import AutoModelForCausalLM, LlamaTokenizer
import torch

# 1. Load your custom tokenizer
tokenizer = LlamaTokenizer.from_pretrained("hf_iban_tokenizer_sp")

# 2. Load base Mistral 7B model (this downloads the model from Hugging Face)
model = AutoModelForCausalLM.from_pretrained(
    "mistralai/Mistral-7B-v0.1",
    torch_dtype=torch.float16,
    device_map="auto"
)

# 3. Resize model embeddings to fit your tokenizer
model.resize_token_embeddings(len(tokenizer))

# 4. Test input (in Iban)
prompt = "ngintu pengawa ti meri kitai semengat"

# 5. Encode, generate, decode
inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
with torch.no_grad():
    outputs = model.generate(**inputs, max_new_tokens=50)

print("\n Model output:")
print(tokenizer.decode(outputs[0], skip_special_tokens=True))
