# network_simulation.py
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Modulo network

Contiene le funzioni per simulare la rete utilizzando il protocollo
Distance Vector Routing.
"""

from typing import List
from node import Node


def simulate_network(nodes: List[Node], output_file: str = None):
    """
    Simula l'aggiornamento delle tabelle di routing nella rete fino alla convergenza.

    Args:
        nodes (List[Node]): La lista dei nodi nella rete.
        output_file (str, optional): Percorso del file dove salvare l'output. Default: None.
    """
    iteration = 0
    output = []
    while True:
        output.append(f"\n--- Iterazione {iteration} ---")
        updated = False
        for node in nodes:
            if node.update_routing_table():
                updated = True
        for node in nodes:
            output.append(node.print_routing_table_to_string())
        if not updated:
            output.append("Le tabelle di routing sono stabili.")
            break
        iteration += 1

    if output_file:
        with open(output_file, 'w') as f:
            f.writelines("\n".join(output))
    else:
        print("\n".join(output))