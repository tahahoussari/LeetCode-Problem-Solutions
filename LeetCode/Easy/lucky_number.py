def luckyNumber(matrix):
    answer = []
    min_in_row = min(matrix[0])
    min_in_row_index = matrix[0].index(min(matrix[0]))
    for i in range(len(matrix)):
        if min(i) >= min_in_row:
            min_in_row_index = i.index(min(i))
    print(min_in_row_index)

    for i in matrix:
        print(i)

    return answer

print(luckyNumber([[3,6],[7,1],[5,2],[4,8]]))