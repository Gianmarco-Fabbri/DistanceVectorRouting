# main.py
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Punto di ingresso per la simulazione del protocollo Distance Vector Routing.
"""

from node import Node
from network import simulate_network


def main():
    """Funzione principale che configura la rete e avvia la simulazione."""
    # Creazione dei nodi
    node_a = Node('A')
    node_b = Node('B')
    node_c = Node('C')
    node_d = Node('D')

    # Definizione delle connessioni e dei costi tra i nodi
    node_a.add_neighbor(node_b, 1)
    node_a.add_neighbor(node_c, 5)

    node_b.add_neighbor(node_a, 1)
    node_b.add_neighbor(node_c, 2)
    node_b.add_neighbor(node_d, 4)

    node_c.add_neighbor(node_a, 5)
    node_c.add_neighbor(node_b, 2)
    node_c.add_neighbor(node_d, 1)

    node_d.add_neighbor(node_b, 4)
    node_d.add_neighbor(node_c, 1)

    # Lista dei nodi nella rete
    nodes = [node_a, node_b, node_c, node_d]

    # Avvio della simulazione con output in un file
    simulate_network(nodes, output_file="output.txt")


if __name__ == '__main__':
    main()