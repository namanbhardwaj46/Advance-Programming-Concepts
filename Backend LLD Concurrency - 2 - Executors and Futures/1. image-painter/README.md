# Parallel Matrix Painting

## Problem Statement
You are tasked with creating a Python program that can divide a matrix into quadrants and paint each quadrant with a different color using parallel processing. The program should leverage the concurrent.futures module to achieve parallelism and improve performance.

## Requirements
The program should include the following components:

1. paint_quadrant function:
    - Takes a matrix, start and end row indices, start and end column indices, and a color as input.
    - Paints the specified quadrant of the matrix with the given color.
2. divide_and_paint function:
    - Takes a matrix and a list of colors as input.
    - Divides the matrix into four quadrants (top-left, top-right, bottom-left, bottom-right).
    - Utilizes the concurrent.futures.ThreadPoolExecutor to create four separate threads.
    - Each thread calls the paint_quadrant function with the corresponding quadrant and color.
    - Waits for all threads to complete before returning.
3. Example usage:
    - Creates a sample 4x4 matrix.
    - Calls the divide_and_paint function with the matrix and a list of four colors.
    - Prints the painted matrix.

## Instructions
- Implement the paint_quadrant function according to the specified requirements.
- Implement the divide_and_paint function, which creates a thread pool executor and submits tasks to paint each quadrant in parallel.