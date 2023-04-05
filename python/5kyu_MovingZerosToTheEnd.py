# Write an algorithm that takes an array and moves all of the zeros to the end, 
# preserving the order of the other elements.

# move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]


def move_zeros(lst):
    new_lst = []
    zeros = 0
    for num in lst:
        if num == 0:
            new_lst.append(num)
            zeros += 1
        else:
            new_lst.insert(len(new_lst) - zeros,num)
    return new_lst