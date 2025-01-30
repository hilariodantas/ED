
from algorithms import shortestPaths, spanTree, topoSort
from graph import LinkedDirectedGraph

class GraphDemoView:

    def __init__(self):
        self.model = GraphDemoModel()

    def run(self):
        menu = """
Main Menu
1  Input a graph from the keyboard
2  View the current graph
3  Single-source shortest paths
4  Minimum spanning tree
5  Topological sort
6  Exit the program
"""
        while True:
            command = self.getCommand(6, menu)
            if command == 1:
                self.getFromKeyboard()
            elif command == 2:
                print(self.model.getGraph())
            elif command == 3:
                print("Paths:\n", self.model.run(shortestPaths))
            elif command == 4:
                print("Tree:", " ".join(map(str, self.model.run(spanTree))))
            elif command == 5:
                print("Sort:", " ".join(map(str, self.model.run(topoSort))))
            else:
                break

    def getCommand(self, high, menu):
        while True:
            try:
                command = int(input(menu + "\nEnter a number [1-7]: "))
                if 1 <= command <= high:
                    return command
            except ValueError:
                pass
            print("Invalid input. Try again.")

    def getFromKeyboard(self):
        rep = ""
        while True:
            edge = input("Enter an edge (format: A>B:1) or press Enter to quit: ")
            if edge == "":
                break
            rep += edge + " "
        startLabel = input("Enter the start label: ")
        print(self.model.createGraph(rep, startLabel))

class GraphDemoModel:

    def __init__(self):
        self.graph = None
        self.startLabel = None

    def createGraph(self, rep, startLabel):
        self.graph = LinkedDirectedGraph()
        self.startLabel = startLabel
        edgeList = rep.split()
        for edge in edgeList:
            if '>' in edge and ':' in edge:
                fromLabel, rest = edge.split('>')
                toLabel, weight = rest.split(':')
                weight = int(weight)
                self.graph.addEdge(fromLabel, toLabel, weight)
            else:
                if not self.graph.containsVertex(edge):
                    self.graph.addVertex(edge)
                else:
                    return "Duplicate vertex"
        if not self.graph.containsVertex(startLabel):
            self.graph = None
            return "Start label not in graph"
        return "Graph created successfully"

    def getGraph(self):
        return str(self.graph) if self.graph else None

    def run(self, algorithm):
        return algorithm(self.graph, self.startLabel) if self.graph else None

if __name__ == "__main__":
    GraphDemoView().run()