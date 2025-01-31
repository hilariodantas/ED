

class LinkedVertex:

    def __init__(self, label):
        self.label = label
        self.edgeList = []
        self.mark = False
    
    def setMark(self):
        self.mark = True
    
    def clearMark(self):
        self.mark = False
    
    def isMarked(self):
        return self.mark
    
    def getLabel(self):
        return self.label
    
    def incidentEdges(self):
        return iter(self.edgeList)
    
    def neighboringVertices(self):
        return (edge.getOtherVertex(self) for edge in self.edgeList)
    
    def addEdgeTo(self, toVertex, weight):
        edge = LinkedEdge(self, toVertex, weight)
        self.edgeList.append(edge)
        toVertex.edgeList.append(edge)  # Ensuring undirected behavior
    
    def getEdgeTo(self, toVertex):
        for edge in self.edgeList:
            if edge.getOtherVertex(self) == toVertex:
                return edge
        return None
    
    def __hash__(self):
        return hash(self.label)
    
    def __eq__(self, other):
        return isinstance(other, LinkedVertex) and self.label == other.label

class LinkedEdge:
    
    def __init__(self, fromVertex, toVertex, weight=1):
        self.vertex1 = fromVertex
        self.vertex2 = toVertex
        self.weight = weight
    
    def getWeight(self):
        return self.weight
    
    def getOtherVertex(self, vertex):
        return self.vertex2 if self.vertex1 == vertex else self.vertex1
    
    def __lt__(self, other):
        return self.weight < other.weight
    
    def __eq__(self, other):
        return (self.vertex1, self.vertex2, self.weight) == (other.vertex1, other.vertex2, other.weight)

class LinkedDirectedGraph:
    
    def __init__(self):
        self.vertices = {}
    
    def addVertex(self, label):
        if label not in self.vertices:
            self.vertices[label] = LinkedVertex(label)
    
    def addEdge(self, fromLabel, toLabel, weight=1):
        if fromLabel not in self.vertices:
            self.addVertex(fromLabel)
        if toLabel not in self.vertices:
            self.addVertex(toLabel)
        self.vertices[fromLabel].addEdgeTo(self.vertices[toLabel], weight)
    
    def getVertex(self, label):
        return self.vertices.get(label)
    
    def containsVertex(self, label):
        return label in self.vertices
    
    def getVertices(self):
        return self.vertices.values()
    
    def size(self):
        return len(self.vertices)
    
    def clearVertexMarks(self):
        for vertex in self.vertices.values():
            vertex.clearMark()
    
    def __str__(self):
        return "\n".join(f"{v.getLabel()}: {[e.getOtherVertex(v).getLabel() for e in v.incidentEdges()]}" for v in self.vertices.values())