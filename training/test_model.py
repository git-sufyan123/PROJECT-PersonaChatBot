from transformers import AutoTokenizer

MODEL = "Qwen/Qwen2.5-3B-Instruct"

tokenizer = AutoTokenizer.from_pretrained(MODEL)

print("Tokenizer Loaded Successfully!")
print(tokenizer.vocab_size)