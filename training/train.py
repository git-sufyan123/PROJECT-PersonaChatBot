import torch

from datasets import load_dataset

from transformers import (
    AutoTokenizer,
    AutoModelForCausalLM,
    BitsAndBytesConfig,
    TrainingArguments
)

from peft import (
    LoraConfig,
    prepare_model_for_kbit_training,
    get_peft_model
)

from trl import SFTTrainer

from config import TrainingConfig

cfg = TrainingConfig()

train_dataset = load_dataset(
    "json",
    data_files=cfg.train_formatted,
    split="train"
)

valid_dataset = load_dataset(
    "json",
    data_files=cfg.valid_formatted,
    split="train"
)

print(train_dataset)
print(valid_dataset)

tokenizer = AutoTokenizer.from_pretrained(
    cfg.model_name,
    trust_remote_code=True
)

if tokenizer.pad_token is None:
    tokenizer.pad_token = tokenizer.eos_token

print("Tokenizer Loaded")
print(tokenizer.pad_token)