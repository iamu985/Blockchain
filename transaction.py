from hashlib import sha256
from util import formatTime
from datetime import datetime
class Transactions:
	def __init__(self, sender, receiver, amount):
		self.sender = sender
		self.receiver = receiver
		self.amount = amount
		self.timestamp = ''
	
	def __call__(self, chain):
		string = sha256(str(self.__dict__).encode('ascii')).hexdigest()
		signature = self.sign_transation(string)
		chain.mempool.append(string)
		chain.mempoolData[string] = self.to_dict(signature)
		
	def sign_transation(self, string):
		signingkey = self.sender.privatekey
		signature = signingkey.sign(string.encode('ascii'))
		self.timestamp = formatTime(datetime.now())
		return signature
	
	def to_dict(self, signature):
		return {
		'sender':self.sender,
		'receiver':self.receiver,
		'amount':self.amount,
		'timestamp':self.timestamp,
		'signature':signature,
		}

