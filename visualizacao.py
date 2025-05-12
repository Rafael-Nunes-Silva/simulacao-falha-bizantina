import random
import matplotlib.pyplot as plt

from Node import Node

def simulate_once(n_nodes, n_malicious):
    """Simula uma rodada de votação entre os nós."""
    nodes = []
    for i in range(n_nodes):
        if i < n_malicious:
            nodes.append(Node(i, honest=False))
        else:
            nodes.append(Node(i, honest=True, initial_vote=random.choice([True, False])))

    for node in nodes:
        node.send_votes(nodes)

    results = {node.node_id: node.decide() for node in nodes if node.honest}
    
    return len(set(results.values())) == 1

def consensus_rates(n, max_f, trials):
    """Calcula a taxa de sucesso entre as votações"""
    rates = []
    for f in range(0, max_f + 1):
        success_count = sum(simulate_once(n, f) for _ in range(trials))
        rates.append((success_count / trials) * 100)
    return rates

n = 100        # total de nós
max_f = 20     # número máximo de nós maliciosos
trials = 200   # número de simulações por rodada
rates = consensus_rates(n, max_f, trials)

plt.figure()
plt.plot(range(0, max_f + 1), rates, marker="o")
plt.title(f"Taxa de Sucesso vs Nós Maliciosos (n={n})")
plt.xlabel("Número de Nós Maliciosos (f)")
plt.ylabel("Taxa de Sucesso na Votação (%)")
plt.xticks(range(0, max_f + 1))
plt.yticks(range(0, 101, 10))
plt.ylim(0, 101)
plt.grid(True)
plt.show()
