from builtins import print

import networkx as nx
import flet as ft

def creaGrafo():
    myGraph = nx.Graph()
    #per aggiungere un nodo posso usare:
    myGraph.add_node(1)
    #posso aggiugnere interi, stringhe, istanze (possono essere diversi)
    myGraph.add_node("a")
    myGraph.add_node(ft.Text("Cavallino"))
    mynodes = [1,2,3,4,5,6,7,8,9,10]
    myGraph.add_nodes_from(mynodes)

    # per aggiungere un arco posso usare:
    edgelist= [(1, 2), (1, 3), (3, 4), (4, 5), (2, 1), (4, 1 )]
    myGraph.add_edges_from(edgelist)
    myGraph.add_edge(1,2, weight = 5) # do un peso all'arco per esempio 1.1

    print(myGraph) # questa funzione mi da il __str__ del grafo

    print(f"Nodi di 1: {myGraph[1]}") # mi restituisce il dizionario, che mi restituisce i nodi collegati a 1

    #Esempio 1.1
    print(f"Nodi di 1: {myGraph[1][2]}") # mi da gli attributi dell'arco

    print(f"Nodo 1 nel grafo: {1 in myGraph}" ) # va a testare se il nodo 1 è nel grafo

    #posso iterare in un grafo ( mi stampa i nodi essendo le chiavi del dizionario)
    for v in myGraph:
        print(v)

    #posso ciclare anche solo i nodi vicini a uno specificato
    print("Nodi di 1:")
    for v in myGraph[1]:
        print(v)
    print(f"Nodes: {myGraph.nodes}")
    print(f"Edges: {myGraph.edges}")


    # Posso creare anche dei grafi direzionati
    myDGraph = nx.DiGraph()
    myDGraph.add_edges_from(edgelist)
    myDGraph.add_nodes_from(mynodes)
    myDGraph.add_edge(1,2, attr="foo")

    print(f"Nodes (oriented): {myDGraph.nodes}")
    print(f"Edges (oriented): {myDGraph.edges}")
    print(f"Archi entranti in un nodo: {myDGraph.in_edges(1)}")


    multigraph = nx.MultiDiGraph()
    multigraph.add_nodes_from(mynodes )
    multigraph.add_edges_from(edgelist)
    multigraph.add_edge(1,2, attr="foo")

    print(f"Nodes (oriented): {multigraph.nodes}")
    print(f"Edges (oriented): {multigraph.edges}")
    print(f"Archi entranti in un nodo: {multigraph.in_edges(1)}")
    print(f"Archi uscenti in un nodo: {multigraph.out_edges (1)}")  # mi ridà  l'arco (1,2)
                                                                    # due volte perchè su un
                                                                    # multigraph si può

    print(multigraph[1])    #{2: {0: {}, 1: {'attr': 'foo'}} questo output significa che
                            # il nodo 1 ha due archi connessi al nodo 2.


if __name__ == "__main__":
    creaGrafo()