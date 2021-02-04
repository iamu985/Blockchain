from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey as private
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PublicKey as public
from cryptography.hazmat.primitives import serialization
from datetime import datetime
from brick import Block
from util import formatTime, to_dict

class Client:
	def __init__(self, node=False):
		self.privatekey = private.generate()
		self.publickey = self.privatekey.public_key()
		self.node = node
		self.wallet = 500

	@property
	def identity(self):
		pem = self.publickey.public_bytes(encoding=serialization.Encoding.Raw, format=serialization.PublicFormat.Raw)
		return pem.splitlines()[0].hex()
	
	def mine(self, fuel, chain):
		if self.node:
			#get 3 transactions from the mempool
			try:
				block = Block()
				for i in range(3):
					zeroTransaction = chain.mempool[-i]
					if zeroTransaction not in chain.verified:
						transactionDetails = chain.mempoolData[zeroTransaction]
						if self.verification(transactionDetails, zeroTransaction):
							#managing wallet
							transactionDetails['sender'].wallet -= transactionDetails['amount']
							transactionDetails['receiver'].wallet += transactionDetails['amount']
							prevBlock = chain.chaindata[chain.prevHash] 
							#removing transaction from mempool 
							chain.mempool.remove(zeroTransaction)
							chain.verified.append(zeroTransaction)
							
							#adding transaction to block
							block.transactions.append(zeroTransaction)
							block.transactionsData[zeroTransaction] = transactionDetails
				
				#prepating block
				block.index = prevBlock['index'] + 1
				block.prevHash = chain.prevHash
				block.timestamp = formatTime(datetime.now())
				count = 0
				blockHash = block()
				while count < fuel:
					block.nonce += 1
					blockHash = block()
					if blockHash.startswith('0'*chain.difficulty):
						chain.chain.append(blockHash)
						chain.chaindata[blockHash] = to_dict(block)
						chain.prevHash = blockHash
						chain.submit(self, blockHash)
						break
					count+=1
				#linking the block to the chain
				
			except IndexError:
				print('Not Enough Transactions to mine')
		else:
			print('Mine Function is not allowed for Non-Node Clients')
	
	def verification(self, transactionDetails, transactionHash):
		signature = transactionDetails['signature']
		verifyingKey = transactionDetails['sender'].publickey
		
		flag = verifyingKey.verify(signature, transactionHash.encode('ascii'))
		if flag == None:
			return True
		else:
			return False
