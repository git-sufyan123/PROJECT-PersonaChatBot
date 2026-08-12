"""from src.models import ConversationTurn

class ConversationBuilder:
    def build_turns(self, messages):
        turns = []

        current_turn = None

        for message in messages:
            if current_turn is None:
                current_turn = ConversationTurn(
                sender=message.sender,
                is_me=message.is_me,
                start_time=message.timestamp,
                end_time=message.timestamp,
                messages=[message.text]
            )
                continue
            if message.sender == current_turn.sender:
                    current_turn.messages.append(message.text)
                    current_turn.end_time = message.timestamp
                    continue
            if message.sender == current_turn.sender:
                 current_turn.messages.append(message.text)
                 current_turn.end_time = message.timestamp
                 continue
            turns.append(current_turn)
            current_turn = ConversationTurn(
                 sender=message.sender,
                 is_me=message.is_me,
                 start_time=message.timestamp,
                 end_time=message.timestamp,
                 messages=[message.text]
                 )    
        return turns"""



from src.models import ConversationTurn


class ConversationBuilder:

    def build_turns(self, messages):

        turns = []

        current_turn = None

        for message in messages:

            if current_turn is None:
                current_turn = ConversationTurn(
                    sender=message.sender,
                    is_me=message.is_me,
                    start_time=message.timestamp,
                    end_time=message.timestamp,
                    messages=[message.text]
                )
                continue

            if message.sender == current_turn.sender:
                current_turn.messages.append(message.text)
                current_turn.end_time = message.timestamp
                continue

            turns.append(current_turn)

            current_turn = ConversationTurn(
                sender=message.sender,
                is_me=message.is_me,
                start_time=message.timestamp,
                end_time=message.timestamp,
                messages=[message.text]
            )

        if current_turn is not None:
            turns.append(current_turn)

        return turns