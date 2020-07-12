from math import inf

graph = {'a': {'b': 10, 'c': 3}, 'b': {'c': 1, 'd': 2}, 'c': {
    'b': 4, 'd': 8, 'e': 2}, 'd': {'e': 7}, 'e': {'d': 9}}


def dijkstra(graph, start, goal):
    shortest_distance = {}
    predecessor = {}
    unvisited = graph
    infinity = inf
    path = []
    for node in unvisited:
        shortest_distance[node] = infinity
    shortest_distance[start] = 0

    while unvisited:
        minNode = None
        for node in unvisited:
            if minNode is None:
                minNode = node
            elif shortest_distance[node] < shortest_distance[minNode]:
                minNode = node

        for childNode, weight in graph[minNode].items():
            if weight + shortest_distance[minNode] < shortest_distance[childNode]:
                shortest_distance[childNode] = weight + \
                    shortest_distance[minNode]
                predecessor[childNode] = minNode
        unvisited.pop(minNode)

    currentNode = goal
    while currentNode != start:
        try:
            path.insert(0, currentNode)
            currentNode = predecessor[currentNode]
        except KeyError:
            print('Path not reachable')
            break
    path.insert(0, start)
    if shortest_distance[goal] != infinity:
        print('Shortest distance is ' + str(shortest_distance[goal]))
        print('And the path is ' + str(path))


dijkstra(graph, 'a', 'b')
