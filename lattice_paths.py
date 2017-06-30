def find_routes(rows,columns):
	dictionary = {}
	for i in range (0,rows+1):
		for j in range (0,columns+1):
			current_point = (i,j)
			if j == 0 or i == 0:
				dictionary[current_point] = 1
			else:
				val1 = i-1
				val2 = j-1
				current_val = dictionary[(val1,j)] + dictionary[(i,val2)]
				dictionary[current_point] = current_val
	return (dictionary[rows,columns])



n = find_routes(20,20)
print n




# recursive/memoization
memo = {(0, 1) : 1, (1, 0) : 1}
def find_pathways(x, y):

    if (x, y) in memo : return memo[(x, y)]

    pathways = 0
    if 0 in (x, y):
        pathways = 1
    else:
        pathways = find_pathways(x-1, y) + find_pathways(x, y-1)


    memo[(x, y)] = pathways
    return pathways

print find_pathways(2, 2)
print find_pathways(20, 20)



