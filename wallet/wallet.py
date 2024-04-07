import base58
import binascii
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcsl_15
from utils import calculate_hash, generate_transaction_data, convert_transaction_data_to_bytes

class Owner:
    def __init__(self, private_key: RSA.RsaKey, public_key :bytes, bitcoin_address :bytes):
        self.private_key = private_key
        self.public_key = public_key
        self.bitcoin_address = bitcoin_address



class Transaction:
    def __init__(self, owner: Owner, receiver_bitcoin_address :bytes, amount :int):
        self.owner = owner
        self.receiver_bitcoin_address = receiver_bitcoin_address
        self.amount = amount
        
    def generate_data(self) -> bytes:
        transaction_data = generate_transaction_data(self.owner.bitcoin_address, self.receiver_bitcoin_address, self.amount)
        return convert_transaction_data_to_bytes(transaction_data)
    
    def sign(self) -> None:
        transaction_data = self.generate_data()
        hash_object = SHA256.new(transaction_data)
        signature = pkcsl_15.new(self.owner.private_key).sign(hash_object)
        self.signature = binascii.hexlify(signature).decode("utf-8")
    
    def send_to_nodes(self):
        return {
            "sender_address":self.owner.bitcoin_address,
            "receiver_address":self.receiver_bitcoin_address,
            "amount":self.amount,
            "signature":self.signature
        }
    

def initialize_wallet(self) -> object:
    private_key = RSA.generate(2048)
    public_key = private_key.publickey().export_key()
    hash_1 = calculate_hash(public_key, hash_function="sha256")
    hash_2 = calculate_hash(hash_1, hash_function="ripemd160")
    bitcoin_address = base58.b58encode(hash_2)
    return Owner(private_key, public_key, bitcoin_address)





