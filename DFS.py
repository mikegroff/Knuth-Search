#Michael Groff

import Knuth2008 as kn
from collections import deque
import time
import copy


def dfs(Graph, Start, Goal):
    v = set()
    v.add(Start)
    k = 0
    stack = [[Start]]
    stack = deque(stack) #this is the queue
    mq = len(stack) #mq keeps track of largest size of stack
    next = None
    while stack: # keeps running while thre are paths to consider
        #print stack
        n = stack.pop()
        k+=1
        next = n[-1]
        #print next
        if next == Goal: #checks the node for the goal every time a path is popped
            break
        nbh = Graph.nodes.get(next).neighbors - v #using set differences
        nbh = list(nbh)
        nbh.sort()
        nbh.reverse() #placing in reverse alphabetical order so that paths are popped off stack accordingly
        for nb in nbh:
            v.add(nb) #visited list that only keeps tracks of nodes that have been added to queue
            np = copy.copy(n)
            np.append(nb) # generating path
            stack.append(np) # adding to stack
        if len(stack) > mq:
            mq = len(stack) # adjust max queue size

    return n,k,mq

if __name__=="__main__":
    k = kn.knuth()
    States = kn.Graph(k) #generating graph from Knuth2008
    S = 'MA'
    G = 'GA'
    mq = 0
    s = time.clock()
    path,v,mq = dfs(States,S,G)
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
