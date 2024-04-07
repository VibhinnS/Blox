import hashlib

class User:
    def __init__(self, username, public_key):
        self.username = username
        self.public_key = public_key
        self.posts = []

class Post:
    def __init__(self, author, content, timestamp):
        self.author = author
        self.content = content
        self.timestamp = timestamp
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        sha = hashlib.sha256()
        sha.update(str(self.author).encode('utf-8'))
        sha.update(self.content.encode('utf-8'))
        sha.update(str(self.timestamp).encode('utf-8'))
        return sha.hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = []
        self.users = {}

    def create_genesis_block(self):
        genesis_block = Post(None, 'Genesis block', 0)
        self.chain.append(genesis_block)

    def add_block(self, post):
        if post.calculate_hash() != self.chain[-1].hash:
            raise Exception('Invalid previous hash')

        self.chain.append(post)

    def get_last_block(self):
        return self.chain[-1]

    def add_user(self, username, public_key):
        new_user = User(username, public_key)
        self.users[username] = new_user

    def create_post(self, author, content, timestamp):
        if author not in self.users:
            raise Exception(f'User {author} not found')

        new_post = Post(author, content, timestamp)
        self.users[author].posts.append(new_post)
        self.add_block(new_post)

        # Gossip the new post to random peers
        gossip_transaction(new_post)