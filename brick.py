from hashlib import sha256

class Block:
	def __init__(self):
		self.index = 0
		self.transactions = []
		self.transactionsData = {}
		self.timestamp = ''
		self.prevHash = ''
		self.nonce = 0
	
	def __call__(self):
		return sha256(str(self.__dict__).encode('ascii')).hexdigest()

