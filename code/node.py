# node.py
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Modulo node

Definisce la classe Node per rappresentare un nodo nella rete
nel protocollo Distance Vector Routing.
"""

from typing import Dict, Tuple


class Node:
    """Rappresenta un nodo nella rete."""

    def __init__(self, name: str):
        """
        Inizializza un nuovo nodo.

        Args:
            name (str): Il nome identificativo del nodo.
        """
        self.name: str = name
        self.neighbors: Dict['Node', int] = {}
        self.routing_table: Dict[str, Tuple[int, str]] = {self.name: (0, self.name)}
        if not name:
            raise ValueError("Il nome del nodo non può essere vuoto.")

    def add_neighbor(self, neighbor: 'Node', cost: int):
        """
        Aggiunge un vicino diretto al nodo con il costo associato.
        
        Args:
            neighbor (Node): Il nodo vicino da aggiungere.
            cost (int): Il costo per raggiungere il vicino.
        
        Raises:
            ValueError: Se il vicino è già definito con un costo diverso.
        """
        if neighbor in self.neighbors:
            if self.neighbors[neighbor] != cost:
                raise ValueError(f"Il vicino {neighbor.name} è già definito con un costo {self.neighbors[neighbor]}.")
        self.neighbors[neighbor] = cost
        self.routing_table[neighbor.name] = (cost, neighbor.name)

    def remove_neighbor(self, neighbor: 'Node'):
        """
        Rimuove un vicino diretto dal nodo.
        In questo modo si può simulare la perdita di una connessione.

        Args:
            neighbor (Node): Il nodo vicino da rimuovere.
        """
        if neighbor in self.neighbors:
            del self.neighbors[neighbor]
            self.routing_table.pop(neighbor.name, None)

    def update_routing_table(self) -> bool:
        """
        Aggiorna la tabella di routing basandosi sulle tabelle dei vicini.

        Returns:
            bool: True se la tabella è stata aggiornata, False altrimenti.
        """
        if not self.neighbors:
            print(f"Attenzione: il nodo {self.name} non ha vicini.")
            return False

        updated = False
        for neighbor, cost_to_neighbor in self.neighbors.items():
            neighbor_table = neighbor.routing_table
            for dest, (cost_to_dest, _) in neighbor_table.items():
                if dest == self.name:
                    continue  # Evita percorsi verso se stesso attraverso altri nodi
                new_cost = cost_to_neighbor + cost_to_dest
                current_cost = self.routing_table.get(dest, (float('inf'), None))[0]
                if new_cost < current_cost:
                    self.routing_table[dest] = (new_cost, neighbor.name)
                    updated = True
        return updated

    def print_routing_table(self):
        """Stampa la tabella di routing corrente del nodo."""
        print(f"Tabella di routing per il nodo {self.name}:")
        print(f"{'Destinazione':<15}{'Costo':<10}{'Prossimo Hop':<15}")
        for dest, (cost, next_hop) in sorted(self.routing_table.items()):
            print(f"{dest:<15}{cost:<10}{next_hop:<15}")
        print("-" * 40)

    def print_routing_table_to_string(self) -> str:
        """
        Restituisce la tabella di routing come stringa.

        Returns:
            str: La rappresentazione della tabella di routing.
        """
        output = [f"Tabella di routing per il nodo {self.name}:"]
        output.append(f"{'Destinazione':<15}{'Costo':<10}{'Prossimo Hop':<15}")
        for dest, (cost, next_hop) in sorted(self.routing_table.items()):
            output.append(f"{dest:<15}{cost:<10}{next_hop:<15}")
        output.append("-" * 40)
        return "\n".join(output)