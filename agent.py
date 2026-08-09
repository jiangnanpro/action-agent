# agent.py
class ActionAgent:
    def __init__(self, name: str):
        self.name = name

    def run(self):
        print(f"Agent {self.name} is running...")
