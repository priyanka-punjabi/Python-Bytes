'''
    @author: Priyanka Punjabi
'''
import math
import sys
import time as t
from heapq import heappop, heappush

sys.setrecursionlimit(6000)


class Maze:
    __slots__ = 'height', 'width', 'start', 'goal', 'idsPath', 'idsDepth'

    def __init__(self):
        self.height = 0
        self.width = 0
        self.idsPath = "(0, 0)"
        self.idsDepth = 0

    def draw_graph(self, maze):
        graph = {(i, j): [] for j in range(self.width) for i in range(self.height)}
        for row, col in graph.keys():
            if row < self.height - 1 and maze[row + 1][col] != '1':
                graph[(row, col)].append((row + 1, col))
            if row < self.height - 1 and maze[row][col] != '1':
                graph[(row + 1, col)].append((row, col))
            if col < self.width - 1 and maze[row][col] != '1':
                graph[(row, col + 1)].append((row, col))
            if col < self.width - 1 and maze[row][col + 1] != '1':
                graph[(row, col)].append((row, col + 1))
        return graph

    # Manhattan Distance
    def getHeuristic1(self, curr, goal):
        return abs(curr[0] - goal[0]) + abs(curr[1] - goal[1])

    # Euclidean Distance
    def getHeuristic2(self, curr, goal):
        return math.sqrt((curr[0] - goal[0]) ** 2 + (curr[1] - goal[1]) ** 2)

    # Chebyshev Distance
    def getHeuristic3(self, curr, goal):
        return max(abs(curr[0] - goal[0]), abs(curr[1] - goal[1]))

    # Octile Distance
    def getHeuristic4(self, curr, goal):
        distx = abs(curr[0] - goal[0])
        disty = abs(curr[1] - goal[1])
        return max(distx, disty) + (math.sqrt(2) - 1) * min(distx, disty)

    def maze_solve(self):
        print("Generating Graph from Maze...")
        maze = []
        with open("data.txt") as f:
            first_line = f.readline()
            self.width = len(first_line.strip().split(" "))
            f.seek(0)
            for line in f:
                line = line.strip().split(" ")
                self.height += 1
                maze.append(line)
        graph = self.draw_graph(maze)
        self.start = (0, 0)
        self.goal = (self.height - 1, self.width - 1)
        self.execute(graph)

    def execute(self, graph):
        print("A* using Heuristic 1: ")
        start_time = t.time()
        path, count = self.astar(graph, self.getHeuristic1)
        end_time = t.time()
        diff_time = end_time - start_time
        if path is None:
            noOfSteps = 0
        else:
            noOfSteps = len(path.split(" -> "))
        print("Path: " + str(path))
        print("No. of Visited Nodes: " + str(count))
        print("No. of Steps: " + str(noOfSteps))
        print("Time taken: " + str(diff_time))
        print("***********************************************************")
        print("A* using Heuristic 2: ")
        start_time = t.time()
        path, count = self.astar(graph, self.getHeuristic2)
        end_time = t.time()
        diff_time = end_time - start_time
        if path is None:
            noOfSteps = 0
        else:
            noOfSteps = len(path.split(" -> "))
        print("Path: " + str(path))
        print("No. of Visited Nodes: " + str(count))
        print("No. of Steps: " + str(noOfSteps))
        print("Time taken: " + str(diff_time))
        print("***********************************************************")
        print("A* using Heuristic 3: ")
        start_time = t.time()
        path, count = self.astar(graph, self.getHeuristic3)
        end_time = t.time()
        diff_time = end_time - start_time
        if path is None:
            noOfSteps = 0
        else:
            noOfSteps = len(path.split(" -> "))
        print("Path: " + str(path))
        print("No. of Visited Nodes: " + str(count))
        print("No. of Steps: " + str(noOfSteps))
        print("Time taken: " + str(diff_time))
        print("***********************************************************")
        print("A* using Heuristic 4: ")
        start_time = t.time()
        path, count = self.astar(graph, self.getHeuristic4)
        end_time = t.time()
        diff_time = end_time - start_time
        if path is None:
            noOfSteps = 0
        else:
            noOfSteps = len(path.split(" -> "))
        print("Path: " + str(path))
        print("No. of Visited Nodes: " + str(count))
        print("No. of Steps: " + str(noOfSteps))
        print("Time taken: " + str(diff_time))
        print("***********************************************************")
        print("Iterative Deepening Search: ")
        max_depth = (self.width - 1) * (self.height - 1)
        start_time = t.time()
        path, count = self.findPathIDFS(self.start, self.goal, graph, max_depth)
        end_time = t.time()
        diff_time = end_time - start_time
        if path is None:
            noOfSteps = 0
        else:
            noOfSteps = len(path)
        path = str(path).strip('[]').replace('),', ') ->')
        print("Path: " + str(path))
        print("No. of visited Nodes: " + str(count))
        print("No. of Steps: " + str(noOfSteps))
        print("Time taken: " + str(diff_time))

    def astar(self, graph, heuristic):
        pqueue = []
        heappush(pqueue, (0 + heuristic(self.start, self.goal), 0, "(0, 0)", self.start))
        heuCost = heuristic(self.start, self.goal)
        costOfNodes = {self.start: (0 + heuCost)}
        vistedCount = 0
        while pqueue:
            _, cost, path, curr = heappop(pqueue)
            if curr == self.goal:
                path = path.lstrip(" -> ")
                return path, vistedCount
            vistedCount += 1
            costOfNodes[curr] += 1

            for neighbour in graph[curr]:
                heuCost = heuristic(neighbour, self.goal)
                if neighbour not in costOfNodes:
                    heappush(pqueue, (1 + heuCost, cost + 1, path + " -> " + str(neighbour), neighbour))
                    costOfNodes[neighbour] = 1 + heuCost
                if cost + 1 + heuCost < costOfNodes[neighbour]:
                    heappush(pqueue, (1 + heuCost + cost, cost + 1, path + " -> " + str(neighbour), neighbour))
                    costOfNodes[neighbour] = 1 + heuCost + cost
        return None, vistedCount

    def __findPathIDFS(self, current, end, graph, depth, visited=None, count=0):
        count += 1
        if current == end:
            return [current], count
        if depth <= 0:
            return None, count
        if visited is None:
            visited = dict()

        visited[current] = depth

        for neighbor in graph.get(current, []):

            if neighbor not in visited or (neighbor in visited and visited[neighbor] < depth - 1):
                path, tot_count = self.__findPathIDFS(neighbor, end, graph, depth - 1, visited, count)
                count = tot_count
                if path != None:
                    path.insert(0, current)
                    return path, tot_count
        return None, count

    def findPathIDFS(self, start, end, graph, max_depth):
        tot_count = 0
        for depth in range(max_depth):
            res, count = self.__findPathIDFS(start, end, graph, depth)
            tot_count += count
            if res is not None:
                print("Found at depth: " + str(depth))
                return res, tot_count
        return None, tot_count


def main():
    m = Maze()
    m.maze_solve()


if __name__ == '__main__':
    main()
