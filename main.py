from collections import deque
from heapq import heappush, heappop 

def shortest_shortest_path(graph, source):
    """
    Params: 
      graph.....a graph represented as a dict where each key is a vertex
                and the value is a set of (vertex, weight) tuples (as in the test case)
      source....the source node
      
    Returns:
      a dict where each key is a vertex and the value is a tuple of
      (shortest path weight, shortest path number of edges). See test case for example.
    """
    ### TODO
    
    #initialize variables
    distances = {vertex: (float('inf'), float('inf')) for vertex in graph}
    paths = {vertex: [] for vertex in graph} #we want to store all paths in a single place
    
    #we want to have a single starting vertex to compute paths so we initialize it
    distances[source] = (0,0)
    paths[source] = [source]
    
    #we want to create a queue of all verticies we want to visit and as we visit them, pop them 
    #off so we do not revisit them
    queue = [source]
    while queue:
        #now we want to find the shortest distance from a vertex to the queue
        vertex = min(queue, key=lambda v: distances[v])
        queue.remove(vertex)
        
    for neighbor, weight in graph[vertex]: 
        #want to compute the distances and paths of adjacent verticesm so we go over all possibilities 
        if distances[neighbor][0] > distances[vertex][0] + weight:
            distances[neighbor] = (distances[vertex][0] + weight, distances[vertex][1] +1)
            paths[neighbor] = paths[vertex] + [neighbor]
        elif distances[neighbor][0] == distances[vertex][0] + weight:
            if distances[neighbor][1] > distances[vertex][1] + 1:
                distances[neighbor] = (distances[vertex][0] + weight, distances[vertex][1] +1)
                paths[neighbor] = paths[vertex] + [neighbor]
                if neighbor not in queue:
                    queue.append(neighbor)
    #then we want to return all of the distances between the starting vertext and adjacent vertices that we computed
    return distances
            
    pass
    
def test_shortest_shortest_path():

    graph = {
                's': {('a', 1), ('c', 4)},
                'a': {('b', 2)}, # 'a': {'b'},
                'b': {('c', 1), ('d', 4)}, 
                'c': {('d', 3)},
                'd': {},
                'e': {('d', 0)}
            }
    result = shortest_shortest_path(graph, 's')
    # result has both the weight and number of edges in the shortest shortest path
    assert result['s'] == (0,0)
    assert result['a'] == (1,1)
    assert result['b'] == (3,2)
    assert result['c'] == (4,1)
    assert result['d'] == (7,2)
    
    
def bfs_path(graph, source):
    """
    Returns:
      a dict where each key is a vertex and the value is the parent of 
      that vertex in the shortest path tree.
    """
    ###TODO
    #want to initialize a parent dictionary to use
    parents = {vertex: None for vertex in graph}
    
    #want the starting vertex of dict to point to itself
    parents[source] = source
    
    #like before we want to create a queue of vertices to visit
    #want to pop off every node that we visit and add vertices not in the queue to it
    queue = [source]
    while queue:
        vertex = queue.pop(0)
    #we want to update the parent of the adjacent vertices
    for neighbor in graph[vertex]:
        if parents[neighbor] is None: #if the adjacent vertex is not in our queue to visit
            parents[neighbor] = vertex
            queue.append(neighbor)
            
    return parents
    pass

def get_sample_graph():
     return {'s': {'a', 'b'},
            'a': {'b'},
            'b': {'c'},
            'c': {'a', 'd'},
            'd': {}
            }

def test_bfs_path():
    graph = get_sample_graph()
    parents = bfs_path(graph, 's')
    assert parents['a'] == 's'
    assert parents['b'] == 's'    
    assert parents['c'] == 'b'
    assert parents['d'] == 'c'
    
def get_path(parents, destination):
    """
    Returns:
      The shortest path from the source node to this destination node 
      (excluding the destination node itself). See test_get_path for an example.
    """
    ###TODO
    
    #initalize array for path
    path = []
    for i in parents:
        if i != parents[i]:
            #we only want to record vertices in the path we are interested in looking at 
            if parents[i] in path:
                continue
            else: #add it to path if it is not already in the array
                path.append(parents[i])
        elif i == destination:
            path.append(parents[i])
            break
        else:
            continue 
        return (''.join(list((path)))) #we want to return the full path 
    
    graph = get_sample_graph()
    parents = bfs_path(graph, 's')
    get_path(parents, 'd')
    pass

def test_get_path():
    graph = get_sample_graph()
    parents = bfs_path(graph, 's')
    assert get_path(parents, 'd') == 'sbc'
