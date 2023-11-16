import hashlib
import time

class Block:
    def __init__(self, index, transactions, timestamp, previous_hash):
        self.index = index
        self.transactions = transactions
        self.timestamp = timestamp
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        sha = hashlib.sha256()
        sha.update(str(self.index).encode('utf-8'))
        sha.update(str(self.transactions).encode('utf-8'))
        sha.update(str(self.timestamp).encode('utf-8'))
        sha.update(str(self.previous_hash).encode('utf-8'))
        return sha.hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = []

    def create_genesis_block(self):
        genesis_block = Block(0, [], 0, '0')
        self.chain.append(genesis_block)

    def add_block(self, block):
        if block.previous_hash != self.chain[-1].hash:
            raise Exception('Invalid previous hash')

        block.hash = block.calculate_hash()
        self.chain.append(block)

    def get_last_block(self):
        return self.chain[-1]

blockchain = Blockchain()
blockchain.create_genesis_block()

transaction = {
    'sender': 'Alice',
    'recipient': 'Bob',
    'amount': 10
}

block = Block(1, [transaction], time.time(), blockchain.get_last_block().hash)
blockchain.add_block(block)

print(blockchain.chain)
