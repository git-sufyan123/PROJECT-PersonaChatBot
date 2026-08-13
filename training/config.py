from dataclasses import dataclass


@dataclass
class TrainingConfig:

    # Base Model
    model_name = "Qwen/Qwen2.5-3B-Instruct"

    # Raw Dataset
    train_file = "data/splits/train.json"
    valid_file = "data/splits/valid.json"
    test_file = "data/splits/test.json"

    # Formatted Dataset
    train_formatted = "data/splits/train_formatted.jsonl"
    valid_formatted = "data/splits/valid_formatted.jsonl"
    test_formatted = "data/splits/test_formatted.jsonl"

    # Output
    output_dir = "checkpoints/personachat"

    # LoRA
    lora_rank = 16
    lora_alpha = 32
    lora_dropout = 0.05

    # Training
    epochs = 3
    learning_rate = 2e-4

    batch_size = 2
    gradient_accumulation = 8

    max_length = 1024

    seed = 42