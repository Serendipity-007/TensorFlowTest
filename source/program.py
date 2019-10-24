# Classifies images from the Fashion MNIST dataset

# https://www.tensorflow.org/tutorials/keras/classification

# Created 10/24/2019


# Setup
from __future__ import absolute_import, division, print_function, unicode_literals

# TensorFlow and tf.keras
import tensorflow as tf
from tensorflow import keras

# Helper libraries
import numpy as np
#import matplotlib.pyplot as plt


# Welcome
print("This program classifies images from the Fashion MNIST dataset following tutorial at https://www.tensorflow.org/tutorials/keras/classification")


# Test TensorFlow so far
print("\nTensorFlow version:")
print(tf.__version__)



# Import dataset and run tests

fashion_mnist = keras.datasets.fashion_mnist

(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()



# Following tutorial

class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']



# "Explore the data"

# https://www.tensorflow.org/tutorials/keras/classification#explore_the_data

print("\n(From the tutorial:) The following shows there are 60,000 images in the training set, with each image represented as 28 x 28 pixels:")
print(train_images.shape)



# Print the length of the dataset

print("\n(From the tutorial:) There are 60,000 labels in the training set:")
print(len(train_labels))



