import math
from chain.utils import calculate_hash

class Node:
    def __init__(self, value :int | str, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right
     
     
def is_valid_power(number_of_leaves :int) -> bool:
    return isinstance(math.log2(number_of_leaves), int)
        
def compute_tree_depth(number_of_leaves :int) -> int:
    return math.ceil(math.log2(number_of_leaves))

    
def build_merkle_tree(node_data :[str]) -> Node:
    old_nodes = [Node(calculate_hash(data)) for data in node_data]
    tree_depth = compute_tree_depth(len(old_nodes))
    for i in range(0, tree_depth):
        num_nodes = 2**(tree_depth-i)
        new_nodes = []
        for j in range(0, num_nodes, 2):
            child_node_0 = old_nodes[j]
            child_node_1 = old_nodes[j+1]
            new_node = Node(
                value = calculate_hash(f"{child_node_0.value}{child_node_1.value}"),
                left=child_node_0,
                right=child_node_1
            )
            new_nodes.append(new_node)
        old_nodes = new_nodes
    return new_nodes[0]


def fill_set(list_of_nodes) -> list[Node]:
    current_number_of_leaves = len(list_of_nodes)
    if is_valid_power(current_number_of_leaves):
        return list_of_nodes
    total_number_of_leaves = 2**compute_tree_depth(current_number_of_leaves)
    if current_number_of_leaves % 2 == 0:
        for i in range(current_number_of_leaves, total_number_of_leaves, 2):
            list_of_nodes += list_of_nodes + [list_of_nodes[-2], list_of_nodes[-1]]
    else:
        for i in range(current_number_of_leaves, total_number_of_leaves):
            list_of_nodes.append(list_of_nodes[-1])
    
    return list_of_nodes
