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
        node = frontier.pop(0)  # queue behavior

        if goal_test(node.state):
            return get_path(node)

        explored.add(node.state)

        for child_state in get_children(node.state):
            if child_state not in explored and all(n.state != child_state for n in frontier):
                frontier.append(Node(child_state, node))

    return None


def goal_test(state):
    return state=='g'


def get_children(state):
    return graph[state]


if __name__ == "__main__":
    graph = {
        's':['A', 'B'],
        'A':['s', 'C'],
        'B':['s', 'D'],
        'C':['A', 'E'],
        'D':['B', 'E', 'F'],
        'E':['C', 'D', 'G'],
        'F':['D', 'H'],
        'G':['E', 'I'],
        'H':['F', 'I', 'J'],
        'I':['G', 'H', 'K'],
        'J':['H', 'L'],
        'K':['I', 'g'],
        'L':['J', 'g'],
        'g':['K', 'L'],
    }

    result=BFS('s', goal_test, get_children)
    print(result)