from node import Client
from transaction import Transactions
from blocks import Blockchain
from util import display

frank = Client(node=True)
alex = Client()
britty = Client()
winni = Client()

miner0 = Client(node=True)
miner1 = Client(node=True)

chain = Blockchain()
chain.init()

frank = Client()
alex = Client()

miner0 = Client(node=True)
miner1 = Client(node=True)
print(miner0.wallet)
print(miner1.wallet)
t0 = Transactions(frank, alex, 30)
t0(chain)

t1 = Transactions(alex, frank, 45)
t1(chain)

t2 = Transactions(alex, frank, 21)
t2(chain)

t3 = Transactions(frank, alex, 65)
t3(chain)

t4 = Transactions(alex, frank, 23)
t4(chain)

miner0.mine(100000, chain)

t5 = Transactions(britty, winni, 34)
t5(chain)

t6 = Transactions(winni, britty, 21)
t6(chain)

t7 = Transactions(britty, winni, 58)
t7(chain)

t8 = Transactions(winni, britty, 76)
t8(chain)

miner1.mine(200000, chain)
#display(chain)
print(miner0.wallet)
print(miner1.wallet)
