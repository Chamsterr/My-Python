from collections import deque

список_смежности_из_лабы = [[2, 5], [1, 7, 8], [8], [6, 9], [1, 6],
                            [4, 5, 9], [2, 8], [2, 3, 7], [4, 6, 9], [9]]

список_смежности_из_лекции = [[2, 4], [1, 6, 7], [7], [1, 5], [4, 8],
                              [2, 7], [2, 3, 6], [5]]


def BSF(start, список_списка_смежности_для_вершин_графа):
    queue = deque()
    visited = []
    queue.append(список_списка_смежности_для_вершин_графа[start - 1])
    visited.append(start - 1)
    while(queue):
        список_смежности_для_вершины = queue.popleft()
        for смежная_вершина in список_смежности_для_вершины:
            if смежная_вершина - 1 not in visited:
                queue.append(список_списка_смежности_для_вершин_графа[смежная_вершина - 1])
                visited.append(смежная_вершина - 1)
    return visited

def DSF(start, список_списка_смежности_для_вершин_графа):
    queue = deque()
    visited = []
    queue.append(список_списка_смежности_для_вершин_графа[start - 1])
    visited.append(start - 1)
    while(queue):
        список_смежности_для_вершины = queue.pop()
        for смежная_вершина in список_смежности_для_вершины:
            if смежная_вершина - 1 not in visited:
                queue.append(список_списка_смежности_для_вершин_графа[смежная_вершина - 1])
                visited.append(смежная_вершина - 1)
    return visited

print('-'*60)
print(f"Breadth First Search для лабы: {list(map(lambda x: x + 1, BSF(1, список_смежности_из_лабы)))}")
print(f"Depth First Search для лабы: {list(map(lambda x: x + 1, DSF(1, список_смежности_из_лабы)))}")
print('-'*60)
print(f"Breadth First Search для лекции: {list(map(lambda x: x + 1, BSF(1, список_смежности_из_лекции)))}")
print(f"Depth First Search для лекции: {list(map(lambda x: x + 1, DSF(1, список_смежности_из_лекции)))}")
print('-'*60)