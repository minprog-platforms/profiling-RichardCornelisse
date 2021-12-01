from __future__ import annotations
from typing import Iterable, Sequence
import numpy as np
from numpy.core.fromnumeric import nonzero 


# class Sudoku:
#     """A mutable sudoku puzzle."""

#     def __init__(self, puzzle: Iterable[Iterable]):
#         self._grid: list[str] = []

#         for puzzle_row in puzzle:
#             row = ""

#             for element in puzzle_row:
#                 row += str(element)

#             self._grid.append(row)

#     def place(self, value: int, x: int, y: int) -> None:
#         """Place value at x,y."""
#         row = self._grid[y]
#         new_row = ""

#         for i in range(9):
#             if i == x:
#                 new_row += str(value)
#             else:
#                 new_row += row[i]

#         self._grid[y] = new_row

#     def unplace(self, x: int, y: int) -> None:
#         """Remove (unplace) a number at x,y."""
#         row = self._grid[y]
#         new_row = row[:x] + "0" + row[x + 1:]
#         self._grid[y] = new_row

#     def value_at(self, x: int, y: int) -> int:
#         """Returns the value at x,y."""

#         return int(self._grid[y][x])

#     def options_at(self, x: int, y: int) -> Iterable[int]:
#         """Returns all possible values (options) at x,y."""
#         options = [1, 2, 3, 4, 5, 6, 7, 8, 9]

#         # Remove all values from the row
#         for value in self.row_values(y):
#             if value in options:
#                 options.remove(value)

#         # Remove all values from the column
#         for value in self.column_values(x):
#             if value in options:
#                 options.remove(value)

#         # Get the index of the block based from x,y
#         block_index = (y // 3) * 3 + x // 3

#         # Remove all values from the block
#         for value in self.block_values(block_index):
#             if value in options:
#                 options.remove(value)

#         return options

#     def next_empty_index(self) -> tuple[int, int]:
#         """
#         Returns the next index (x,y) that is empty (value 0).
#         If there is no empty spot, returns (-1,-1)
#         """
#         # next_x, next_y = -1, -1

#         # for y in range(9):
#         #     for x in range(9):
#         #         if self.value_at(x, y) == 0 and next_x == -1 and next_y == -1:
#         #             next_x, next_y = x, y

#         # return next_x, next_y

#         for y in range(9):
#             for x in range(9):
#                 if int(self._grid[y][x]) == 0:
#                     return x, y

#         return -1, -1

#     def row_values(self, i: int) -> Iterable[int]:
#         """Returns all values at i-th row."""
#         return map(int, self._grid[i])


#     def column_values(self, i: int) -> Iterable[int]:
#         """Returns all values at i-th column."""
#         values = []

#         for j in range(9):
#             values.append(self.value_at(i, j))

#         return values

#     def block_values(self, i: int) -> Iterable[int]:
#         """
#         Returns all values at i-th block.
#         The blocks are arranged as follows:
#         0 1 2
#         3 4 5
#         6 7 8
#         """
#         values = []

#         x_start = (i % 3) * 3
#         y_start = (i // 3) * 3

#         for x in range(x_start, x_start + 3):
#             for y in range(y_start, y_start + 3):
#                 values.append(self.value_at(x, y))

#         return values

#     def is_solved(self) -> bool:
#         """
#         Returns True if and only if all rows, columns and blocks contain
#         only the numbers 1 through 9. False otherwise.
#         """
#         values = [1, 2, 3, 4, 5, 6, 7, 8, 9]

#         result = True

#         for i in range(9):
#             for value in values:
#                 if value not in self.column_values(i):
#                     result = False

#                 if value not in self.row_values(i):
#                     result = False

#                 if value not in self.block_values(i):
#                     result = False

#         return result

#     def __str__(self) -> str:
#         representation = ""

#         for row in self._grid:
#             representation += row + "\n"

#         return representation.strip()


# def load_from_file(filename: str) -> Sudoku:
#     """Load a Sudoku from filename."""
#     puzzle: list[str] = []

#     with open(filename) as f:
#         for line in f:

#             # strip newline and remove all commas
#             line = line.strip().replace(",", "")

#             puzzle.append(line)

#     return Sudoku(puzzle)

# def load_from_file(filename: str) -> Sudoku:
#     """Load a Sudoku from filename."""
#     puzzle: str = []

#     with open(filename) as f:
#         for line in f:

#             # strip newline and remove all commas
#             line = line.strip().replace(",", " ")
#             puzzle.append(line)
#         puzzle = "; ".join(puzzle)

#     return Sudoku(puzzle)





## test numpy -------------------------------







## test matrix -------------------------------

class Sudoku:
    """A mutable sudoku puzzle."""

    def __init__(self, puzzle: Iterable[Iterable]):
        self._grid: list[list[int]] = np.matrix(puzzle)

    def place(self, value: int, x: int, y: int) -> None:
        """Place value at x,y."""
        self._grid[y, x] = int(value)

    def unplace(self, x: int, y: int) -> None:
        """Remove (unplace) a number at x,y."""
        self._grid[y, x] = 0

    def value_at(self, x: int, y: int) -> int:
        """Returns the value at x,y."""
        return int(self._grid[y, x])

    def options_at(self, x: int, y: int) -> Iterable[int]:
        """Returns all possible values (options) at x,y."""
        options = {1, 2, 3, 4, 5, 6, 7, 8, 9}

        # # breakpoint()
        # # Remove all values from the row
        # # for i in range(9):
        # #     row_element = int(self._grid[y,i])
        # #     if row_element in options:
        # #         options.remove(row_element)

        # for value in self.row_values(y):
        #     if value in options:
        #         options.remove(value)


        # # breakpoint()
        # # Remove all values from the column
        # # for i in range(9):
        # #     col_element = int(self._grid[i,x])
        # #     if col_element in options:
        # #         options.remove(col_element)

        # for value in self.column_values(x):
        #     if value in options:
        #         options.remove(value)

        # # Get the index of the block based from x,y
        # block_index = (y // 3) * 3 + x // 3

        # # Remove all values from the block
        # for value in self.block_values(block_index):
        #     if value in options:
        #         options.remove(value)

        # breakpoint()


        # options = options - self.row_values(x) 

        # options = options - self.column_values(y)

        block_index = (y // 3) * 3 + x // 3

        # Remove all values from the block
        # for value in self.block_values(block_index):
        #     if value in options:
        #         options.remove(value)

        # options = options - self.block_values(block_index)

        options = options - self.row_values(x) - self.column_values(y) - self.block_values(block_index)

        breakpoint()
        
        return options

    def next_empty_index(self) -> tuple[int, int]:
        """
        Returns the next index (x,y) that is empty (value 0).
        If there is no empty spot, returns (-1,-1)
        """
        # if 0 in self._grid:
        #     location = np.where(self._grid == 0)
        #     y = location[0][0]
        #     x = location[1][0]
        #     return x, y 
        # return -1, -1

        location = np.where(self._grid == 0)
        y = location[0][0]
        x = location[1][0]

        return x, y 

    def row_values(self, i: int) -> Iterable[int]:
        """Returns all values at i-th row."""
        # return self._grid[i]

        # return self._grid[i].tolist()[0]

        values = set()
        for j in range(9):
            values.add(self._grid[i,j])
        return values

    def column_values(self, i: int) -> Iterable[int]:
        """Returns all values at i-th column."""
        # return self._grid[i:]

        # return self._grid[i:].tolist()

        # row_values = self._grid[i]
        # nonzero_values = row_values[np.nonzero(row_values)].tolist()[0]
        # return nonzero_values

        # col = []
        # for item in self._grid[i:].tolist():
        #     col.append(item[0])

        # return col

        values = set()
        for j in range(9):
            # location = i * 9 + j
            # values.add(self._grid[:,i].tolist()[j][0])
            values.add(self._grid[j,i])
        return values

    def block_values(self, i: int) -> Iterable[int]:
        """
        Returns all values at i-th block.
        The blocks are arranged as follows:
        0 1 2
        3 4 5
        6 7 8
        """
        # values = []

        # x_start = (i % 3) * 3
        # y_start = (i // 3) * 3

        # values = self._grid[y_start:y_start + 3, x_start:x_start + 3]
        # values = values[np.nonzero(values)].tolist()[0]

        # return values


        values = set()

        x_start = (i % 3) * 3
        y_start = (i // 3) * 3

        # for n in range(3):
        #     for m in range(3):
        #         values.add(self._grid[y_start:y_start + 3, x_start:x_start + 3].tolist()[m][n])

        # breakpoint()

        # for m in range(x_start,x_start + 3):
        #     for n in range(y_start,y_start + 3):
        #         values.add(self._grid.item(y_start)

        for x in range(x_start, x_start + 3):
            for y in range(y_start, y_start + 3):
                values.add(self._grid[y, x])

        return values

    def is_solved(self) -> bool:
        """
        Returns True if and only if all rows, columns and blocks contain
        only the numbers 1 through 9. False otherwise.
        """
        return np.all(self._grid)

    def __str__(self) -> str:
        representation = ""

        for i in range(9):
            for j in range(9):
                representation += str(self._grid[i,j])
            representation += "\n"

        return representation


def load_from_file(filename: str) -> Sudoku:
    """Load a Sudoku from filename."""
    puzzle: str = []

    with open(filename) as f:
        for line in f:

            # strip newline and remove all commas
            line = line.strip().replace(",", " ")
            puzzle.append(line)
        puzzle = "; ".join(puzzle)

    return Sudoku(puzzle)
