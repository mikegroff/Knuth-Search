#Michael Groff

import Knuth2008 as kn
from collections import deque
import time
import copy


def bfs(Graph, Start, Goal):
    #this is almost exactly the same as the dfs code except now we pop from the head of the stack
    v = set()
    v.add(Start)
    k = 0
    stack = [[Start]]
    stack = deque(stack) #this is the queue
    mq = len(stack) #mq keeps track of largest size of stack
    next = None
    while stack: # keeps running while thre are paths to consider
        n = stack.popleft()
        k+=1 #number of times we deque
        next = n[-1]
        #print next
        if next == Goal: #checks the node for the goal every time a path is popped
            break
        nbh = Graph.nodes.get(next).neighbors - v #using set differences
        nbh = list(nbh)
        nbh.sort() #placing in alphabetical order so that paths are popped off stack accordingly
        #nbh.reverse()
        for nb in nbh:
            v.add(nb)  #visited list that only keeps tracks of nodes that have been added to queue
            np = copy.copy(n)
            np.append(nb) # generating path
            stack.append(np) # adding to stack
        if len(stack) > mq:
            mq = len(stack) # adjust max queue size

    return n,k,mq

if __name__=="__main__":
    k = kn.knuth()
    States = kn.Graph(k)
    S = 'MA'
    G = 'GA'
    mq = 0
    s = time.clock()
    path,v,mq = bfs(States,S,G)
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
