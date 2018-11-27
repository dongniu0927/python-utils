import tensorflow as tf
import numpy as np


def safe_get(name, *args, **kwargs):
    """ Same as tf.get_variable, except flips on reuse_variables automatically """
    try:
        return tf.get_variable(name, *args, **kwargs)
    except ValueError:
        tf.get_variable_scope().reuse_variables()
        return tf.get_variable(name, *args, **kwargs)


def dropout(layer, keep_prob=0.9, is_training=True, name=None):
    if is_training:
        return tf.nn.dropout(layer, keep_prob=keep_prob, name=name)
    else:
        return tf.add(layer, 0, name=name)


def init_weights(shape, name=None):
    shape = tuple(shape)
    weights = np.random.normal(scale=0.01, size=shape).astype('f')
    return safe_get(name, list(shape), initializer=tf.constant_initializer(weights), dtype=tf.float32)


def init_bias(shape, name=None):
    return safe_get(name, initializer=tf.zeros(shape, dtype=tf.float32))


def init_fc_weights_xavier(shape, name=None):
    fc_initializer = tf.contrib.layers.xavier_initializer(dtype=tf.float32)
    return safe_get(name, list(shape), initializer=fc_initializer, dtype=tf.float32)


def init_conv_weights_xavier(shape, name=None):
    conv_initializer = tf.contrib.layers.xavier_initializer_conv2d(dtype=tf.float32)
    return safe_get(name, list(shape), initializer=conv_initializer, dtype=tf.float32)