"""
name: sudoku.py

author:             Rick Cornelisse
student number:     12367885

Helper file for solve.py
Contains:
- the class of a Sudoku
- the function to load a sudoku from text: def load_from_file
"""

from __future__ import annotations
from typing import Iterable
import numpy as np


class Sudoku:
    """A mutable sudoku puzzle."""

    def __init__(self, puzzle: Iterable[Iterable]):
        self._grid: np.array[np.array[int]] = np.array(puzzle)

    def place(self, value: int, x: int, y: int) -> None:
        """Place value at x,y."""
        self._grid[y, x] = int(value)

    def unplace(self, x: int, y: int) -> None:
        """Remove (unplace) a number at x,y."""
        self._grid[y, x] = 0

    def value_at(self, x: int, y: int) -> int:
        """Returns the value at x,y."""
        return self._grid[y, x]

    def options_at(self, x: int, y: int) -> Iterable[int]:
        """Returns all possible values (options) at x,y."""
        options = {1, 2, 3, 4, 5, 6, 7, 8, 9}

        # computes in which of the nine blocks it is
        block_index = (y // 3) * 3 + x // 3

        # use the union of row, column and blockvalues to eliminate the possible options left
        used = set.union(self.row_values(y), self.column_values(x), self.block_values(block_index))
        options_left = options - used

        return options_left

    def next_empty_index(self) -> tuple[int, int]:
        """Returns the next index (x,y) that is empty (value 0)."""
        location = np.where(self._grid == 0)
        y = location[0][0]
        x = location[1][0]

        return x, y 

    def row_values(self, i: int) -> Iterable[int]:
        """
        Returns all used values at i-th row.
        As values can only occur once it adds nonduplicates to a set for every entry.
        """
        values = set()
        for j in range(9):
            values.add(self.value_at(j,i))

        return values

    def column_values(self, j: int) -> Iterable[int]:
        """
        Returns all values at j-th column.
        As values can only occur once it adds nonduplicates to a set for every entry.
        """
        values = set()
        for i in range(9):
            values.add(self.value_at(j,i))

        return values

    def block_values(self, i: int) -> Iterable[int]:
        """
        Returns all values at i-th block.
        As values can only occur once it adds nonduplicates to a set for every entry.
        The blocks are arranged as follows:
        0 1 2
        3 4 5
        6 7 8
        """
        values = set()

        # compute the starting values for each block
        x_start = (i % 3) * 3
        y_start = (i // 3) * 3

        # go through every entry of the block and add to the set
        for x in range(x_start, x_start + 3):
            for y in range(y_start, y_start + 3):
                values.add(self.value_at(x,y))

        return values

    def is_solved(self) -> bool:
        """
        Returns True if and only if all rows, columns and blocks contain
        only the numbers 1 through 9. False otherwise.
        """
        return np.all(self._grid)

    def __str__(self) -> str:
        """Formats the sudoku such that it can be printed."""
        representation = ""

        for i in range(9):
            for j in range(9):
                representation += str(self.value_at(j,i))
            representation += "\n"

        return representation


def load_from_file(filename: str) -> Sudoku:
    """Load a Sudoku from filename."""
    # create a zero/null matrix (2D numpy array) as "blank board"
    puzzle: np.array = np.zeros((9,9), dtype=int)

    with open(filename) as f:
        row = 0
        for line in f:
            # strip the line such that only sudoku values remain
            line = line.strip().replace(",","")

            # put each value in its designated position as an integer
            col = 0
            for item in line:
                puzzle[row][col] = int(item)
                col += 1

            # update the next row to fill
            row += 1

    return Sudoku(puzzle)