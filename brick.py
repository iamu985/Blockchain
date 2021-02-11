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
		hashprint = sha256(str(self.__dict__).encode('ascii')).hexdigest()
		while not hashprint.startswith('0'*2):
			self.nonce += 1
			hashprint = sha256(str(self.__dict__).encode('ascii')).hexdigest()
		return hashprint
	
	@staticmethod
	def genHash(nonce):
		return sha256(str(nonce).encode('ascii')).hexdigest()

