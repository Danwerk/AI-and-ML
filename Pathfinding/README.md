This project compares three pathfinding algorithms
- **Breadth-First Search**
- **Greedy Search**
- **Astar search**
The algorithms are tested on a grid-based map with obstacles, and the goal is to find a path from a starting point to an ending point.

## Algorithms

### Breadth-First Search (BFS)
BFS explores all nodes at the present "depth" level before moving on to nodes at the next depth level. It is guaranteed to find the shortest path in an unweighted grid.

### Greedy Best-First Search (Greedy)
Greedy Best-First Search uses a heuristic to estimate the cost to the goal and chooses paths that appear to be leading towards the goal most quickly. It is not guaranteed to find the shortest path.

### A* Search (A*)
A* Search combines features of BFS and Greedy. It uses a heuristic to estimate the cost to the goal and also considers the cost to reach the current node. It is guaranteed to find the shortest path if the heuristic is admissible.

## Map Format

The map is represented as a list of strings where:
- `'*'` denotes obstacles.
- `'s'` denotes the starting point.
- `'D'` denotes the ending point.
- Spaces denote walkable areas.

Here is the example map:
``` 
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
```

## Results
The results of BFS:
```
Cave300x300:
BFS: Time to find solution: 178.43 ms
BFS: Number of iterations: 47264
BFS: Length of solution in steps: 554
---------------------------------------

Cave600x600:
BFS: Time to find solution: 862.75 ms
BFS: Number of iterations: 197806
BFS: Length of solution in steps: 1247
---------------------------------------

Cave900x900:
BFS: Time to find solution: 2021.83 ms
BFS: Number of iterations: 450448
BFS: Length of solution in steps: 1843
```

The results of Greedy:
```
Cave300x300:
GREEDY: Time to find solution: 15.62 ms
GREEDY: Number of iterations: 3358
GREEDY: Length of solution in steps: 982
---------------------------------------

Cave600x600:
GREEDY: Time to find solution: 37.90 ms
GREEDY: Number of iterations: 6293
GREEDY: Length of solution in steps: 1973
---------------------------------------

Cave900x900
GREEDY: Time to find solution: 153.43 ms
GREEDY: Number of iterations: 29496
GREEDY: Length of solution in steps: 4129
```

The results of A*
``` 
Cave300x300
A*: Time to find solution: 53.11 ms
A*: Number of iterations: 8202
A*: Length of solution in steps: 554
---------------------------------------

Cave600x600
A*: Time to find solution: 316.84 ms
A*: Number of iterations: 60472
A*: Length of solution in steps: 1247
---------------------------------------

Cave900x900
A*: Time to find solution: 600.09 ms
A*: Number of iterations: 93999
A*: Length of solution in steps: 1843

```