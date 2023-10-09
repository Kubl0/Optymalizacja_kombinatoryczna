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


def sum_of_edges():
    sums = {v: sum(matrix[v].values()) for v in matrix}
    sorted_sums = dict(sorted(sums.items(), key=lambda item: item[1], reverse=True))
    return sorted_sums


def highest_sum():
    sums = sum_of_edges()
    highest = max(sums.items(), key=lambda item: item[1])
    return {highest[0]: highest[1]}


def lowest_sum():
    sums = sum_of_edges()
    lowest = min(sums.items(), key=lambda item: item[1])
    return {lowest[0]: lowest[1]}


def amount_of_even_and_odd():
    even = sum(1 for v in matrix if sum(matrix[v].values()) % 2 == 0)
    odd = len(matrix) - even
    return {"even": even, "odd": odd}


size = int(input("Enter the size of the matrix: "))
generate_matrix(size)

while True:
    print("1. Add vertex")
    print("2. Remove vertex")
    print("3. Add edge")
    print("4. Remove edge")
    print("5. Print matrix")
    print("6. Sum of edges")
    print("7. Highest sum")
    print("8. Lowest sum")
    print("9. Amount of even and odd")
    print("10. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        add_vertex()
    elif choice == 2:
        vertex = int(input("Enter the vertex to remove: "))
        remove_vertex(vertex)
    elif choice == 3:
        vertex1 = int(input("Enter the first vertex: "))
        vertex2 = int(input("Enter the second vertex: "))
        add_edge(vertex1, vertex2)
    elif choice == 4:
        vertex1 = int(input("Enter the first vertex: "))
        vertex2 = int(input("Enter the second vertex: "))
        remove_edge(vertex1, vertex2)
    elif choice == 5:
        print_matrix()
    elif choice == 6:
        print(sum_of_edges())
    elif choice == 7:
        print(highest_sum())
    elif choice == 8:
        print(lowest_sum())
    elif choice == 9:
        print(amount_of_even_and_odd())
    elif choice == 10:
        break
    else:
        print("Invalid choice")
