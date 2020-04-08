from drawing.line import print_line


def print_triangle(n):
    [print_line(r) for r in range(n)]
    [print_line(r) for r in range(n - 2, -1, -1)]
    # for row in range(n):
    #     print_line(row)
    # for row in range(n - 2, -1, -1):
    #     print_line(row)
