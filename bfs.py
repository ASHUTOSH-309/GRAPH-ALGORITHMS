from queue import Queue

def bfs(start_node,total_nodes,graph):

    visited=[0]*total_nodes
    visited[start_node]=True
    ans_list=[]


    queue=Queue()
    queue.put(start_node)

    while(queue.qsize()):
          node=queue.get()
          ans_list.append(node)
          for it in graph[node] :
               if(visited[it]==0):
                    visited[it]=True
                    queue.put(it)

    return ans_list

graph={
     0:[1,2,3,4],
     1:[3,5,7,9],
     2:[4,7,5,8],
     3:[2],
     4:[6,7,2,3],
     5:[1,2,3,4],
     6:[4],
     7:[1,2],
     8:[2],
     9:[1]
}

total_nodes=len(graph)
start_node=0
ans=bfs(start_node,total_nodes,graph)

for each_elem in ans :
     print(each_elem, end='\t') 
                  







    




    
      

    

