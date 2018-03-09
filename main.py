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
        0:[(1,1),(8,1)],
        1:[(0,1)],
        2:[(3,1),(4,1),(5,1),(8,1)],
        3:[(2,1)],
        4:[(2,1),(7,1)],
        5:[(2,1),(6,1),(4,1)],
        6:[(8,1),(5,1)],
        7:[(6,1),(4,1)],
        8:[(0,1),(2,1),(6,1)]
   })
  

    
    print("DFS: %s" % str(h.DFS(0, 5)))
    print("BFS: %s" % str(h.BFS(0, 5)))


if __name__=="__main__":
	main()