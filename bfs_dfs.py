from collections import deque

def dfs_matrix(graph, start, visited, locations):
    print(locations[start], end=" ")
    visited[start] = True
    for i in range(len(graph[start])):
        if graph[start][i] == 1 and not visited[i]:
            dfs_matrix(graph, i, visited, locations)

def bfs_list(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)

    while queue:
        node = queue.popleft()
        print(node, end=" ")
        for neighbour in graph[node]:
            if neighbour not in visited:
                queue.append(neighbour)
                visited.add(neighbour)

def main():
    n = int(input("Enter number of locations (nodes): "))

    print("\nEnter location names (like A, B, C, ...):")
    locations = []
    for i in range(n):
        loc = input(f"Location {i+1}: ").upper()
        locations.append(loc)

    print("\nEnter adjacency matrix (0 or 1):")
    matrix = []
    for i in range(n):
        row = list(map(int, input(f"Row {i+1}: ").split()))
        matrix.append(row)

    graph = {}
    print("\nEnter adjacency list connections:")
    for loc in locations:
        neighbors = input(f"Enter connected locations for {loc} (space separated): ").upper().split()
        graph[loc] = neighbors

    while True:
        print("\n========= GRAPH TRAVERSAL MENU =========")
        print("1. BFS Traversal (Adjacency List)")
        print("2. DFS Traversal (Adjacency Matrix)")
        print("3. Exit")
        ch = int(input("Enter your choice: "))

        if ch == 1:
            start = input("Enter starting location for BFS: ").upper()
            print("BFS Traversal Order:")
            bfs_list(graph, start)
            print()

        elif ch == 2:
            start = input("Enter starting location for DFS: ").upper()
            start_index = locations.index(start)
            visited = [False] * n
            print("DFS Traversal Order:")
            dfs_matrix(matrix, start_index, visited, locations)
            print()

        elif ch == 3:
            print("Exiting Program...")
            break

        else:
            print("Invalid choice! Try again.")

main()
