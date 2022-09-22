from dis import dis
from math import inf
# A B C D E F G H I 
# 0 1 2 3 4 5 6 7 8

number_of_edges = 8
edges = [inf for x in range(number_of_edges)]
distancess = [((2, 10), (1, 7)), ((0, 7), (5, 9), (6, 27)),
           ((0, 10), (5, 8), (4, 31)), ((4, 32), (7, 17), (8, 21)),
           ((2, 31), (3, 32)), ((1, 9), (2, 8), (7, 11)),
           ((1, 27), (8, 15)), ((5, 11), (3, 17), (8, 15)), 
           ((3, 21), (7, 15), (6, 15))]

                                # A B C D E F G H I 
                                # 0 1 2 3 4 5 6 7 8
distances_lecture = [((1, 5), (2, 2)), ((0, 5), (2, 2), (3, 3), (4, 2)),
                     ((0, 2), (1, 2), (3, 10), (4, 7)), ((1, 3), (2, 10), (6, 5), (5, 5)),
                     ((1, 2), (2, 7), (5, 6), (6, 4)), ((4, 6), (3, 5), (7, 3)),
                     ((3, 5), (7, 2), (4, 4)), ((5, 3), (6, 2))]

def Dijkstra(distances):
    while(0 < (pick := int(input("Choose edge: "))) > number_of_edges):
        continue
    edges[pick - 1] = 0

    for distance in distances[pick - 1]:
            edges[distance[0]] = distance[1]

    for x in range(len(distances)):
        for distance in distances[x]:
                edges[x] = min(distance[1] + edges[distance[0]], edges[x])

    print(edges)


Dijkstra(distances_lecture)

