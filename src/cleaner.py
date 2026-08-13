class DatasetCleaner:

    def __init__(self):
        self.bad_phrases = [
            "(file attached)",
            "<Media omitted>",
            "image omitted",
            "video omitted",
            "audio omitted",
            "GIF omitted",
            "sticker omitted",
            "document omitted",
            "vcf",
            "Missed voice call",
            "Missed video call",
            "deleted this message"
        ]

    def is_valid(self, text):

        text = text.lower()

        for phrase in self.bad_phrases:
            if phrase.lower() in text:
                return False

        return True