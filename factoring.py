#!/usr/bin/env python

'''
Solution for IPSI Limited Factoring interview test

https://gist.github.com/jcampbell-ipsi/1cca1c94f84fd7d198bda41b33f01a51
'''

__author__ = "Junting Zhu"

import sys
import numpy

def get_shortest_path(n, a):
	'''
	Get the shortest path for a given target number with a list of possible factors

	:param int n: The target number (N) which is a positive integer less than 2^60
	:param [] a: The short listed array of unique integers, each less than 2^60
	:return: The shortest path in string or -1 if shortest path not exist
	'''
	if len(a) == 0:
		return '-1'
		
	for e in a:
		if n > e and n % e == 0:
			output = get_shortest_path(n / e, a)
			#print(output)
			if output != '-1':
				return output + ' ' + str(n)
		elif n == e:
			#print(str(n) + ' ' + str(e))
			return '1 ' + str(n)

	return '-1'

def main():
	'''
	the main function, which takes the std input for aspecific format
	and print out the shortest path if available
	'''

	# start input validation 
	try:
		# line 1, N is a positive integer less than 2^60 K is a positive integer less than 32
		print('Please type in two space-separated integers N and K:')
		line = sys.stdin.readline()
		nk = map(int, line.split())

		if len(nk) != 2:
			print('Two integers required')
			return

		n = nk[0]
		k = nk[1]

		if n >= 2 ** 60 or n <= 0:
			print('N should be positive integer less than 2^60')
			return

		if k >= 32 or n <= 0:
			print('K should be positive integer less than 32')
			return

		# line 2, A is a set of unique integers, each less than 2^60, with K elements
		print('Please type in a set of unique integers, each less than 2^60')
		line = sys.stdin.readline()
		a = map(int, line.split())

		if len(a) != k :
			print('A should contains K elements')
			return

		if len(numpy.unique(a)) != k:
			print('A should only contains unique integers')
			return			

		for e in a:
			if e >= 2 ** 60 or n <= 0:
				print('All elements in a should be positive integer less than 2^60')
				return
		
	except:
		print('Input value errors')
		return

	# end input validation  
	sorted_a = sorted(a, reverse=True)
		
	for e in a:
		if n % e != 0 or e == 1 or e > n:
			sorted_a.remove(e)
	#print(sorted_a)
	
	# recursive function for shortest path
	print('Shortest path: ')
	print(get_shortest_path(n, sorted_a))
		

if __name__ == '__main__':
	main()
