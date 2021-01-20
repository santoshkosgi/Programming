"""
This script has implementations of various activation functions.
"""

import numpy as np


class Relu(object):
    def __init__(self):
        self.x = None

    def forward_pass(self, x):
        """
        This function does a forward pass of the reslu activation function
        @param x: Input X
        @return: Output
        """
        self.x = x
        return x * (x > 0)

    def backwardpass(self, grad):
        """
        This function computes the gradient of x w.r.t loss
        @param grad: gradient from above level
        @return: Gradient w.r.t to x
        """
        return (self.x>0) * grad


class Sigmoid(object):

    def __init__(self):
        self.x = None

    def forward_pass(self, x):
        """
        Forward pass. 1/(1+e.pow(-x)
        @param x: x
        @return: output of forward pass
        """
        self.x = x
        negative_x = -1 * x
        exp_x = np.exp(negative_x)
        one_plus_exp = 1 + exp_x
        return 1/one_plus_exp

    def backward_pass(self, grad):
        """
        Backward Pass
        @param x:
        @return:
        """

class softmax(object):
    """
    This class defines softmax function, which is typically used in last layer.
    """
    def __init__(self):
        self.x = None

    def forward_pass(self, x):
        """
        This is soft max function it sort of calculates probabilities given all the values.
        One reason why the scores are exploded using exponent is that, to make the differences larger.
        @param x: Input of dimension N * C, for each input score across all the classes
        @return: N * C, scores computed after exploding them.
        """
        self.x = x
        exp_x = np.exp(x)
        sum_x = np.sum(axis=1)
        return exp_x/sum_x

    def backward(self, grad, index):
        """
        This is backward pass of the softmax function. It accepts a grad from above layer and alos the correct class
        index for each of the sample.
        @param grad:
        @param index:
        @return:
        """
        pass


class tanhx(object):
    """
    This class defines forward and backward pass for the tanhx activation function.
    """
    def __init__(self):
        self.x = None

    def forward_pass(self, x):
        self.x = x
        negative_x = -1 * x
        exp_x_negative = np.exp(negative_x)
        exp_x = np.exp(self.x)
        return (exp_x - exp_x_negative)/(exp_x + exp_x_negative)

    def backward_pass(self, grad):
        """
        This function computes the backward pass of the tanh activation using the grad from the above layer and
        chain rule.
        @param grad: grad form the above layer.
        @return:
        """
        pass




