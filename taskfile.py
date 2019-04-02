import hashlib
import datetime

class Block:
    blockNumber = 0
    data = None
    nextBlock = None
    hash = None
    nonce = 0
    previousHash = 0x0
    timestamp = datetime.datetime.now()

    def __init__(self,data):
        #Initialises the block by saving the data as the block data, can be anything including the amount of money sent.
        self.data=data
    #Function to hash the data of the block
    def hash(self):
        h  = hashlib.sha256()
        h.update(
            str(self.nonce).encode('utf-8') +
            str(self.data).encode('utf-8') +
            #Remember the previous hash of the block is also included, this is what make the blockchain immutable
            str(self.previousHash).encode('utf-8') +
            str(self.timestamp).encode('utf-8') +
            str(self.blockNumber).encode('utf-8')
        )
        return h.hexdigest()
    def __str__(self):
        return "Block Hash: " + str(self.hash()) + "\nBlockNo: " + str(self.blockNumber) + "\nBlock Data: " + str(self.data) + "\nHashes: " + str(self.nonce) + "\n--------------"


class Blockchain:

    difficulty = 1
    maxNonce = 2**32
    target = 2 ** (256-difficulty)
    #The genesis block is just a normal header pointer
    block = Block("Genesis")
    dummy=head = block

    def add(self, block):

        #Add your code here

    def mine(self, block):
        for block.nonce in range(self.maxNonce):
            # if the integer value of the hash is less than the target then the block is added
            # else the nonce is incremented and you try again
            if int(block.hash(), 16) <= self.target:
                #add your code here


    def printBlockchain(self):
        while self.head != None:
            print(self.head)
            self.head = self.head.nextBlock

Stephens_Coin = Blockchain
for n in range(10):
    Stephens_Coin.mine(Stephens_Coin,Block("Block " + str(n+1)))

Stephens_Coin.printBlockchain(Stephens_Coin)
