"""
Handles the ai model using the ``tensorflow.keras`` library as a base.

Resources
--------

* https://www.tensorflow.org/guide/keras/sequential_model
"""

# %%

__author__ = "Florian Obernberger"

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

from game_board import Board


def create_model(layer_size: int = 20,
                 layer_count: int = 6) -> keras.models.Sequential:
    """Creates a ``keras.Sequential`` model with the given params.

    Parameters
    ----------
    layer_size : optional
        The size of one layer, by default 20.
    layer_count : optional
        [description], by default 6.

    Returns
    -------
    keras.models.Sequential
        Returns the created module.
    """
    board_area: int = Board._height * Board._width
    model = keras.models.Sequential([
        layers.Dense(board_area, name='board-input', activation='relu'), *[
            layers.Dense(
                layer_size, name=f'hidden-layer-{n}', activation='relu')
            for n in layer_count
        ]
    ])

    return model


# %%
if __name__ == "__main__":
    ...
