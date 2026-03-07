def x(square):
    if len(square) != 3:
        return False
    for row in square:
        if len(row) != 3:
            return False
    flat_list = []
    for row in square:
        flat_list.extend(row)
    if sorted(flat_list) != [1, 2, 3, 4, 5, 6, 7, 8, 9]:
        return False
    magic_sum = 15
    for row in square:
        if sum(row) != magic_sum:
            return False
    for col in range(3):
        column_sum = square[0][col] + square[1][col] + square[2][col]
        if column_sum != magic_sum:
            return False
    diag1_sum = square[0][0] + square[1][1] + square[2][2]
    if diag1_sum != magic_sum:
        return False
    diag2_sum = square[0][2] + square[1][1] + square[2][0]
    if diag2_sum != magic_sum:
        return False
    return True

# test_square = [[4, 9, 2], [3, 5, 7], [8, 1, 6]]
# print(x(test_square))

