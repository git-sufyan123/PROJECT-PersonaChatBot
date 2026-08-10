
class ConversationSegmenter:

    def __init__(self, max_gap_minutes=60):
        self.max_gap_minutes = max_gap_minutes

    def segment(self, turns):
        conversations = []

        current_conversation = []

        for turn in turns:
            if len(current_conversation) == 0:
                current_conversation.append(turn)
                continue
            previous_turn = current_conversation[-1]
            gap = turn.start_time - previous_turn.end_time
            if gap.total_seconds() <= self.max_gap_minutes * 60:
                current_conversation.append(turn)
            else:
                conversations.append(current_conversation)
                current_conversation = [turn]
        if len(current_conversation) > 0:
            conversations.append(current_conversation)
        return conversations