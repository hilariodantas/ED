
from linkedstack import LinkedStack
import heapq

def topoSort(g, startLabel=None):
    stack = LinkedStack()
    g.clearVertexMarks()
    for v in g.getVertices():
        if not v.isMarked():
            dfs(g, v, stack)
    return stack

def dfs(g, v, stack):
    v.setMark()
    for w in g.neighboringVertices(v.getLabel()):
        if not w.isMarked():
            dfs(g, w, stack)
    stack.push(v)

def spanTree(g, startLabel):
    if not g.containsVertex(startLabel):
        return None
    mst = []
    visited = set()
    pq = []
    
    startVertex = g.getVertex(startLabel)
    visited.add(startVertex)
    for edge in startVertex.incidentEdges():
        heapq.heappush(pq, (edge.getWeight(), startVertex, edge.getOtherVertex(startVertex)))
    
    while pq and len(visited) < g.size():
        weight, fromVertex, toVertex = heapq.heappop(pq)
        if toVertex not in visited:
            visited.add(toVertex)
            mst.append((fromVertex.getLabel(), toVertex.getLabel(), weight))
            for edge in toVertex.incidentEdges():
                if edge.getOtherVertex(toVertex) not in visited:
                    heapq.heappush(pq, (edge.getWeight(), toVertex, edge.getOtherVertex(toVertex)))
    return mst

def shortestPaths(g, startLabel):
    if not g.containsVertex(startLabel):
        return None
    
    distances = {v: float('inf') for v in g.getVertices()}
    distances[startLabel] = 0
    predecessors = {v: None for v in g.getVertices()}
    pq = [(0, g.getVertex(startLabel))]
    
    while pq:
        currentDist, currentVertex = heapq.heappop(pq)
        if currentDist > distances[currentVertex.getLabel()]:
            continue
        for edge in currentVertex.incidentEdges():
            neighbor = edge.getOtherVertex(currentVertex)
            newDist = currentDist + edge.getWeight()
            if newDist < distances[neighbor.getLabel()]:
                distances[neighbor.getLabel()] = newDist
                predecessors[neighbor.getLabel()] = currentVertex.getLabel()
                heapq.heappush(pq, (newDist, neighbor))
    
    return {v.getLabel(): (distances[v.getLabel()], predecessors[v.getLabel()]) for v in g.getVertices()}
