<!-- small explainations -->

# move to github tracking
## commands 
time python -m XX>py

### day X
#### part 1
#### part 2

### day 12
#### part 1
	This is the most scam question ever 😭. The "intended" solution does not work on the test case provided. why ? Eric must've had enough. In order to solve this; one must notice the input pattern; for each input, it is either trivially yes or no. So without the complications of the input constraints (rotating and flipping), one can simply place the shapes next to each other and check if that is enough area or not.

### day 11
#### part 1
	this is standard graph traversal problem. How many nodes from start to end; can be solved iteratively with stack or recursively with dfs;
#### part 2
	iterative stack will not work becasue of how large the network of connections can grow; rely on caching if a path is already seen.
	
### day 10
#### part 1
	input is small enough that u may generate all the subsequence (combinations) of possible keys and try them out sorted by length of the combinations. It is some coding but nothing mind boggling;
#### part 2 [FK this 😭]


### day 9
#### part 1
	So need to find area taking two points as their extremes; can just brute force it.
#### part 2 [TODO]
	shid so hard; even John took a break 😭🙏🏼
	This is point in polygon algorithm except here the polygon is guaranteed to have 90 degress (internal). The hard part is getting the boundary of the polygon. 

### day 8 [TODO: straight up graph]
#### part 1
#### part 2

### day 7
#### part 1
	It is a graph problem. we branch out search when "^" is encountered. Needs to count no of branching happening (unique); the branching may result in clashing branches which needs to be ignored.
#### part 2
	Count no of paths from start to end. 

### day 6
#### part 1
	Very tedious. Needs to splits a string just the right way and transform to ints.
#### part 2 [TODO]


### day 5
#### part 1
	a list of ranges is given and simply need to check if an id falls within any of the ranges. The list of ranges given is not too long in actual input so a normal for loop suffice.
#### part 2
	the ranges can have overlap; now we need to count the unique values in all the ranges. This can be achieved by merging all overlapping ranges and simply couting the interval range of the range. We can do this using "interval tree" (very hard segment tree based data structure) or we should just sort given ranges and try merging until no more merge is possible (so this one it is :D).
	check how the smart people have done it

### day 4
#### part 1
	it is a graph like problem where u explore 8 of its neighbours and count the presence of '@'. Fairly easy to simulate
#### part 2
	Needs to repeat part 2 until no more conditions are satisfied. Can be done by calling part 1 in a loop


### day 3
#### part 1
	for each ordered input; take two digits in original order and make the largest 2 digit num possible. You can check by choosing the largest and comparing what is received by joining left ans and right answer seperately. It is still very simulation.

#### part 2 [TODO]
	We can choose 12 numbers intead of just 2.; Can use DP for 12 nested for loop

### day 2
#### part 1 
	range a-b is given and within range need to find num which can be split into two parts and both parts are same. Can simulate direclty as the range is not too wide.
#### part 2
	now it can be split into as many parts as possible and there needs to be only one repeating. Can still simulate as range is not that wide.
