import numpy as np

input = np.genfromtxt('input.txt', dtype=str, delimiter='-')

graph = {}
visited = {}
for n1, n2 in input:
    if n1 in graph.keys():
        graph[n1].append(n2)
    else:
        graph[n1] = [n2]

    if n2 in graph.keys():
        graph[n2].append(n1)
    else:
        graph[n2] = [n1]

    visited[n1] = 0
    visited[n2] = 0


ans = 0
current_path = []
def DFS(u, v):
    global ans, current_path
    if visited[u]:
        return

    if u.islower():
        visited[u] = 1

    current_path.append(u)
    if u == v:
        ans += 1
        visited[u] = 0
        current_path = current_path[:-1]
        return

    for n in graph[u]:
        DFS(n, v)

    current_path = current_path[:-1]
    visited[u] = 0


DFS('start', 'end')

print(f"How many paths through this cave system are there that visit small caves at most once? {ans}")


ans = 0
current_path = []
def DFS(u, v):
    global ans, current_path
    if visited[u] and (u == 'start' or np.any(np.array(list(visited.values())) > 1)):
        return

    if u.islower():
        visited[u] += 1

    current_path.append(u)
    if u == v:
        ans += 1
        visited[u] = 0
        current_path = current_path[:-1]
        return

    for n in graph[u]:
        DFS(n, v)

    if u.islower():
        visited[u] -= 1

    current_path = current_path[:-1]


DFS('start', 'end')

print(f"Given these new rules, how many paths through this cave system are there? {ans}")
