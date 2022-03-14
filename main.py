import collections
import json
import numpy as np


PACMAN = 3.
GHOST = 2.
WALL = 1.


def route(board, ghost):
    queue = collections.deque([[ghost]])
    seen = {ghost}
    while queue:
        path = queue.popleft()
        x, y = path[-1]

        if board[y][x] == PACMAN:
            return len(path) - 1

        for x2, y2 in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
            if 0 <= x2 < board.shape[1] and 0 <= y2 < board.shape[0] and board[y2][x2] != WALL and (x2, y2) not in seen:
                queue.append(path + [(x2, y2)])
                seen.add((x2, y2))


with open("C:/Users/glaze/Downloads/interview2/board1.npy_array.json") as f:
    data = json.load(f)

board = np.asarray(data)

ghosts = np.where(board == GHOST)
ghosts_cords = [(ghosts[0][i], ghosts[1][i]) for i in range(len(ghosts[0]))]

paths = list()
for ghost in ghosts_cords:
    paths.append((ghost, route(board, ghost)))

# sorting the paths lengths
for iter_num in range(len(paths)-1,0,-1):
    for idx in range(iter_num):
        if paths[idx][1]>paths[idx+1][1]:
            paths[idx], paths[idx+1] = paths[idx+1], paths[idx]

print(paths)
