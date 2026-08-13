import random
from collections import defaultdict


class DatasetSplitter:

    def __init__(self,
                 train_ratio=0.8,
                 valid_ratio=0.1,
                 seed=42):

        self.train_ratio = train_ratio
        self.valid_ratio = valid_ratio
        self.seed = seed

    def split(self, pairs):

        # Group all pairs by conversation
        grouped = defaultdict(list)

        for pair in pairs:
            grouped[pair.conversation_id].append(pair)

        # List of conversation IDs
        conversation_ids = list(grouped.keys())

        # Shuffle conversations (not pairs)
        random.seed(self.seed)
        random.shuffle(conversation_ids)

        total = len(conversation_ids)

        train_end = int(total * self.train_ratio)
        valid_end = train_end + int(total * self.valid_ratio)

        train_ids = conversation_ids[:train_end]
        valid_ids = conversation_ids[train_end:valid_end]
        test_ids = conversation_ids[valid_end:]

        train = []
        valid = []
        test = []

        for cid in train_ids:
            train.extend(grouped[cid])

        for cid in valid_ids:
            valid.extend(grouped[cid])

        for cid in test_ids:
            test.extend(grouped[cid])

        print("\n========== DATASET SUMMARY ==========")
        print(f"Train Conversations : {len(train_ids)}")
        print(f"Validation Conversations : {len(valid_ids)}")
        print(f"Test Conversations : {len(test_ids)}")
        print()
        print(f"Train Pairs : {len(train)}")
        print(f"Validation Pairs : {len(valid)}")
        print(f"Test Pairs : {len(test)}")

        return train, valid, test