import json
from typing import Any
from datetime import datetime
from utils import calculate_hash


class Block(object):
    def __init__(
        self, 
        timestamp :float, 
        transaction_data :Any, 
        previous_block = None
        ):
        self.transaction_data = transaction_data
        self.previous_block = previous_block
        self.timestamp = timestamp
        
    @property
    def previous_block_cryptographic_hash(self):
        previous_block_cryptographic_hash = ""
        if self.previous_block:
            previous_block_cryptographic_hash = self.previous_block_cryptographic_hash
        return previous_block_cryptographic_hash
    
    @property
    def cryptographic_hash(self) -> str:
        block_content = {
            "transaction_data": self.transaction_data,
            "timestamp": self.timestamp,
            "previous_block_cryptographic_hash": self.previous_block_cryptographic_hash
        }
        block_content_bytes = json.dumps(block_content, indent=2).encode('utf-8')
        return calculate_hash(block_content_bytes)
