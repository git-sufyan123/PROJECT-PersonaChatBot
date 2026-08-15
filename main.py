
from src.dataset_builder import ConversationBuilder
from src.context_builder import ContextBuilder
from src.segmenter import ConversationSegmenter
from src.exporter import DatasetExporter
from src.parser import WhatsAppParser
from src.splitter import DatasetSplitter


def main():

    print("Main Started")

    parser = WhatsAppParser(
        my_name="Muhammad Abu Sufyan"
    )

    print("Parser Created")

    messages = parser.parse_folder("data/raw")


    builder = ConversationBuilder()
    turns = builder.build_turns(messages)

    segmenter = ConversationSegmenter()
    conversations = segmenter.segment(turns)
    print(f"Total Conversations: {len(conversations)}")
    print("\nFirst Conversation Size:")
    print(len(conversations[0]))
    print("\nLast Conversation Size:")
    print(len(conversations[-1]))

    context_builder = ContextBuilder(window_size=3)
    pairs = context_builder.build_pairs(conversations)

    splitter = DatasetSplitter()
    train_pairs, valid_pairs, test_pairs = splitter.split(pairs)
    exporter = DatasetExporter()
    exporter.export_json(
    train_pairs,
    "data/splits/train.json")

    exporter.export_json(
    valid_pairs,
    "data/splits/valid.json")
    exporter.export_json(
    test_pairs,
    "data/splits/test.json")
    
    print()
    print(
    f"Total Pairs Check: "f"{len(train_pairs)+len(valid_pairs)+len(test_pairs)}")

    exporter = DatasetExporter()
    exporter.export_json(pairs,"data/processed/dataset.json")

    print(f"Turns: {len(turns)}")
    print(f"Pairs: {len(pairs)}")
    print("\n========== FIRST PAIR ==========\n")
    print(pairs[0].context)
    print("\n----------- RESPONSE -----------\n")
    print(pairs[0].response)
    print(f"\nTotal Parsed Messages: {len(messages)}")
    print("\nFirst Message:")
    print(messages[0])
    print("\nLast Message:")
    print(messages[-1])

    

    
    print("Finished")
    


if __name__ == "__main__":
    main()