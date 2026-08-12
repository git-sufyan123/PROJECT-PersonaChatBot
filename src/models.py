from dataclasses import dataclass
from datetime import datetime


@dataclass
class RawMessage:
    """
    Represents a single message exactly as it appears
    in the exported WhatsApp chat.
    """

    timestamp: datetime
    sender: str
    text : str
    is_me:bool




@dataclass
class ConversationTurn:
    sender: str
    is_me: bool
    start_time: datetime
    end_time: datetime
    messages: list[str]


@dataclass
class ConversationPair:
    context: str
    response: str
    conversation_id: int