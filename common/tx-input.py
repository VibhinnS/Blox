import json

class TransactionInput:
    def __init__(self, tx_hash :str, output_index :int, unlock_script :str = ""):
        self.tx_hash = tx_hash
        self.output_index = output_index
        self.unlock_script = unlock_script
        
        
    def to_json(self, with_unlock_script :bool = True) -> str:
        if with_unlock_script:
            return json.dumps({
                "tx_hash": self.tx_hash,
                "output_index": self.output_index,
                "unlock_script": self.unlock_script
            })
        else:
            return json.dumps({
                "tx_hash": self.tx_hash,
                "output_index": self.output_index
            })
            
    