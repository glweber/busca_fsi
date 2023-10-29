import random
import networkx as nx

def generate_rally_map(num_nodes: int, num_discounted_nodes: int, discount_ratio: float, max_connections: int) -> nx.Graph:
    """
    Generates a graph representing a rally map with time discounts at randomly selected checkpoints.

    Args:
        num_nodes (int): the number of nodes in the graph.
        num_discounted_nodes (int): the number of checkpoints with time discounts.
        discount_ratio (float): the proportion of time discount for each checkpoint.
        max_connections (int): the maximum number of connections each node can have.

    Returns:
        nx.Graph: the generated graph object.
    """
    # Initializing a NetworkX graph object
    graph = nx.Graph()

    # Defining the cost for each type of terrain
    terrain_costs = {
        'Solid': 1,
        'Rocky': 10,
        'Sandy': 4,
        'Swampy': 20
    }

    # Adding nodes to the graph
    for i in range(1, num_nodes + 1):
        graph.add_node(i)

    # Creating a list of all nodes in the graph
    nodes = list(graph.nodes())

    # Adding edges to the graph with random costs and distances
    for i in range(len(nodes)):
        # Selecting a random number of connections for the node
        num_connections = random.randint(1, max_connections)
        # Randomly selecting destination nodes for the connections
        destination_nodes = random.sample(nodes[:i] + nodes[i + 1:], num_connections)
        # Adding edges with random costs and distances
        for node in destination_nodes:
            cost = terrain_costs[random.choice(list(terrain_costs.keys()))]
            distance = abs(node - nodes[i])
            graph.add_edge(nodes[i], node, cost=cost, distance=distance)

    # Randomly selecting checkpoints with time discounts
    discounted_nodes = random.sample(range(1, num_nodes + 1), num_discounted_nodes)

    # Assigning time discounts for each checkpoint based on the terrain cost
    for node in discounted_nodes:
        terrain_cost = terrain_costs[random.choice(list(terrain_costs.keys()))]
        time_discount = int(terrain_cost * discount_ratio)
        graph.nodes[node]['time_discount'] = time_discount

    return graph
