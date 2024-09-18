import queue
import time

STARTING_POINT = 's'
ENDING_POINT = 'D'

lava_map1 = [
    "      **               **      ",
    "     ***     D        ***      ",
    "     ***                       ",
    "                      *****    ",
    "           ****      ********  ",
    "           ***          *******",
    " **                      ******",
    "*****             ****     *** ",
    "*****              **          ",
    "***                            ",
    "              **         ******",
    "**            ***       *******",
    "***                      ***** ",
    "                               ",
    "                s              ",
]

lava_map2 = [
    "     **********************    ",
    "   *******   D    **********   ",
    "   *******                     ",
    " ****************    **********",
    "***********          ********  ",
    "            *******************",
    " ********    ******************",
    "********                   ****",
    "*****       ************       ",
    "***               *********    ",
    "*      ******      ************",
    "*****************       *******",
    "***      ****            ***** ",
    "                               ",
    "                s              ",
]


def reconstruct_path(came_from, start, end):
    """Reconstructs the path from start to end by following the came_from dictionary."""
    current = end
    path = []
    while current != start:  # Traverse back from the end to the start
        path.append(current)
        current = came_from[current]
    path.append(start)  # Don't forget to add the start position
    path.reverse()  # We reversed the path so it's from start to end
    return path


def heuristic(goal: tuple, next: tuple):
    # Manhattan distance on a square grid
    return abs(goal[0] - next[0]) + abs(goal[1] - next[1])


# Function that calculates the location of provided character. In our case we have start and end points.
def get_char_on_lava_map(char, lava_map):
    for i in range(len(lava_map)):
        for j in range(len(lava_map[i])):
            if lava_map[i][j] == char:
                # i is row and j is column
                return i, j
    return 0


def can_move(lava_map, row, col):
    # len(lava_map) is the the vertical length
    map_row_size = len(lava_map)
    map_col_size = len(lava_map[0])

    # - 1 because len gives length of list but indexing starts from 0
    if 0 <= row <= map_row_size - 1 and 0 <= col <= map_col_size - 1 and lava_map[row][col] != "*":
        return True
    else:
        return False


def bfs(lava_map):
    start_coords = get_char_on_lava_map(STARTING_POINT, lava_map)
    end_coords = get_char_on_lava_map(ENDING_POINT, lava_map)

    frontier = queue.Queue()

    frontier.put(start_coords)
    came_from = dict()
    came_from[start_coords] = None

    start_time = time.time()
    iterations = 0

    while not frontier.empty():
        iterations += 1
        current = frontier.get()

        # If diamond reached then end searching and current is our search result
        if current == end_coords:
            break
        row, col = current

        neighbors = [(row, col + 1), (row, col - 1), (row + 1, col), (row - 1, col)]
        for move_row, move_col in neighbors:

            if can_move(lava_map, move_row, move_col) and (move_row, move_col) not in came_from:
                frontier.put((move_row, move_col))
                came_from[(move_row, move_col)] = current

    path = reconstruct_path(came_from, start_coords, end_coords)
    end_time = time.time()
    result_time = (end_time - start_time) * 1000
    # Number of steps from start to end
    path_length = len(path) - 1

    print(f"BFS: Time to find solution: {result_time:.2f} ms")
    print(f"BFS: Number of iterations: {iterations}")
    print(f"BFS: Length of solution in steps: {path_length}")


def greedy(lava_map):
    start_coords = get_char_on_lava_map(STARTING_POINT, lava_map)
    end_coords = get_char_on_lava_map(ENDING_POINT, lava_map)

    frontier = queue.PriorityQueue()
    frontier.put((0, start_coords))
    came_from = dict()
    came_from[start_coords] = None

    # Measure the time and iterations
    start_time = time.time()
    iterations = 0

    while not frontier.empty():
        iterations += 1
        current = frontier.get()[1]

        # If diamond reached then end searching and current is our search result
        if current == end_coords:
            break
        row, col = current

        neighbors = [(row, col + 1), (row, col - 1), (row + 1, col), (row - 1, col)]
        for move_row, move_col in neighbors:

            if can_move(lava_map, move_row, move_col) and (move_row, move_col) not in came_from:
                priority = heuristic(end_coords, (move_row, move_col))
                frontier.put((priority, (move_row, move_col)))
                came_from[(move_row, move_col)] = current

    path = reconstruct_path(came_from, start_coords, end_coords)
    end_time = time.time()
    result_time = (end_time - start_time) * 1000
    # Number of steps from start to end
    path_length = len(path) - 1

    print(f"GREEDY: Time to find solution: {result_time:.2f} ms")
    print(f"GREEDY: Number of iterations: {iterations}")
    print(f"GREEDY: Length of solution in steps: {path_length}")


def a_star(lava_map):
    start_coords = get_char_on_lava_map(STARTING_POINT, lava_map)
    end_coords = get_char_on_lava_map(ENDING_POINT, lava_map)

    frontier = queue.PriorityQueue()
    frontier.put((0, start_coords))
    came_from = dict()
    came_from[start_coords] = None
    cost_so_far = dict()
    cost_so_far[start_coords] = 0

    # Measure the time and iterations
    start_time = time.time()
    iterations = 0

    while not frontier.empty():
        iterations += 1
        current = frontier.get()[1]

        # If diamond reached then end searching and current is our search result
        if current == end_coords:
            break
        row, col = current

        neighbors = [(row, col + 1), (row, col - 1), (row + 1, col), (row - 1, col)]
        for move_row, move_col in neighbors:
            new_cost = cost_so_far[current] + 1

            if can_move(lava_map, move_row, move_col) and (
                    (move_row, move_col) not in cost_so_far or new_cost < cost_so_far[(move_row, move_col)]):
                cost_so_far[(move_row, move_col)] = new_cost
                priority = heuristic(end_coords, (move_row, move_col)) + new_cost
                frontier.put((priority, (move_row, move_col)))
                came_from[(move_row, move_col)] = current

    path = reconstruct_path(came_from, start_coords, end_coords)
    end_time = time.time()
    result_time = (end_time - start_time) * 1000
    # Number of steps from start to end
    path_length = len(path) - 1

    print(f"A*: Time to find solution: {result_time:.2f} ms")
    print(f"A*: Number of iterations: {iterations}")
    print(f"A*: Length of solution in steps: {path_length}")
    # print_path(lava_map, path)


def print_path(lava_map, path):
    # Convert the map into a list of lists so we can modify it
    map_copy = [list(row) for row in lava_map]

    # Go through the path and replace the characters with '.'
    for row, col in path[1:-1]:  # Exclude start and end points
        map_copy[row][col] = '.'

    # Convert the map back to string rows and print the map
    for row in map_copy:
        print(''.join(row))


if __name__ == '__main__':
    with open("cave900x900") as f:
        map_data = [l.strip() for l in f.readlines() if len(l) > 1]
    # bfs(map_data)
    # greedy(map_data)
    a_star(map_data)
