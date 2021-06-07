"""Implementing the Deep Q-Learning algorithm with a neural network."""

__author__ = "Florian Obernberger"
__all__ = []
__ref__ = "https://towardsdatascience.com/playing-connect\
    -4-with-deep-q-learning-76271ed663ca"

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers


def create_model():
    model = keras.models.Sequential()

    model.add(layers.Flatten())
    model.add(layers.Dense(50, activation='relu'))
    model.add(layers.Dense(50, activation='relu'))
    model.add(layers.Dense(50, activation='relu'))
    model.add(layers.Dense(50, activation='relu'))
    model.add(layers.Dense(50, activation='relu'))
    model.add(layers.Dense(50, activation='relu'))
    model.add(layers.Dense(50, activation='relu'))

    model.add(layers.Dense(7))

    return model


def compute_loss(logits, actions, rewards):
    neg_logprob = tf.nn.sparse_softmax_cross_entropy_with_logits(logits=logits, labels=actions)
    loss = tf.reduce_mean(neg_logprob * rewards)
    return loss


def train_step(model, optimizer, observations, actions, rewards):
    with tf.GradientTape() as tape:
        # Forward propagate through the agent network

        logits = model(observations)
        loss = compute_loss(logits, actions, rewards)
        grads = tape.gradient(loss, model.trainable_variables)

        optimizer.apply_gradients(zip(grads, model.trainable_variables))
