#Michael Groff

def author():
    return 'mgroff3'

def build(sfile):
    # reads in textfile from knuth's website and creates nodes
    sfileo = open(sfile,"r")
    edge = []
    edges = []
    for l in sfileo:
        if l.strip() == "":
            edges.append(edge)
            edge = []
        if l.strip() != "":
            edge.append(l.strip())
    if (edge):
        edges.append(edge)
    return edges

def knuth():
    map = {}
    states = build("states.txt")
    for s in states:
        k = map.get(s[0])
        if not k:
            n = Node(s[0])
            n.neighbors.add(s[1])
            map[s[0]] = n
        else:
            k.neighbors.add(s[1])
        k = map.get(s[1])
        if not k:
            n = Node(s[1])
            n.neighbors.add(s[0])
            map[s[1]] = n
        else:
            k.neighbors.add(s[0])
    return map

class Node:
    def __init__(self, label):
        self.label = label
        self.neighbors = set()

class Graph:
    # literally just a dictionary mapping nodes to string labels 
    def __init__(self,nodes):
        self.nodes = nodes


if __name__=="__main__":
    k = knuth()
    States = Graph(k)
    for s in States.nodes:
        n = States.nodes.get(s)
        print n.label
        print n.neighbors
        print
