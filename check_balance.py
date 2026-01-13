from web3 import Web3
from eth_account import Account
import os
from dotenv import load_dotenv

load_dotenv()

w3 = Web3(Web3.HTTPProvider(os.getenv('BUILDBEAR_RPC_URL')))
account = Account.from_key(os.getenv('PRIVATE_KEY'))
balance = w3.eth.get_balance(account.address)
print(f'Balance: {w3.from_wei(balance, "ether")} ETH')
print(f'Gas Price: {w3.eth.gas_price}')
