All you should need to do to run each file is python _.py and maybe: set PYTHONPATH=%PYTHONPATH%;..;. depedning on the machien you use to run it
Ive only imported basic libriaries such as collections,time,and copy so python 2 or 3 should be fine
Knuth2008 simply constructs the graph so as long as its in the same directory as the other files they can call/import it
states.txt holds the data from his website of all the edges

Ive added the extra file dbs.py which is my version of ids which does not repeat nodes visited,
instead it loads all possible paths into the front of the stack so that dfs is performed all the way to max depth,
then max depth is increased and it begins to pop out all the partial paths longer than that depth but shorter than 
the new max depth, if run with a value of 1 it behaves like bfs, however with larger steps its more of a mix between dfs and bfs 
perfroming dfs on chuncks of levels in the graph in a bfs fashion 
you can ignore it if you want i just coded it to see how well it would work 
