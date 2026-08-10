import re
from pathlib import Path
from datetime import datetime

from src.models import RawMessage


class WhatsAppParser:

    def parse_folder(self, folder_path):
        all_messages = []
        folder = Path(folder_path)
        for file in folder.glob("*.txt"):
            messages = self.parse(file)
            all_messages.extend(messages)
        return all_messages

    def __init__(self, my_name):
        self.my_name = my_name

    def _parse_timestamp(self, date_str, time_str, period):
       
       
    #Convert WhatsApp date and time into a datetime object.
    

       timestamp = f"{date_str} {time_str} {period}"

       return datetime.strptime(
        timestamp,
        "%m/%d/%y %I:%M %p"
       )
    def parse(self, file_path):

        path = Path(file_path)

        print(f"Reading: {path}")

        with open(path, "r", encoding="utf-8") as file:
            lines = file.readlines()
        message_pattern = re.compile(
        r"^(\d{1,2}/\d{1,2}/\d{2,4}),\s+"
        r"(\d{1,2}:\d{2})\s*([AP]M)\s+-\s+"
        r"([^:]+):\s(.*)$"
)
        messages = []
        current_message = None

        for line in lines:

         match = message_pattern.match(line)

         if match:
            date = match.group(1)
            time = match.group(2)
            period = match.group(3)
            sender = match.group(4)
            sender = sender.replace("~", "").strip()
            if sender == self.my_name:
               sender = "YOU"
            text = match.group(5)
            text =text.strip()
            timestamp = self._parse_timestamp(
               date,
               time,
               period
            )
            message = RawMessage(
             timestamp=timestamp,
             sender=sender,
             text=text,
             is_me=(sender == "YOU")
             )

            messages.append(message)

        return messages       


