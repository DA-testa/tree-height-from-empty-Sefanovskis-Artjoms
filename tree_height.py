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
    parentNodes = []
    visited = []
    for i in range(int(n)):
        child = np.where(nodes == currentNode)
        
        # Iet augšā
        if len(child[0]) == 0 or (child[0][0] in visited and (len(child[0]) >= 2 and child[0][1] in visited)):
            currentNode = parentNodes.pop()
        # Iet lejā
        else:
            
            if child[0][0] in visited:
                if len(child[0]) > 1:
                    child = child[0][1]
            else:
                child = child[0][0]
            parentNodes.append(currentNode)
            currentNode = child
            visited.append(currentNode)
            if len(parentNodes) > max_height:
                max_height = len(parentNodes)
    return max_height+1


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

