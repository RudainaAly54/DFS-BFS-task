# DFS-BFS-task
#That program finds the traversal (visited order) of graph by BFS &DFS
the start is 'A' & the goal is 'G' 
#create a dictionary which is our graph 
# firstly creates a dfs function
in the function initialize an empty set caleed visited to keep track of visited node the mark the current node as visited the make a loop for neighbour node and a condition to check if neighbour node visited or not then call the dfs function to reapet 
# secondly create a bfs function 
in the function initialize an empty set to keep track of visited node & create a queue for bfs make a loop to to dequeue(remove) the first node from the node then add it to another one (vertex)  then make a condition to check if vertex visitied or not then mark it as visited then enqueue unvisited neighbours
#output 
DFS traversal 
A B H F T C E D G 
BFS traversal
A B T H C E F D G 
