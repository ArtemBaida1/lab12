def print_diamond(width, height):
    for i in range(height // 2):
        print(" " * (width // 2 - i) + "*" * (2 * i + 1))
    for i in range(height // 2, -1, -1):
        print(" " * (width // 2 - i) + "*" * (2 * i + 1))

print_diamond(7, 7)
