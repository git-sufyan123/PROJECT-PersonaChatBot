import json
from config import TrainingConfig


def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


from transformers import AutoTokenizer


class QwenFormatter:

    def __init__(self, model_name):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)


    def format_pair(self, pair):
        messages = [
            {
                "role": "system",
                "content":
                    "You are Muhammad Abu Sufyan. "
                    "Reply exactly like him. "
                    "Match his language, slang, texting style, emojis, "
                    "and personality. Never explain yourself."
            },
            {
                "role": "user",
                "content": pair["context"]
            },
            {
                "role": "assistant",
                "content": pair["response"]
            }
        ]

        return self.tokenizer.apply_chat_template(
            messages,
            tokenize=False,
            add_generation_prompt=False
        )
    def format_dataset(self, dataset):
            formatted = []
            for pair in dataset:
                formatted.append({"text": self.format_pair(pair)})
            return formatted

    def save_jsonl(self, dataset, output_path):
        formatted = self.format_dataset(dataset)
        with open(output_path, "w", encoding="utf-8") as f:
            for sample in formatted:
                json.dump(sample, f, ensure_ascii=False)
                f.write("\n")

        print(f"Saved {len(formatted)} formatted samples to {output_path}")


if __name__ == "__main__":

    cfg = TrainingConfig()

    formatter = QwenFormatter(cfg.model_name)

    train = load_json(cfg.train_file)
    valid = load_json(cfg.valid_file)
    test = load_json(cfg.test_file)

    formatter.save_jsonl(
        train,
        cfg.train_formatted
    )

    formatter.save_jsonl(
        valid,
        cfg.valid_formatted
    )

    formatter.save_jsonl(
        test,
        cfg.test_formatted
    )