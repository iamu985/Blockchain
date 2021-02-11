from hashlib import sha256
from datetime import datetime
from node import Client
from transaction import Transactions
from util import formatTime, to_dict
from brick import Block
import random

class Blockchain:
	def __init__(self):
		self.mempool = []
		self.mempoolData = {}
		self.chain = []
		self.chaindata = {}
		self.difficulty = 2
		self.prevHash = ''
		self.verified = []
	
	def init(self):
		gen0 = Client()
		gen1 = Client()
		genesis_transaction = Transactions(gen0, gen1, 3)
		genesis_transaction(self)
		
		#verify
		transaction = self.mempool[-1]
		transactionData = self.mempoolData[transaction]
		
		#getting signature and public key fromo data
		transactionSignature = transactionData['signature']
		transactionVerifyKey = transactionData['sender'].publickey
		
		if gen0.verification(transactionData, transaction):
			#managing accounts
			transactionData['sender'].wallet -= transactionData['amount']
			transactionData['receiver'].wallet += transactionData['amount']
			
			#deleting the transaction from mempool
			self.mempool.remove(transaction)
			self.verified.append(transaction)
			genesis = Block()
			genesis.transactions.append(transaction)
			genesis.transactionsData[transaction] = transactionData
			genesis.index = 0
			genesis.timestamp = formatTime(datetime.now())
			genesis.prevHash = "Genesis"
			
			#Mining Block
			proof = genesis()
			while not proof.startswith('0'*self.difficulty):
				genesis.nonce += 1
				proof = genesis()
			self.chain.append(proof)
			self.chaindata[proof] = to_dict(genesis)
			self.prevHash = genesis.genHash(genesis.nonce)
			print('Blockchain is initialised')
	
	def submit(self, miner, proof):
		reward = [i for i in range(1, 11)]
		publicIdenity = miner.identity
		number_of_transactions = len(self.chaindata[proof]['transactions'])
		reward_amount = random.choice(reward) * number_of_transactions
		miner.wallet += reward_amount


