#def get_2d_array(text_file):
	#with open(text_file) as file:
		#elevation_list = [line.split() for line in file]
		#print(elevation_list)
		#print(f'The length of each list is {len(elevation_list)}')
		#print(f'The length is{len(elevation_list[0]) }')
		#return elevation_list

#get_2d_array('elevation_small.txt')

# try array action on simple example

simple_array = [['1', '2', '3', '4', '5'],
				['1', '2', '3', '4', '5'],
				['1', '2', '3', '4', '5'],
				['9', '8', '7', '6', '5']]

simple_int_array = [[int(number) for number in row] for row in simple_array]

#print(simple_int_array)

mins = [min(row) for row in simple_int_array]
smallest_min = min(mins)
# print(smallest_min)

maxs = [max(row) for row in simple_int_array]
biggest_min = max(maxs)

print(biggest_min)

