
from web3 import Web3
import json
import requests
from decimal import *

#ganache testnet

ganache_url = "HTTP://127.0.0.1:8545"
web3 = Web3(Web3.HTTPProvider(ganache_url))

#infura mainnet 

# infura_url= "https://mainnet.infura.io/"  #signup infura.io and add project id 
# web3 = Web3(Web3.HTTPProvider(infura_url))


#connecting web3 to Ganache
if  web3.isConnected() == True:
    print("web3 connected...\n")
else :
    print("error connecting...")


#accounts value and private key

account_1 = "0x242F5c9a1D42e962A1c6B479349FFAf188163757" ## add public key from first account (sender)
account_2 = "0x0F1eFBb7b0C2Af2CC7d0976655A4a0e95AdB2246" ## add public key from second account (reciver)
private_key = "3ddc37fdcd6ba99f9a16206467e459d4009ab30b3b4909a5ba0ca50ea40d2624" ## add ETH private key from first account (sender)

balance=0
gas_fee = 21000*35
gas_fee = Decimal(gas_fee)
gas_fee = web3.fromWei(gas_fee,'Gwei')


#Get balance account
balance = web3.eth.getBalance(account_1)
balance = web3.fromWei(balance, "ether") #convert to ether value

balance = balance-gas_fee
# print(balance)
# print(balance)
# print(web3.fromWei(balance, "ether"))


#get nonce number
nonce = web3.eth.getTransactionCount(account_1)

#build transaction
tx = {
    'nonce':nonce,
    'to':account_2,
    'value':web3.toWei(balance,'ether'),
    'gas':21000,
    'gasPrice':web3.toWei('35','gwei')
}

#sign transaction with private key
signed_tx = web3.eth.account.signTransaction(tx,private_key)

#send Transaction
tx_hash= web3.eth.sendRawTransaction(signed_tx.rawTransaction)

print(web3.toHex(tx_hash))