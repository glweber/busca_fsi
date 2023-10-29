import heapq  # Standard Python library providing a binary heap-based priority queue.
from collections import deque
from typing import Tuple, List

import networkx as nx


def bfs(graph, start_node, goal_node):
    """
    Find the shortest path between the start and goal nodes using the breadth-first search algorithm.

    Args:
        graph (nx.Graph): Graph to be traversed.
        start_node (int): Start node.
        goal_node (int): Goal node.

    Returns:
        List[int]: List containing the shortest path between the start and goal nodes.
    """
    queue = deque([start_node])
    visited = set()
    path = {}
    path[start_node] = None

    while queue:
        node = queue.popleft()
        if node == goal_node:
            break
        visited.add(node)
        for neighbor in graph.neighbors(node):
            if neighbor not in visited and graph[node][neighbor]['cost'] > 0:
                queue.append(neighbor)
                visited.add(neighbor)
                path[neighbor] = node

    shortest_path = []
    node = goal_node
    while node is not None:
        shortest_path.append(node)
        node = path[node]
    shortest_path.reverse()

    return shortest_path


def dfs(graph, start_node, goal_node):
    """
    Find the shortest path between the start and goal nodes using the depth-first search algorithm.

    Args:
        graph (nx.Graph): Graph to be traversed.
        start_node (int): Start node.
        goal_node (int): Goal node.

    Returns:
        List[int]: List containing the shortest path between the start and goal nodes.
    """
    stack = [(start_node, [start_node])]
    visited = set()

    while stack:
        (node, path) = stack.pop()
        if node == goal_node:
            return path
        visited.add(node)
        for neighbor in graph.neighbors(node):
            if neighbor not in visited and graph[node][neighbor]['cost'] > 0:
                stack.append((neighbor, path + [neighbor]))

    return None


def astar_search(graph, start, goal):
    """
    Execute the A* algorithm to find the shortest path in the graph.

    Args:
        graph (nx.Graph): The graph in which the algorithm should be executed.
        start (int): The starting node of the path.
        goal (int): The destination node of the path.

    Returns:
        Tuple[float, List[int]]: A tuple containing the length of the shortest path and a list of nodes in the path.
    """
    heap = [(0, start)]
    shortest_path_costs = {start: 0}
    parents = {start: None}

    while heap:
        (cost, node) = heapq.heappop(heap)
        if node == goal:
            break
        for neighbor in graph.neighbors(node):
            edge_cost = graph[node][neighbor]['cost']
            neighbor_cost = shortest_path_costs[node] + edge_cost
            if neighbor not in shortest_path_costs or neighbor_cost < shortest_path_costs[neighbor]:
                shortest_path_costs[neighbor] = neighbor_cost
                heuristic_cost = graph.nodes[neighbor].get('time_discount', 0)
                total_cost = neighbor_cost + heuristic_cost
                heapq.heappush(heap, (total_cost, neighbor))
                parents[neighbor] = node

    if goal in parents:
        path = [goal]
        node = goal
        while parents[node] is not None:
            path.append(parents[node])
            node = parents[node]
        path.reverse()
        return shortest_path_costs[goal], path


def greedy_search(graph, start, goal):
    """
    Perform a greedy search in the graph.

    Args:
        graph (nx.Graph): Graph to be traversed.
        start (int): Start node.
        goal (int): Goal node.

    Returns:
        List[int]: List containing the nodes visited during the search.
        float: Total cost of the path.
    """
    visited = []
    frontier = [(start, 0)]

    while frontier:
        node, path_cost = min(frontier, key=lambda x: min_path_heuristic(graph, x[0], goal))
        frontier.remove((node, path_cost))
        if node == goal:
            return visited + [node], path_cost
        visited.append(node)

        for neighbor in graph.neighbors(node):
            if neighbor not in visited:
                cost = graph[node][neighbor]['distance'] + graph.nodes[neighbor].get('time_discount', 0)
                frontier.append((neighbor, path_cost + cost))

    return None


def min_path_heuristic(graph, node, goal):
    """
    Heuristic function that estimates the minimum path length between a node and the goal node.

    Args:
        graph (nx.Graph): Graph to be traversed.
        node (int): The current node.
        goal (int): The goal node.

    Returns:
        float: The estimated minimum path length.
    """
    try:
        path = nx.shortest_path(graph, node, goal, weight='distance')
        return path_length(graph, path) + graph.nodes[node].get('time_discount', 0)
    except nx.NetworkXNoPath:
        return float('inf')


def path_length(graph, path):
    """
    Calculate the total cost of a path.

    Args:
        graph (nx.Graph): Graph to be traversed.
        path (List[int]): List of nodes in the path.

    Returns:
        float: The total cost of the path.
    """
    length = 0
    for i in range(len(path) - 1):
        length += graph[path[i]][path[i + 1]]['cost']
    return length
