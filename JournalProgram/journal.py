import datetime
import random
import os
import pickle

class Entry:
    def __init__(self, text, prompt, date):
        self.text = text  # The journal entry text
        self.prompt = prompt  # The writing prompt for the entry
        self.date = date  # The date when the entry was written

    def __repr__(self):
        return f"Entry({self.text}, {self.prompt}, {self.date})"


class Journal:
    def __init__(self):
        self.entries = []
        self.prompts = [
            "What did you learn today?",
            "What are you grateful for?",
            "Describe your day in one word.",
            "What are your goals for tomorrow?",
            "What challenges did you face today?"
        ]

    def add_entry(self, text):
        prompt = random.choice(self.prompts)
        date = datetime.datetime.now()
        new_entry = Entry(text, prompt, date)
        self.entries.append(new_entry)

    def display_entries(self):
        for entry in self.entries:
            print(f"Date: {entry.date}")
            print(f"Prompt: {entry.prompt}")
            print(f"Entry: {entry.text}")
            print("-" * 20)

    def save(self, filename="journal_data.pkl"):
        with open(filename, "wb") as file:
            pickle.dump(self.entries, file)

    def load(self, filename="journal_data.pkl"):
        if os.path.exists(filename):
            with open(filename, "rb") as file:
                self.entries = pickle.load(file)

    def get_random_prompt(self):
        return random.choice(self.prompts)
