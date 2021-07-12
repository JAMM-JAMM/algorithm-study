import time

# 나의 풀이

# location = input()

# start_time = time.time()

# steps = [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (1, -2), (-1, 2), (1, 2)]

# col_conversion = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}

# cur_row = int(location[1])
# cur_col = col_conversion[location[0]]

# result = 0

# for step in steps:
#     next_row = cur_row + step[0]
#     next_col = cur_col + step[1]
#     if next_row >= 1 and next_row <= 8 and next_col >= 1 and next_col <= 8:
#         result += 1
#         print(next_row, next_col)

# end_time = time.time()

# print(result)
# print(end_time - start_time)

# 답안

input_data = input()

start_time = time.time()

row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1

steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

result = 0
for step in steps:
    next_row = row + step[0]
    next_column = column + step[1]
    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        result += 1

end_time = time.time()

print(result)
print(end_time - start_time)