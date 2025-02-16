import hashlib
import time

# 1. Klasa për një Bllok
class Block:
    def __init__(self, index, data, previous_hash):
        self.index = index
        self.data = data
        self.previous_hash = previous_hash
        self.timestamp = time.time()
        self.nonce = 0  # Numri i përpjekjeve për "minierë"
        self.hash = self.calculate_hash()

    # Llogarit hash-in e bllokut (si "ID unik")
    def calculate_hash(self):
        return hashlib.sha256(
            f"{self.index}{self.data}{self.previous_hash}{self.timestamp}{self.nonce}".encode()
        ).hexdigest()

# 2. Klasa për Blockchain
class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.difficulty = 2  # Sa zero duhet të fillojë hash-i (vështirësia)

    # Blloku i parë (i veçantë)
    def create_genesis_block(self):
        return Block(0, "Genesis Block", "0")

    # Shto një bllok të ri
    def add_block(self, data):
        new_block = Block(len(self.chain), data, self.chain[-1].hash)
        print("Duke minuar bllokun...")
        # "Mino" bllokun (Proof of Work)
        while new_block.hash[:self.difficulty] != "0" * self.difficulty:
            new_block.nonce += 1
            new_block.hash = new_block.calculate_hash()
        self.chain.append(new_block)
        print("Blloku u shtua!")

    # Kontrollo nëse blockchain-i është i vlefshëm
    def is_valid(self):
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i-1]
            if current.hash != current.calculate_hash():
                return False
            if current.previous_hash != previous.hash:
                return False
        return True

# 3. Testo kodin
if __name__ == "__main__":
    blockchain = Blockchain()

    # Shto 2 blloqe
    blockchain.add_block("Data 1")
    blockchain.add_block("Data 2")

    # Shfaq të gjithë blockchain
    print("\nBlockchain:")
    for block in blockchain.chain:
        print(f"Blloku {block.index}: {block.hash}")

    # Kontrollo validitetin
    print("\nBlockchain valide?", blockchain.is_valid())