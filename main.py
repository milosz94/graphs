#! /usr/bin/env python
# -*- coding: utf-8 -*-

from graph import Graph


def main():
    g = Graph({
        0: [(2, 1),(1, 10)],
        1: [(0, 1)],
        2: [(2, 1), (1, 1)]
    })
    h = Graph({
        0:[(1,2),(8,866)],
        1:[(0,3),(2,1)],
        2:[(3,4),(4,1),(5,2),(8,1)],
        3:[(2,2)],
        4:[(2,1),(7,3)],
        5:[(2,3),(6,2),(4,1)],
        6:[(8,1),(5,1)],
        7:[(6,4),(4,4)],
        8:[(0,4),(2,1),(6,6)]
   })
  

    print("DFS: %s" % str(h.DFS(0, 7)))
    print("BFS: %s" % str(h.BFS(0, 7)))
    print("Dikstra: %s" % str(h.dikstra(0,7)))
    print("Heuristics: %s" % h.h(7))
    print("Astar: %s" % str(h.astar(0,7,h.h(7))))

if __name__=="__main__":
	main()
