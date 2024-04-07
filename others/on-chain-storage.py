"""This code defines classes for User, Post, and Blockchain. The User class represents a social media user with a username, public key, and a list of posts. The Post class represents a social media post with an author, content, timestamp, and a post hash. The Blockchain class represents the blockchain that stores social media posts.

To store a social media post on-chain, a user would first create a new post using the User.create_post() method. This method would create a new Post object and add it to the user's list of posts. The method would also calculate the post hash and set it as the post's post_hash attribute.

"""

import hashlib
import json

class User:
    def __init__(self, username, public_key):
        self.username = username
        self.public_key = public_key
        self.posts = []

    def create_post(self, content, timestamp):
        post_hash = hashlib.sha256(json.dumps({
            "content": content,
            "timestamp": timestamp
        }).encode('utf-8')).hexdigest()

        new_post = Post(self.username, content, timestamp, post_hash)
        self.posts.append(new_post)
        return new_post

class Post:
    def __init__(self, author, content, timestamp, post_hash):
        self.author = author
        self.content = content
        self.timestamp = timestamp
        self.post_hash = post_hash

class Blockchain:
    def __init__(self):
        self.chain = []
        self.users = {}

    def create_genesis_block(self):
        genesis_block = Post(None, 'Genesis block', 0, '0x0')
        self.chain.append(genesis_block)

    def add_block(self, post):
        if post.post_hash != self.chain[-1].post_hash:
            raise Exception('Invalid previous hash')

        self.chain.append(post)

    def get_last_block(self):
        return self.chain[-1]

    def add_user(self, username, public_key):
        new_user = User(username, public_key)
        self.users[username] = new_user

    def create_post(self, username, content, timestamp):
        if username not in self.users:
            raise Exception(f'User {username} not found')

        new_post = self.users[username].create_post(content, timestamp)
        self.add_block(new_post)
