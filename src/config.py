import os


class Config:
    def __init__(self):
        self.ganache_mode = os.getenv("GANACHE_MODE")
        self.ganache_url = os.getenv("GANACHE_URL")
        self.infura_url = os.getenv("INFURA_URL")
        self.victim_address = os.getenv("VICTIM_ADDRESS")
        self.victim_key = os.getenv("VICTIM_KEY")
        self.recipient_address = os.getenv("RECIPIENT_ADDRESS")
