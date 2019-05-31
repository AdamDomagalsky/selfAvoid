def FindWalk(
        walks,
        current_walk,
        current_x,
        current_y,
        side,
        pathLength,
        visited):
    # If we have visited every position,
    # then this is a complete walk.
    if (len(current_walk) == pathLength + 1):
        walks.append(current_walk)
        print(walks)
    else:
        next_points = [
            [current_x - 1, current_y],
            [current_x + 1, current_y],
            [current_x, current_y - 1],
            [current_x, current_y + 1]
        ]

        for point in next_points:
            x, y = point[0], point[1]

            if (x < 0): continue
            if (x > side): continue
            if (y < 0): continue
            if (y > side): continue

            if (visited[x][y]): continue

            # Try visiting this point.
            visited[x][y] = True
            current_walk.append(point)

            return FindWalk(walks, current_walk,
                     x, y, side, pathLength, visited)

            # We're done visiting this point.
            visited[x][y] = False
            current_walk.pop()



def initWalker(pathLength):
    # Start the walk at (0, 0).
    current_walk = []
    current_walk.append([0, 0])
    walks = []
    side = pathLength + 1
    visited = [[False] * side] * side

    visited[0][0] = True

    FindWalk(walks, current_walk, 0, 0, side, pathLength, visited)

    return walks


p1 = initWalker(15)
