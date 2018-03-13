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

	def dikstra(self,start,stop):

		#open list		
		Q = set()
		#starting distance
		D={}
		#parents of nodes
		parents = {}
		for v in self.adj_list:
			D[v] = float('inf')
			Q.add(v)
			parents[v] = None
		
		#first node -> 0
		D[start] = 0

		v=D[0]
		while len(Q) > 0:
	
			v = float('inf')
			val =float ('inf')
			flag=0
			for item,value in D.items():
				if value != float('inf') and item in Q and flag==0:
					v=item
					
					val=value
					
					flag=1
				if flag==1 and value!=float('inf') and val>value and item in Q:
					v=item
					
					val=value
					
			if v==float('inf'):
				
				return []
			
			if v==stop:
				print "Min distance = %d" % val
				path = deque()
				while parents[v] != None:
					path.appendleft(v)
					v= parents[v]
				path.appendleft(v)
				return list(path)
					
			
			for (w,weight) in self.adj_list[v]:
				if w in Q:
					if val+weight < D[w]:
						D[w]=val+weight
						parents[w]=v
			
			Q.remove(v)
		return []
	
	def h(self,stop):
		self.unmark()
		result = {}
		i=0
		result[stop]=i 
		self.marked[stop] = True
		path = deque([])
		path.appendleft(stop)

		while len(path) > 0:
			v = path.popleft()
			i=i+1
			for (w,weight) in self.adj_list[v]:
				if w not in self.marked:
					path.append(w)
					result[w] = i
										
					self.marked[w] = True
		return result

	def astar(self,start,stop,h):
		open_list = {}
		closed_list = {}
		parents = {}
		D= {}
		open_list[start] = True
		for it in self.adj_list:
			parents[it]= None
			D[it] = float('inf')
		D[start] = 0

		v=D[0]
		while open_list > 0:
	
			v = float('inf')

			for w in open_list:
				if D[w] != float('inf') and (v == float('inf') or D[w]+h[w] < D[v]+h[v]):
					v = w;

			if v == float('inf'):
				return []

			if v==stop:
				path = deque()
				print ("Min distance= %d" % D[w])
				while parents[v] != None:
					
					path.appendleft(v)
					v=parents[v]
				path.appendleft(v)
				return list(path)
			for (w,weight) in self.adj_list[v]:
				if(w not in closed_list and w not in open_list):
					open_list[w] = True
					parents[w] = v
					D[w] = weight + D[v]
				else:
					if D[v] + weight < D[w]:
						D[w] = D[v] + weight
						parents[w] = v 
						if w in closed_list:
							del closed_list[w]
							open_list[w] = True
			del open_list[v]
			closed_list[v] = True
		return []

						


   


			
