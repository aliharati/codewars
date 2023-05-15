# DESCRIPTION:
# Snail Sort
# Given an n x n array, return the array elements 
# arranged from outermost elements to the middle element, 
# traveling clockwise.

# array = [[1,2,3],
#          [4,5,6],
#          [7,8,9]]
# snail(array) #=> [1,2,3,6,9,8,7,4,5]
# For better understanding, please follow the numbers of the next array consecutively:

# array = [[1,2,3],
#          [8,9,4],
#          [7,6,5]]
# snail(array) #=> [1,2,3,4,5,6,7,8,9]
# This image will illustrate things more clearly:


# NOTE: The idea is not sort the elements from the lowest value to the highest; 
# the idea is to traverse the 2-d array in a clockwise snailshell pattern.

# NOTE 2: The 0x0 (empty matrix) is represented as en empty array inside an array [[]].

def snail(snail_map):
    new_list = []
    backup_list = []
    if snail_map == []:
        return []
    if isinstance(snail_map[0],int):
        new_list = snail_map
    else:
        for i in range(len(snail_map)):
            if i == 0:
                for j in range(len(snail_map[0])):
                    new_list.append(snail_map[0][j])
            elif i < len(snail_map) - 1:
                new_list.append(snail_map[i][-1])
                if len(backup_list) == 0:                
                    backup_list.append(snail_map[i][:-1])
                else:
                    backup_list[0].insert(0,snail_map[i][0])
                    backup_list.append(snail_map[i][1:-1])
            else:
                for j in range(len(snail_map[-1])-1,-1,-1):
                    new_list.append(snail_map[-1][j])
    new_list += snail(backup_list)
    return new_list

snail([[1,2,3,4],
       [14,15,16,5],
       [13,20,17,6],
       [12,19,18,7],
       [11,10,9,8]])