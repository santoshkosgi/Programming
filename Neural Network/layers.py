"""
This script has code related Layer class
"""

class Layer(object):
    def __init__(self, input_dim, output_dim, activation_function):
        self.input_dim = input_dim
        self.output_dim = output_dim
        self.w, self.b = self.initialise_weights()
        self.activation_function = activation_function
        self.x = None

    def initialise_weights(self):
        """
        This function initialises weights and biases. FOr now we will use some algorithm, but later on
        we might have to accept which algo to use
        @param input_dim: Input dimesnion to the layer
        @param output_dim: Output dimension to the layer
        @return: Weight and biases
        """
        pass

    def forward_pass(self, x):
        """
        This function does the forward pass given x. We have to store this x which can be used during backprop
        @param x: Data
        @return:
        """
        self.x = x

    def backward_pass(self, grad):
        """
        This function computes backward prop related to w, b and x, which can be passed to the previous layer.
        @param grad: grad from the top layer.
        @return: returns  gradients w.r.t w, b and x
        """
        pass


