from typing import ByteString
from eth_utils.conversions import to_hex
from eth_utils.currency import from_wei
from web3 import Web3
import json
import requests
from decimal import *


ganache_url = "HTTP://127.0.0.1:8545"
web3 = Web3(Web3.HTTPProvider(ganache_url))

# infura_url= "https://mainnet.infura.io/v3/8a422fe86e44c0ab9fdc4aea947b15b6"
# web3 = Web3(Web3.HTTPProvider(infura_url))


# check connecting web3 to Ganache
if  web3.isConnected() == True:
    print("started")
else :
    print("error connecting...")

# get gas price
# try :
#     gas_url= "https://www.gasnow.org/api/v3/gas/price"
#     r = requests.get(gas_url)
#     r = r.json()
#     r = r['data']
#     r = r['fast']
#     r = web3.fromWei(r, "Gwei")
# except:
#     print("error gas")

#accounts value and private key
print("Done gas")
account_1 = "0x242F5c9a1D42e962A1c6B479349FFAf188163757"
account_2 = "0x858C1eAC770C883f6FB4496B856023A7A483b6B6"
private_key = "3ddc37fdcd6ba99f9a16206467e459d4009ab30b3b4909a5ba0ca50ea40d2624"

balance=0
gas_fee = 21000*56  # You can change gasfee value
gas_fee = Decimal(gas_fee)
gas_fee = web3.fromWei(gas_fee,'Gwei')
print("get balance...","gas fee is : ", gas_fee)
def get_balance_loop():
    balance=0
    while True:
        while 0.0005>balance:
            #Get balance account
            try:
                balance = web3.eth.getBalance(account_1)
                balance = web3.fromWei(balance, "ether") #convert to ether value
            except:
                print("error , i can't get balance...")

        try:
            balance = balance-gas_fee
            print(balance)
            # print(balance)
            # print(web3.fromWei(balance, "ether"))
            build_transaction(balance)
        except:
            print("Error, check balance and Gasfee again")
            


def build_transaction(balance):
    try:
        #get nonce number
        nonce = web3.eth.getTransactionCount(account_1)
        #build transaction
        tx = {
            'nonce':nonce,
            'to':account_2,
            'value':web3.toWei(balance,'ether'),
            'gas':21000,
            'gasPrice':web3.toWei('56','gwei')
        }

        #sign transaction with private key
        signed_tx = web3.eth.account.signTransaction(tx,private_key)
        #send Transaction
        tx_hash= web3.eth.sendRawTransaction(signed_tx.rawTransaction)

        print(web3.toHex(tx_hash))
        print("Transaction Completed\n GET Balance Again...")
        get_balance_loop()
    except:
        print("ERROR, check buldTransction Funcation")

get_balance_loop()
