#! /usr/bin/env python
# -*- coding: utf-8 -*-

from collections import deque


class Graph:
	def __init__(self,adj_list):
		self.adj_list=adj_list
		self.marked = {}
	def unmark(self):
		self.marked = {}

	
	def DFS(self,start,stop):
		self.unmark()

		self.marked[start] = True
		path = []
		path.append(start)
		
		while len(path) > 0:
			v = path[-1]
			if v == stop:
				return path

			unvisited = False

			for (w,weight) in self.adj_list[v]:
				if w not in self.marked:
					path.append(w)
					self.marked[w] = True
					unvisited = True
					break

			if unvisited == False:
				path.pop()


	def BFS(self,start,stop):
		self.unmark()
		result = deque([])
		parents = {}

		for v in self.adj_list:
			parents[v] = None

		
		self.marked[start] = True
		path = deque([])
		path.appendleft(start)

		while len(path) > 0:
			v = path.popleft()
			
			if v==stop:
				while parents[v] != None:
					result.appendleft(v)
					v=parents[v]
				result.appendleft(v)
				return list(result)

			for (w,weight) in self.adj_list[v]:
				if w not in self.marked:
					path.append(w)
					parents[w] = v
					
										
					self.marked[w] = True






   


			
