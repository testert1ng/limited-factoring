#!/usr/bin/env python

'''
Solution for IPSI Limited Factoring interview test

https://gist.github.com/jcampbell-ipsi/1cca1c94f84fd7d198bda41b33f01a51
'''

__author__ = "Junting Zhu"

import sys
import numpy

def get_shortest_path(target_number, factors):
	'''
	Get the shortest path for a given target number with a list of possible factors

	:param int target_number: The target number (N) which is a positive integer less than 2^60
	:param [] factors: The short listed array of unique integers, each less than 2^60
	:return: The shortest path in string or -1 if shortest path not exist
	'''
	if len(factors) == 0:
		return '-1'
		
	for f in factors:
		if target_number > f and target_number % f == 0:
			path = get_shortest_path(target_number / f, factors)
			#print(path)
			if path != '-1':
				return path + ' ' + str(target_number)
		elif target_number == f:
			#print(str(target_number) + ' ' + str(f))
			return '1 ' + str(target_number)

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

		target_number = nk[0]
		number_of_factors = nk[1]

		if target_number >= 2 ** 60 or target_number <= 0:
			print('N should be positive integer less than 2^60')
			return

		if number_of_factors >= 32 or number_of_factors <= 0:
			print('K should be positive integer less than 32')
			return

		# line 2, A is a set of unique integers, each less than 2^60, with K elements
		print('Please type in a set of unique integers, each less than 2^60')
		line = sys.stdin.readline()
		possible_factors = map(int, line.split())

		if len(possible_factors) != number_of_factors :
			print('A should contains K elements')
			return

		if len(numpy.unique(possible_factors)) != number_of_factors:
			print('A should only contains unique integers')
			return			

		for f in possible_factors:
			if f >= 2 ** 60 or f <= 0:
				print('All elements in a should be positive integer less than 2^60')
				return
		
	except:
		print('Input value errors')
		return

	# end input validation

	sorted_factors = sorted(possible_factors, reverse=True)
	factors = sorted_factors
		
	for f in sorted_factors:
		if target_number % f != 0 or f == 1 or f > target_number:
			factors.remove(f)
	#print(factors)
	
	# recursive function for shortest path
	print('Shortest path: ')
	print(get_shortest_path(target_number, factors))
		

if __name__ == '__main__':
	main()
