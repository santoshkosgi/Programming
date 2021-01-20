"""
This script has methods to normalise input data.
"""
import numpy as np
class Standadization(object):
    """
    This class has methods to do zero mean and unit variance normalisation.
    """
    def __init__(self):
        self.x = None

    def normalise(self, x):
        """
        @param x: input
        @return: Normalised data
        """
        self.x = x
        mean = np.sum(x, axis=0)
        N, C = self.x.shape
        mean /= N
        variance = self.x - mean
        variance *= variance
        variance = np.sum(variance, axis=0)
        variance /= N
        std = np.sqrt(variance)
        return ((self.x - mean)/std)

class MinMaxScalar(object):
    """
    This class has methods to do min max scaling. This scales each of the feature of data between zero and one
    """
    def __init__(self):
        self.x = None

    def normalise(self, x):
        self.x = x
        max_element = np.max(x, axis=0)
        min_element = np.min(x, axis=0)
        return (self.x - min_element)/(max_element - min_element)
