import random

def gossip_transaction(transaction):
    # Select random peers
    peers = random.sample(connected_peers, k=min(len(connected_peers), 5))

    # Send transaction to selected peers
    for peer in peers:
        send_transaction(peer, transaction)
