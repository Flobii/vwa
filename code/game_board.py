"""
This module handles the game board.

TODO
----
* Add `win_test()` function to `Board` class
"""

# %%

from __future__ import annotations

__author__ = "Florian Obernberger"
__all__ = ['Board', 'Position', 'Stone']

from typing import List, NamedTuple, Tuple
from enum import IntEnum
import numpy as np
from numba import njit


class Position(NamedTuple):
    """A position consisting of a `x` and a `y` Value.
    Inherits from `NamedTuple`.

    Parameters
    ----------
    x : int
        Posiition in `x` direction.
    y : int
        Position in `y` direction.
    """
    x: int
    y: int = 0

P = Position  # Set alias for `Position`

class Stone(IntEnum):
    empty: int = 0
    p_red: int = 1
    p_yel: int = 2
    _mark: int = 9


WIDTH: int = 7
HEIGHT: int = 6


class Board:
    """Creates a connect four gameboard and handles wintesting.
    """
    __slots__ = ['board']

    def __init__(self) -> None:
        self.board: List[List[int]] = np.zeros((HEIGHT, WIDTH), dtype=np.int8)

    def drop(self) -> None:
        """Automatically drops every Stone in the board to the lowest
        possible position.
        """
        for _ in range(HEIGHT + 1):
            for row_number in range(HEIGHT - 1, -1, -1):
                for stone_pos in range(len(self.board[row_number])):
                    try:
                        if self.board[row_number][stone_pos] != Stone.empty \
                            and self.board[row_number + 1][stone_pos] == Stone.empty:
                            self.board[row_number + 1][stone_pos] = self.board[
                                row_number][stone_pos]
                            self.board[row_number][stone_pos] = Stone.empty
                    except IndexError:
                        ...  # who cares?

    def win_test(self) -> Tuple[True, Stone]:
        ...

    def __eq__(self, other: Board):
        return self.board == other.board

    def __setitem__(self, key, value):
        self.board[key] = value

    def __getitem__(self, key) -> Stone:
        return self.board[key]

    def set(self, pos: Position, stone: Stone, static: bool = False) -> None:
        """Place a Stone on the board at the given Position.

        Parameters
        ----------
        pos
            The Position of the Stone.
        stone
            The type of Stone to be placed.
        static : optional
            If True calls `self.drop`, by default False.
        """
        self.board[pos.y][pos.x] = np.intp(stone)
        if not static:
            self.drop()

    def get(self, pos: Position) -> Stone:
        """Get the type of Stone at the given Position.

        Parameters
        ----------
        pos
            The Position of the Stone.

        Returns
        -------
        Stone
            The type of Stone.
        """
        return Stone(self.board[pos.y][pos.x])

    def __repr__(self) -> str:
        return str(self.board)


# %%
if __name__ == "__main__":
    board = Board()
    board.set(P(1), Stone.p_red)
    board.set()
    print(board)

# %%
