#Michael Groff

import Knuth2008 as kn
from collections import deque
import time
import copy

def ids(Graph, Start, Goal, Depth):
    # to avoid redundant comments im only going to explain the differences between this and the dfs code
    max = Depth # this is out depth that we perfrom dfs chose 5 because of the path lengths other algrothims returned
    v = set()
    v.add(Start)
    k = 0
    stack = [[Start]]
    stack = deque(stack)
    mq = len(stack)
    next = None
    while stack:
        n = stack.pop()
        k+=1
        if len(n) > max:
            max += Depth #once we reach our first path thats longer than max depth we increaseexit

        next = n[-1]
        if next == Goal:
            break

        nbh = Graph.nodes.get(next).neighbors - v
        nbh = list(nbh)
        nbh.sort()
        if len(n) != max:
            nbh.reverse() # at max depth we add to the front of the queue so reverse order isnt needed
        for nb in nbh:
            v.add(nb)
            np = copy.copy(n)
            np.append(nb)
            if len(n) == max:
                # to preserve the lifo property of the stack we simply add every path that would be above max depth to the head of the list
                # they will be popped after every path of max depth has been examined
                stack.appendleft(np)
            else:
                stack.append(np)
        if len(stack) > mq:
            mq = len(stack)

    return n,k,mq

if __name__=="__main__":
    k = kn.knuth()
    States = kn.Graph(k)
    S = 'MA'
    G = 'GA'
    mq = 0
    s = time.clock()
    path,v,mq = ids(States,S,G,5)
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
