def get_mex(arr):
    s = set(arr)
    i = 0
    while i in s:
        i += 1
    return i

def possible_valid_sizes(n, memoryblocks):
    from itertools import product

    possible_mex_values = set()
    # Each block can be incremented from its current value up to n-1
    ranges = [range(block, n) for block in memoryblocks]
    for candidate in product(*ranges):
        possible_mex_values.add(get_mex(candidate))
    return sorted(list(possible_mex_values))

# Example from the problem description:
n_val = 8
blocks = [0,1,2,2,3,3,4,4]
print(possible_valid_sizes(n_val, blocks))  # Should print [0,1,2,3,4,5,6,7,8]
print(possible_valid_sizes(3, [0,2,2]))    # Should print [0,1]
print(possible_valid_sizes(3, [2,2,2])) 