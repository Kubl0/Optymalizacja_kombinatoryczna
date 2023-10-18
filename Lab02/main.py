import copy


def generate_matrix(matrix_size):
    global matrix
    matrix = {x: {y: 0 for y in range(matrix_size)} for x in range(matrix_size)}


def add_vertex():
    matrix[highest_vertex() + 1] = {x: 0 for x in range(len(matrix))}
    for elem in matrix:
        matrix[elem][highest_vertex()] = 0


def highest_vertex():
    return max(matrix.keys(), default=0)


def remove_vertex(v):
    if v in matrix:
        for i in range(len(matrix)):
            matrix[i].pop(v)
        matrix.pop(v)
    else:
        print("Vertex does not exist")


def print_matrix():
    for elem in matrix:
        print(elem, matrix[elem])


def add_edge(v1, v2):
    if v1 not in matrix or v2 not in matrix:
        print("Vertex does not exist")
        return
    matrix[v1][v2] = 1
    matrix[v2][v1] = 1


def remove_edge(v1, v2):
    if v1 in matrix and v2 not in matrix:
        print("Vertex does not exist")
    else:
        matrix[v1][v2] = 0
        matrix[v2][v1] = 0


def naive():
    matrix_list = []
    for elem in matrix:
        matrix_list.append(list(matrix[elem].values()))

    for i in range(len(matrix_list)):
        for j in range(len(matrix_list)):
            if matrix_list[i][j] == 1:
                for k in range(len(matrix_list)):
                    if matrix_list[j][k] == 1 and matrix_list[k][i] == 1:
                        print("Znaleziony cykl: " + str(i) + " " + str(j) + " " + str(k))
                        return True
    return False


def power_3():
    a = []
    for elem in matrix:
        a.append(list(matrix[elem].values()))

    result = multiply_matrices(multiply_matrices(a, a), a)

    helper = 0

    for i in range(len(result)):
        helper += result[i][i]
    helper = helper//6

    print("Liczba cykli: " + str(helper))
    return True if helper > 0 else False


def multiply_matrices(matrix_a, matrix_b):
    n = len(matrix_a)
    result_matrix = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            for k in range(n):
                result_matrix[i][j] += matrix_a[i][k] * matrix_b[k][j]

    return result_matrix



generate_matrix(4)
add_edge(0, 1)
add_edge(0, 2)
add_edge(1, 0)
add_edge(1, 2)
add_edge(2, 0)
add_edge(2, 1)

print_matrix()

print("\nNaive:")
print(naive())
print("\n")
print(power_3())
