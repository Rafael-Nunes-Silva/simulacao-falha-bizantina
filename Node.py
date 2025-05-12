import random

class Node:
    def __init__(self, node_id, honest=True, initial_vote=None):
        self.node_id = node_id
        self.honest = honest
        self.initial_vote = initial_vote if honest else None
        self.received = {}

    def send_votes(self, nodes):
        if self.honest:
            for n in nodes:
                n.receive_vote(self.node_id, self.initial_vote)
        else:
            for n in nodes:
                vote = random.choice([True, False])
                n.receive_vote(self.node_id, vote)

    def receive_vote(self, sender_id, vote):
        self.received[sender_id] = vote

    def decide(self):
        votes = list(self.received.values()) + ([self.initial_vote] if self.honest else [])
        true_count = votes.count(True)
        false_count = votes.count(False)
        decision = True if true_count > false_count else False
        return decision
