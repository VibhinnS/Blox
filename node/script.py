import json
import binascii
from wallet.utils import calculate_hash
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256
from Crypto.Signature import pkcs1_15

class Stack:
    def __init__(self):
        self.elements = []
        
    def push(self, element):
        self.elements.append(element)
        
    def pop(self):
        return self.elements.pop()
    

class StackScript(Stack):
    def __init__(self, tx_data :dict):
        super().__init__()
        for count, tx_input in enumerate(tx_data["inputs"]):
            tx_input_dict = json.loads(tx_input)
            tx_input_dict.pop("unlock_script")
            tx_data["inputs"][count] = json.dumps(tx_input_dict)
        self.tx_data = tx_data
        
    def op_dup(self):
        public_key = self.pop()
        self.push(public_key)
        self.push(public_key)
    
    def op_hash160(self):
        public_key = self.pop()
        self.push(calculate_hash(calculate_hash(public_key, hash_function="sha256"), hash_function="ripemd160"))
    
    def op_equalverify(self):
        last_elem1 = self.pop()
        last_elem2 = self.pop()
        assert last_elem1 == last_elem2
    
    def op_checksig(self):
        public_key = self.pop()
        signature = self.pop()
        signature_decoded = binascii.unhexlify(signature.encode("utf-8"))
        public_key_bytes = public_key.encode("utf-8")
        public_key_object = RSA.import_key(binascii.unhexlify(public_key_bytes))
        transaction_bytes = json.dumps(self.transaction_data, indent=2).encode('utf-8')
        transaction_hash = SHA256.new(transaction_bytes)
        pkcs1_15.new(public_key_object).verify(transaction_hash, signature_decoded)
