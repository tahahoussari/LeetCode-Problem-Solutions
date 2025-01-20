def generate_pascal_triangle(num_rows):
    list = [[1],[1,1]]
    for i in range(1, num_rows):
        list.append([])

    for i in range(1, num_rows):
        temp_ls = []
        sum = 0
        
        for j in range(len(list[i])-1):
            sum = list[i][j] + list[i][j+1]
            temp_ls.append(sum)

        list.append(temp_ls)

    print(list)

generate_pascal_triangle(5)