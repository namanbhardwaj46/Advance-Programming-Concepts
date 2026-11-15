import concurrent.futures

def paint_quadrant(matrix, start_row, end_row, start_col, end_col, color):
    # Todo
    for r in range(start_row, end_row):
        for c in range(start_col, end_col):
            matrix[r][c] = color

def divide_and_paint(matrix, colors):
    # Todo
    rows = len(matrix)
    cols = len(matrix[0])
    mid_r = rows // 2
    mid_c = cols // 2

    # (start_row, end_row, start_col, end_col) for each quadrant
    quadrants = [
        (0, mid_r, 0, mid_c),       # top-left
        (0, mid_r, mid_c, cols),    # top-right
        (mid_r, rows, 0, mid_c),    # bottom-left
        (mid_r, rows, mid_c, cols), # bottom-right
    ]

    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        futures = [
            executor.submit(paint_quadrant, matrix, start_row, end_row, start_col, end_col, color)
            for (start_row, end_row, start_col, end_col), color in zip(quadrants, colors)
        ]

        # wait for all four tasks; result() also re-raises any exception from a thread
        for f in futures:
            f.result()


# Example usage:
matrix = [[0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]]

# color is given
colors = ["red","blue","green","yellow"]

divide_and_paint(matrix, colors)

# Print the painted matrix
for row in matrix:
    print(row)