def print_pascals_triangle(n):
    triangle = []
    for i in range(n):
        row = [1] * (i + 1)
        if i > 1:
            for j in range(1, i):
                row[j] = triangle[i-1][j-1] + triangle[i-1][j]
        triangle.append(row)
        print(" " * (n-i-1), end="")
        print(" ".join(str(num) for num in row))

n = 5  # Example number of rows
print_pascals_triangle(n)
