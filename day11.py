from collections import deque

def toposort(graph):
    indegree={node:0 for node in graph}
    for node in graph:
        for nei in graph[node]:
            indegree[nei]+=1

    queue=([node for node in graph if indegree[node]==0])
    result=[]
    while queue:
        node=queue.popleft()
        result.append(node)
        for nei in graph[node]:
            indegree[nei]-=1
            if indegree[nei]==0:
                queue.append(nei)
    return result if len(result)==len(graph)else[]