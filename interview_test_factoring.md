### Problem:
Given a set of potential factors, find the shortest (by number of factors, then numerical order) path to the target number.

##### Example:
`N` (target number) = 12

`A` (possible factors) = 2, 3, 4

##### The following paths are valid:
```
(a) 1  ->  2  ->  4  ->  12
       x2     x2     x3

(b) 1  ->  4  ->  12
       x4     x3

(c) 1  ->  3  ->  12
       x3     x4
```

(a) is not the shortest path because it has 4 elements.  While (b) and (c) are both the shortest, (c) has a shorter numerical order path (3 < 4).

### Input format:
Input is given via stdin, in two lines.
The first line contains two space-separated integers `N` and `K`, which are the target number and number of factors respectively.
The second line contains `K` space-separated integers representing the set `A` of possible factors.

### Output format:
Output should be printed to stdout, on a single line.
This line should contain all steps from `1` to the final number inclusive (eg. `1 3 12` for the above example)
If no path from `1` to the final number is possible with the given factors, `-1` should be output instead.

### Constraints:
`N` is a positive integer less than 2^60
`K` is a positive integer less than 32
`A` is a set of unique integers, each less than 2^60, with `K` elements

### Sample 1:
##### Input:
```
12 3
2 3 4
```

##### Output:
```
1 3 12
```

##### Explanation:
See above description

### Sample 2:
##### Input:
```
15 5
2 10 6 9 11
```

##### Output:
```
-1
```

##### Explanation:
There is no factored path from 1 to 15 given the possible factors.

### Sample 3:
##### Input:
```
72 9
2 4 6 9 3 7 16 10 5
```

##### Output:
```
1 2 8 72
```

##### Explanation:
Given these 8 possible factors, there is several ways to reach `72`, however the shortest path is 4 states.

```
States          =>  Multiplication operation
 1   9  18  72  =>      (x9, x2, x4)
 1   4  36  72  =>      (x4, x9, x2)
 1   2   8  72  =>      (x2, x4, x9)
 1   2  18  72  =>      (x2, x9, x4)
 1   4   8  72  =>      (x4, x2, x9)
 1   9  36  72  =>      (x9, x4, x2)
```

Of these, `1 2 8 72` is the lowest numerical ordering.
