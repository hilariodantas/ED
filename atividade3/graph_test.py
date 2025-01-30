"""
File: graph_test.py
Example usage and validation of the graph implementation.
"""

from graph import LinkedDirectedGraph
from algorithms import shortestPaths, spanTree, topoSort

def main():
    """Creates a graph, runs algorithms, and prints results."""
    g = LinkedDirectedGraph()
    
    # Adding vertices and edges
    g.addEdge("A", "B", 2)
    g.addEdge("A", "C", 5)
    g.addEdge("B", "C", 1)
    g.addEdge("B", "D", 3)
    g.addEdge("C", "D", 2)
    g.addEdge("D", "E", 4)
    
    print("Graph representation:")
    print(g)
    
    # Running shortest paths from A
    print("\nShortest paths from A:")
    shortest_paths = shortestPaths(g, "A")
    for vertex, (distance, predecessor) in shortest_paths.items():
        print(f"To {vertex}: Distance = {distance}, Predecessor = {predecessor}")
    
    # Running minimum spanning tree from A
    print("\nMinimum Spanning Tree from A:")
    mst = spanTree(g, "A")
    for edge in mst:
        print(f"{edge[0]} - {edge[1]} (Weight: {edge[2]})")
    
    # Running topological sort
    print("\nTopological Sort:")
    sorted_vertices = topoSort(g)
    while not sorted_vertices.isEmpty():
        print(sorted_vertices.pop().getLabel(), end=" ")
    print()

if __name__ == "__main__":
    main()