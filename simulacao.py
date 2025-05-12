import random
import threading

from Node import Node

"""
- Nós Honestos (honest=True) definem um voto inicial aleatório (True/False) e o anunciam corretamente a todos.

- Nós Maliciosos (honest=False) enviam votos conflitantes (escolhendo aleatoriamente True ou False para cada destinatário).

- Após a fase de broadcast, cada nó honesto conta os votos recebidos + seu próprio voto e decide pela maioria.
"""

def simulate(n_nodes=4, n_malicious=1):
    nodes = []
    for i in range(n_nodes):
        if i < n_malicious:
            nodes.append(Node(i, honest=False))
        else:
            nodes.append(Node(i, honest=True, initial_vote=random.choice([True, False])))

    threads = []
    for node in nodes:
        t = threading.Thread(target=node.send_votes, args=(nodes,))
        t.start()
        threads.append(t)
    for t in threads:
        t.join()

    results = {node.node_id: node.decide() for node in nodes if node.honest}
    print("Decisões dos nós honestos:")
    for nid, dec in results.items():
        print(f"Nó {nid}: {dec}")
    if len(set(results.values())) == 1:
        print("Censenso:", list(results.values())[0])
    else:
        print("Consenso não foi atingido (decisões divergentes)")

simulate(100, 10)
