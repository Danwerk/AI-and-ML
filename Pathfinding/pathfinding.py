import queue
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
    came_from = {}
    came_from[start_coords] = None

    while not frontier.empty():
        current = frontier.get()

        # If diamond reached then end searching and current is our search result
        if current == end_coords:
            break
        print(current)
        row, col = current

        neighbors = [(row, col + 1), (row, col - 1), (row + 1, col), (row - 1, col)]
        print(neighbors)
        for move_row, move_col in neighbors:

            if can_move(lava_map, move_row, move_col) and (move_row, move_col) not in came_from:
                frontier.put((move_row, move_col))
                came_from[(move_row, move_col)] = current



if __name__ == '__main__':
    bfs(lava_map1)
