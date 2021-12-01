from __future__ import annotations
from typing import Iterable

class Sudoku:
    """A mutable sudoku puzzle."""

    def __init__(self, puzzle: Iterable[Iterable]):
        self._grid: list[str] = []

        for puzzle_row in puzzle:
            row = ""

            for element in puzzle_row:
                row += str(element)

            self._grid.append(row)

    def place(self, value: int, x: int, y: int) -> None:
        """Place value at x,y."""
        pass

    def unplace(self, x: int, y: int) -> None:
        """Remove (unplace) a number at x,y."""
        pass

    def value_at(self, x: int, y: int) -> int:
        """Returns the value at x,y."""
        pass

    def options_at(self, x: int, y: int) -> Iterable[int]:
        """Returns all possible values (options) at x,y."""
        pass

    def next_empty_index(self) -> tuple[int, int]:
        """
        Returns the next index (x,y) that is empty (value 0).
        If there is no empty spot, returns (-1,-1)
        """
        pass

    def row_values(self, i: int) -> Iterable[int]:
        """Returns all values at i-th row."""
        pass


    def column_values(self, i: int) -> Iterable[int]:
        """Returns all values at i-th column."""
        pass

    def block_values(self, i: int) -> Iterable[int]:
        """
        Returns all values at i-th block.
        The blocks are arranged as follows:
        0 1 2
        3 4 5
        6 7 8
        """
        pass

    def is_solved(self) -> bool:
        """
        Returns True if and only if all rows, columns and blocks contain
        only the numbers 1 through 9. False otherwise.
        """
        pass

    def __str__(self) -> str:
        pass


def load_from_file(filename: str) -> Sudoku:
    """Load a Sudoku from filename."""
    puzzle: list[str] = ""

    with open(filename) as f:
        for line in f:

            # strip newline and remove all commas
            line = line.strip(",")
            line.join()
    puzzle = line
    
    return Sudoku(puzzle)