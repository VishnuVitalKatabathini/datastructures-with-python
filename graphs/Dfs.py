def dfs(graph, node):
    if node not in visited:
        visited.add(node)
        print('visited nodes :',visited)
        for i in graph[node]:
            dfs(graph,i)


visited=set()
graph={'A':['B','C','F'],
       'B':['A','C','D'],
       'C':['A','B','F'],
       'D':['B',],
       'F':['A','C']}
dfs(graph,'A')

