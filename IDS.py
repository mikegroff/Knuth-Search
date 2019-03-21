#Michael Groff

import Knuth2008 as kn
from collections import deque
import time
import copy

def ids(Graph, Start, Goal, Depth):
    # to avoid redundant comments im only going to explain the differences between this and the dfs code
    max = Depth
    k = 0
    for i in range(1,max): #starting at one because a single node is a path of length zero
        v = set()
        v.add(Start)
        stack = [[Start]]
        stack = deque(stack)
        mq = len(stack)
        next = None
        while stack:
            n = stack.pop()
            k+=1
            next = n[-1]
            if next == Goal:
                break
            if len(n) == i:
                continue #not adding any paths beyong max depth to the queue
            nbh = Graph.nodes.get(next).neighbors - v
            nbh = list(nbh)
            nbh.sort()
            nbh.reverse()
            for nb in nbh:
                v.add(nb)
                np = copy.copy(n)
                np.append(nb)
                stack.append(np)
            if len(stack) > mq:
                mq = len(stack)

        if next == Goal:
            #each time the stack is cleared or the loop is broken we have either found a path or exhausted our search
            #a binary check determeines whether to
            break

    return n,k,mq

if __name__=="__main__":
    k = kn.knuth()
    States = kn.Graph(k)
    S = 'MA'
    G = 'GA'
    mq = 0
    s = time.clock()
    path,v,mq = ids(States,S,G,len(States.nodes)-1)
    e = time.clock()
    t = e - s

    print "Cumputational Time: {}".format(t)
    print
    print "Nodes visited: {}".format(v)
    print
    print "Maximum Queue size: {}".format(mq)
    print
    print "Length of Path: {}".format(len(path)-1)
    print
    print "Path Found: {}".format(path)
