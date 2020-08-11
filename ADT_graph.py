class Vertax:
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}

    def addNeighbor(self, nbr, weight=0):
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id) + 'connectionTo: ' \
                + str([x.id for x in self.connectedTo])

    def getconnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self, nbr):
        return self.connectedTo[nbr]

class Graph:
    def __init__(self):
        self.verList = {}
        self.numVertices = 0

    def addVertax(self, key):
        self.numVertices += 1
        newVertax = Vertax(key)
        self.verList[key] = newVertax
        return newVertax

    def getVertax(self, n):
        if n in self.verList:
            return self.verList[n]
        else:
            return None

    def __contains__(self, n): #判断一个定点是否在里面
        return n in self.verList

    def addEdge(self, f, t, cost = 0):
        if f not in self.verList(f):
            nv = self.verList(f)
        if t not in self.verList(t):
            nv = self.verList(t)

    def getVertices(self):
        return self.verList.keys()

    def __iter__(self):
        return iter(self.verList.values())

g= Graph()
for i in range(6):
    g.addVertax(i)

print(g.verList)