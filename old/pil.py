def get_2d_array(text_file):
    with open(text_file) as file:
        elevation_list = [line.split() for line in file]
        #print(elevation_list)
        # print(f'The length is{len(elevation_list[0]) }')
        # return elevation_list


small_elevation_array = get_2d_array(
    'elevation_small.txt')  # creating variable to function get_2d_array

# Task 2
# use function get_2d_array calling it by its new variable name small_elevation_list

# try array action on simple example

# simple_array = [['1', '2', '3', '4', '5'],
# 				['1', '2', '3', '4', '5'],
# 				['1', '2', '3', '4', '5'],
# 				['9', '8', '7', '6', '5']]

# simple_int_array = [[int(number) for number in row] for row in simple_array]

# #print(simple_int_array)

# mins = [min(row) for row in simple_int_array]
# smallest_min = min(mins)
# # print(smallest_min)

# maxs = [max(row) for row in simple_int_array]
# biggest_min = max(maxs)

# print(biggest_min)