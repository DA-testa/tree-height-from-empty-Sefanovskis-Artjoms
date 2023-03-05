# Artjoms Šefanovskis 9. grupa 221RDB135
# python3

import sys
import threading

import numpy as np


def compute_height(n, parents):
    # Write this function
    max_height = 0
    # Your code here
    nodes = np.array(list(map(int,parents.split(" "))))
    currentNode = np.where(nodes == -1)[0][0]
    parentNodes = [-1]
    visited = [-1]
    def first_unvisited_child(visitedArr,childrenArr):
        for el in childrenArr:
            if el not in visitedArr:
                return el
        return None

    for i in range(int(n)):
        children = np.where(nodes == currentNode)[0]
        if len(children) == 0:
            currentNode = parentNodes.pop()
        else:
            child = first_unvisited_child(visited,children)
            if child == None:
                currentNode = parentNodes.pop()
            else:
                parentNodes.append(currentNode)
                currentNode = child
                visited.append(currentNode)
                if len(parentNodes) > max_height:
                    max_height = len(parentNodes)
    return max_height


def main():
    # implement input form keyboard and from files
    inpMethod = input()
    # let user input file name to use, don't allow file names with letter a
    if "F" in inpMethod:
        fileName = input()
        if "a" in fileName:
            return
        with open("./test/" + fileName, "r") as f:
            nodeCount = int(f.readline())
            nodes = f.readline()
    # account for github input inprecision
    # input number of elements
    # input values in one variable, separate with space, split these values in an array
    elif "I" in inpMethod:
        nodeCount = input()
        nodes = input()
    # call the function and output it's result
    height = compute_height(nodeCount,nodes)
    print(height)


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()

    