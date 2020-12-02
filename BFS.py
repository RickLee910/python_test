from pythonds.graphs import Graph, Vertex
from pythonds.basic import Queue
def bfs(g, start):
    start.setDistance(0)
    start.setPred(None)
    verQueue = Queue()
    verQueue.enqueue(start)
    while(verQueue.size() > 0):
        currentVert = verQueue.dequeue()
        for nbr in currentVert.getConnections():
            if nbr.getColor() == 'white':
                nbr.setColor('gray')
                nbr.setDistance(currentVert.getDistance() + 1)
                nbr.setPred(currentVert)
                verQueue.enqueue(nbr)
            currentVert.setColor('black')