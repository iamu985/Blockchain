from datetime import datetime


def formatTime(timeStruct):
	return f'{timeStruct.year}-{timeStruct.month}-{timeStruct.day}-{timeStruct.hour}:{timeStruct.minute}:{timeStruct.second}'

def to_dict(block):
	return block.__dict__

def display(chain):
	blockchaindata = chain.chaindata
	for keys, values in blockchaindata.items():
		transactionsdata = values['transactionsData']
		transactionsHash = values['transactions']
		print(f"\nBlock #{values['index']}")
		print(f'\tBlockHash: {keys}')
		print(f"\tTotal Transactions: {len(values['transactions'])}")
		print(f"\tMerkle Root: {values['prevHash']}")
		print(f"\tTimestamp: {values['timestamp']}")
		print("\n\nTransactions: ")
		for transactions in transactionsHash:
			details = transactionsdata[transactions]
			print(f"\t\tTransaction: {transactions}")
			print(f"\t\tTime: {details['timestamp']}")
			print(f"\t\tAmount: {details['amount']}")
		
