def hasPathDFS(graph, src, dst, visited):
    if src==dst:
        return True
    visited.add(src)
    for nei in graph[src]:
        if nei not in visited:
            if hasPathDFS(graph, nei, dst, visited):
                return True
    return False