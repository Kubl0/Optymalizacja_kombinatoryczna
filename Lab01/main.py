def generate_matrix(matrixSize):
    global matrix
    matrix = {x: {y: 0 for y in range(matrixSize)} for x in range(matrixSize)}


def add_vertex():
    matrix[highest_vertex() + 1] = {x: 0 for x in range(len(matrix))}
    for elem in matrix:
        matrix[elem][highest_vertex()] = 0


def highest_vertex():
    highest = 0
    for elem in matrix:
        if elem > highest:
            highest = elem
    return highest


def remove_vertex(vertex):
    for i in range(len(matrix)):
        matrix[i].pop(vertex)
    matrix.pop(vertex)


def print_matrix():
    for elem in matrix:
        print(elem, matrix[elem])


def add_edge(vertex1, vertex2):
    matrix[vertex1][vertex2] = 1
    matrix[vertex2][vertex1] = 1


def remove_edge(vertex1, vertex2):
    matrix[vertex1][vertex2] = 0
    matrix[vertex2][vertex1] = 0


def sum_of_edges():
    sums = {}
    for elem in matrix:
        sums[elem] = sum(matrix[elem].values())
    return sums


def highest_sum():
    sums = sum_of_edges()
    highest = max(sums.values())
    return highest


def lowest_sum():
    sums = sum_of_edges()
    lowest = min(sums.values())
    return lowest



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
    print("9. Exit")
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
        break
    else:
        print("Invalid choice")
