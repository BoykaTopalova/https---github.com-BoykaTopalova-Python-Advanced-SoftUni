# Python3 implementation to sort
# the given matrix

SIZE = 10


# Function to sort the given matrix
def sortMat(mat, n):
    # Temporary matrix of size n^2
    temp = [0] * (n * n)
    k = 0

    # Copy the elements of matrix
    # one by one into temp[]
    for i in range(0, n):

        for j in range(0, n):
            temp[k] = mat[i][j]
            k += 1

    # sort temp[]
    temp.sort()

    # copy the elements of temp[]
    # one by one in mat[][]
    k = 0

    for i in range(0, n):

        for j in range(0, n):
            mat[i][j] = temp[k]
            k += 1


# Function to print the given matrix
def printMat(mat, n):
    for i in range(0, n):

        for j in range(0, n):
            print(mat[i][j], end=" ")

        print()

    # Driver program to test above


mat = [[5, 4, 7],
       [1, 3, 8],
       [2, 9, 6]]
n = 3

print("Original Matrix:")
printMat(mat, n)

sortMat(mat, n)

print("\nMatrix After Sorting:")
printMat(mat, n)
