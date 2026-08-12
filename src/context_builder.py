from src.models import ConversationPair
from src.cleaner import DatasetCleaner


class ContextBuilder:

    def __init__(self, window_size=3):
        self.window_size = window_size
        self.cleaner = DatasetCleaner()

    def _format_turn(self, turn):
        lines = []
        for message in turn.messages:
            lines.append(f"{turn.sender}: {message}")
        return "\n".join(lines)

    def build_pairs(self, conversations):

        pairs = []

        for conversation_id,conversation in enumerate(conversations):
            for index, turn in enumerate(conversation):
                if not turn.is_me:
                    continue
                start = max(0, index - self.window_size)
                context_turns = conversation[start:index]
                if len(context_turns) == 0:
                    continue
                formatted = [] 
                for t in context_turns:
                    if not self.cleaner.is_valid(self._format_turn(t)):
                        continue
                    formatted.append(self._format_turn(t))
                context_text = "\n\n".join(formatted)
                response_text = "\n".join(turn.messages)
                if not self.cleaner.is_valid(response_text):
                    continue
                if len(formatted) == 0:
                    continue    
                pair = ConversationPair(
                context=context_text,
                response=response_text,
                conversation_id=conversation_id)
                pairs.append(pair)

        return pairs