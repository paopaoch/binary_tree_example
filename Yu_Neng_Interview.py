# nums  = [3,6,5,1,8] # Not distinct, no cap
# output = 18
# pick 3, 6, 1 and 8 and their sum is 18


# Maximum possible sum such that it is divisible by three
# if num % 3 == 0

# [8, 6, 5, 3, 1]

# sum(nums) --> 23

# 0 -> 3 -> 6
# =
# 0 -> 6
# =
# 0

def max_divisible_by_three(nums): # 1262
    sums = [0, 0, 0]
    for num in nums:
        for summ in sums[:]:
            remainder = (num + summ) % 3
            sums[remainder] = max(num + summ, sums[remainder])

    return sums[0]


# --------------------------------------------------------------

# grid =   [['a', 'a', 'a', 'a'], 
#           ['a', 'b', 'b', 'a'], 
#           ['a', 'b', 'b', 'a'], 
#           ['a', 'a', 'a', 'a']]

# output = true

def get_if_cycle(grid): # 1559

    def in_grid(index):
        if index[0] < 0 or index[0] > len(grid[0]) - 1:
            return False
        if index[1] < 0 or index[1] > len(grid) - 1:
            return False
        return True

    def recursion_function(index, previous_index, hashy_thing, global_hashy):
        if index in hashy_thing:
            return True
        hashy_thing.add(index)
        global_hashy.add(index)
        if grid[previous_index[0]][previous_index[1]] == grid[index[0]][index[1]]:
            for x_index, y_index in [[1, 0], [-1, 0], [0, -1], [0, 1]]:
                if ((index[0] + x_index, index[1] + y_index) != previous_index 
                    and in_grid((index[0] + x_index, index[1] + y_index))):
                    if recursion_function((index[0] + x_index, index[1] + y_index), index, hashy_thing, global_hashy):
                        return True
        return False

    global_hashy = set()
    for i, row in enumerate(grid):
        for j, _ in enumerate(row):
            if (i, j) not in global_hashy:
                hashy_thing = set()
                if recursion_function((i, j), None, hashy_thing, global_hashy):
                    return True
    
    return False

# en1 = (1,2)
# en2 = (1,2)

# print(en1 == en2) --> True