class Node:
    def __init__(self, state, parent=None):
        self.state = state
        self.parent = parent


def get_path(node):
    path = []
    while node:
        path.append(node.state)
        node = node.parent
    return path[::-1]


def BFS(initial_state, goal_test, get_children):
    frontier = [Node(initial_state)]
    explored = set()

    while frontier:
        node = frontier.pop(0)   # queue behavior

        if goal_test(node.state):
            return get_path(node)

        explored.add(node.state)

        for child_state in get_children(node.state):
            if child_state not in explored and all(n.state != child_state for n in frontier):
                frontier.append(Node(child_state, node))

    return None

def goal_test(state):
    return state == 'D'

def get_children(state):
    return graph[state]

if __name__ == "__main__":
    graph = {
        'A': ['B', 'E', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['F', 'G', 'A'],
        'D': ['B', 'E'],
        'E': ['A', 'B', 'D'],
        'F': ['C'],
        'G': ['C']
    }
    result = BFS('D', goal_test,get_children)
    print(result)