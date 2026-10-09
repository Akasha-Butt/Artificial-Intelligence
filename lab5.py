################################## TASK 01##############################################
#########Write a program that will implement the following graph in python. ############
from collections import deque

# graph = {
#     0: [1, 4],
#     1: [0, 4, 3, 2],
#     2: [1, 3],
#     3: [1, 4, 2],
#     4: [0, 1, 3]
# }

# queue = deque([0])
# visited = [0]

# while queue:
#     node = queue.popleft()
#     print(node, end=" ")

#     for neighbour in graph[node]:
#         if neighbour not in visited:
#             visited.append(neighbour)
#             queue.append(neighbour)

# ################################## TASK 02##############################################
# ######You are given the following tree whose starting node is A and Goal node is G .####
# # You are required to implement the following graph in python ###########################
# # and then apply the following search(Stop the search when goal is achieved) a) Breadth First Search using Queue.####
# from collections import deque

# tree = {
#     'A': ['B', 'F', 'D', 'E'],
#     'B': ['K', 'J'],
#     'F': [],
#     'D': ['G'],
#     'E': ['C', 'H', 'I'],
#     'K': ['N', 'M'],
#     'J': [],
#     'G': [],
#     'C': [],
#     'H': [],
#     'I': ['L'],
#     'N': [],
#     'M': [],
#     'L': []
# }

# queue = deque(['A'])
# visited = ['A']

# while queue:
#     node = queue.popleft()
#     print(node, end=" ")

#     if node == 'G':
#         print("\nGoal found!")
#         break

#     for child in tree[node]:
#         if child not in visited:
#             visited.append(child)
#             queue.append(child)


################################## TASK 03##############################################
#############################: Implement priority Queue. ###############################
import heapq

queue = []

heapq.heappush(queue, (3, "AIMAN"))
heapq.heappush(queue, (1, "MADIHA"))
heapq.heappush(queue, (2, "AKASHA"))

print(heapq.heappop(queue))
print(heapq.heappop(queue))
print(heapq.heappop(queue))