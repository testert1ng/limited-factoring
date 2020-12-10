'''
Test for factoring.py
'''

import pytest
from factoring import get_shortlisted_factors, get_shortest_path

@pytest.mark.parametrize("line1, line2, target_number, number_of_factors, possible_factors", 
	[('12 3', '2 3 4', 12, 3, [2, 3, 4]), 
	('15 5', '2 10 6 9 11', 15, 5, [2, 10, 6, 9, 11]), 
	('72 9', '2 4 6 9 3 7 16 10 5', 72, 9, [2, 4, 6, 9, 3, 7, 16, 10, 5])])
def test_input(line1, line2, target_number, number_of_factors, possible_factors):
	nk = map(int, line1.split())
	assert target_number == nk[0]
	assert number_of_factors == nk[1]
	assert possible_factors == map(int, line2.split())

@pytest.mark.parametrize("target_number, possible_factors, expected", 
	[(12, [2, 3, 4], [4, 3, 2]), 
	(15, [2, 10, 6, 9, 11], []), 
	(72, [2, 4, 6, 9, 3, 7, 16, 10, 5], [9, 6, 4, 3, 2])])
def test_get_shortlisted_factors(target_number, possible_factors, expected):
	assert get_shortlisted_factors(target_number, possible_factors) == expected

@pytest.mark.parametrize("target_number, shortlisted_factors, expected", 
	[(12, [4, 3, 2], '1 3 12'), 
	(15, [], '-1'), 
	(72, [9, 6, 4, 3, 2], '1 2 8 72')])
def test_get_shortest_path(target_number, shortlisted_factors, expected):
	assert get_shortest_path(target_number, shortlisted_factors) == expected