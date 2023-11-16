import rlp
import socket
import threading

class EthereumProtocol:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.peers = []

    def start(self):
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(5)
        print(f"Listening for incoming connections on {self.host}:{self.port}")

        while True:
            client_socket, addr = self.server_socket.accept()
            print(f"Accepted connection from {addr}")
            self.handle_connection(client_socket)

    def handle_connection(self, client_socket):
        peer = EthereumPeer(client_socket)
        self.peers.append(peer)
        threading.Thread(target=self.receive_messages, args=(peer,)).start()

    def receive_messages(self, peer):
        while True:
            data = peer.receive()
            if not data:
                print(f"Connection with {peer.address} closed.")
                self.peers.remove(peer)
                break

            # Process received data (deserialize, handle messages, etc.)
            self.process_data(data)

    def send_message(self, peer, message):
        serialized_message = rlp.encode(message)
        peer.send(serialized_message)

    def process_data(self, data):
        # Implement logic to handle received data
        pass

class EthereumPeer:
    def __init__(self, socket):
        self.socket = socket
        self.address = self.socket.getpeername()

    def send(self, data):
        self.socket.send(data)

    def receive(self):
        data = self.socket.recv(1024)
        return data

# Example Usage:
if __name__ == "__main__":
    host = "127.0.0.1"
    port = 30303

    ethereum_protocol = EthereumProtocol(host, port)
    ethereum_protocol.start()
