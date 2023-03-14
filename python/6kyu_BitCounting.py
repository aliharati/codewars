# Write a function that takes an integer as input, and returns the number of bits 
# that are equal to one in the binary representation of that number. 
# You can guarantee that input is non-negative.

# Example: The binary representation of 1234 is 10011010010, 
# so the function should return 5 in this case

def count_bits(n):
    num = n
    binary_list = []
    while num >= 1:
        binary_list.insert(0, num%2)
        num = num//2
    
    return sum(binary_list)

