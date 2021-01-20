from collections import deque


class MyNode:

    def __init__(self, row, col, toRemove, matrix, prevNode):
        self.row = row
        self.col = col
        self.toRemove = toRemove
        self.matrix = matrix
        self.prevNode = prevNode

    def __key(self):
        return (self.row, self.col, self.toRemove)

    def __hash__(self):
        return hash(self.__key())

    def __eq__(self, other):
        # this was a surprisingly big hang up, we need to also consider whether the remove wall has been used or not in comparison
        return (isinstance(other, type(self))
                and (self.row, self.col, self.toRemove) ==
                    (other.row, other.col, other.toRemove))

    def getNeighbours(self):
        neighbours = []
        row = self.row
        col = self.col
        matrix = self.matrix
        toRemove = self.toRemove
        prevNode = self.prevNode
        rows = len(matrix)
        cols = len(matrix[0])

        # Can't move diagonally so we only (try to) add neighbours above/below/beside this MyNode
        # Neighbour beside to the right
        if col < cols - 1:
            # check if the target neighbour is the node that this node was added from
            if not (prevNode.row == row and prevNode.col == col+1):
                # check if wall
                isWall = matrix[row][col+1] == 1
                if isWall:
                    if toRemove > 0:
                        # decrement toRemove for the neighbour MyNode as we are using up the wall removal in this iteration
                        neighbours.append(
                            MyNode(row, col + 1, 0, matrix, self))
                else:
                    neighbours.append(
                        MyNode(row, col + 1, toRemove, matrix, self))

        # Neighbour beside to the left
        if col > 0:
            if not (prevNode.row == row and prevNode.col == col-1):
                isWall = matrix[row][col-1] == 1
                if isWall:
                    if toRemove > 0:
                        neighbours.append(
                            MyNode(row, col - 1, 0, matrix, self))
                else:
                    neighbours.append(
                        MyNode(row, col - 1, toRemove, matrix, self))

        # Neighbour above
        if row > 0:
            if not (prevNode.row == row-1 and prevNode.col == col):
                isWall = matrix[row - 1][col] == 1
                if isWall:
                    if toRemove > 0:
                        neighbours.append(
                            MyNode(row - 1, col, 0, matrix, self))
                else:
                    neighbours.append(
                        MyNode(row - 1, col, toRemove, matrix, self))

        # Neighbour below
        if row < rows - 1:
            if not (prevNode.row == row+1 and prevNode.col == col):
                isWall = matrix[row + 1][col] == 1
                if isWall:
                    if toRemove > 0:
                        neighbours.append(
                            MyNode(row + 1, col, 0, matrix, self))
                else:
                    neighbours.append(
                        MyNode(row + 1, col, toRemove, matrix, self))

        return neighbours


def solution(m):

    # toRemove is 1 as default as per question constraints, and there is no previous node so make it itself
    start = MyNode(0, 0, 1, m, MyNode(0, 0, 1, m, None))

    # initialize a queue to use in the BFS
    q = deque([start])

    # The initial distance is 1 because we include the start and end nodes as part of the distance
    # the distance dict will keep track of nodes and their distance from the start. This way, once we
    # find the end node, we will have the proper distance from the start
    distanceDict = {start: 1}

    # while the queue is not empty
    while q:

        # pop the next node off
        currNode = q.popleft()
        # check if this is the end node. If it is, return the distance associated with it, which would have been set in a previous iteration
        if currNode.row == len(m) - 1 and currNode.col == len(m[0]) - 1:
            return distanceDict[currNode]

        # if not, push its neighbours onto queue with updated distance and repeat
        for neighbour in currNode.getNeighbours():
            # only add a node if it's not already in the queue (taking into consideration the position and whether the wall remove has been used)
            if neighbour not in distanceDict.keys():
                # incrememnt distance for the next node in the existing path
                distanceDict[neighbour] = distanceDict[currNode] + 1
                q.append(neighbour)

    # We are guaranteed that a path can be found so this return should never be executed, but return -1 by default just in case
    return -1


def main():

    # # Test cases
    assert(solution(
        [[0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]) == 39)
    # print("==================================================================")
    assert (
        solution([[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]]) == 7
    )
    # print("==================================================================")
    assert (
        solution([[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [
                 0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]) == 11
    )
    # print("==================================================================")
    assert(
        solution([[0, 1, 0, 0], [0, 0, 0, 0], [0, 0, 1, 1],
                  [0, 1, 1, 0], [0, 1, 1, 0]]) == 8
    )
    # print("==================================================================")
    assert(
        solution([
            [0, 1, 0, 1, 0, 0, 0],
            [0, 0, 0, 1, 0, 1, 0]
        ]) == 10
    )


if __name__ == "__main__":
    main()
