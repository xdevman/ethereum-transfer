import os


class Config:
    def __init__(self):
        self.ganache_mode = os.getenv("RPC_URL")
        self.ganache_url = os.getenv("WATCHED_ADDRESS")
        self.infura_url = os.getenv("RESERVE_ADDRESS")
        self.victim_address = os.getenv("WATCHED_PRIVATE_KEY")
        self.victim_key = float(os.getenv("MIN_BALANCE", "0.001"))
        self.recipient_address = int(os.getenv("POLL_INTERVAL", "1"))
