"""
This function defines the loss functions.
"""

class svmloss(object):
    """
    This class has methods to compute loss, given x and y.
    """
    def __init__(self):
        self.x = None
        self.y = None

    def compute_loss(self, x, y):
        """
        X would be of dimension N * C and Y would be dimension N * 1.
        @param x:
        @param y:
        @return: Loss for each sample
        """
        pass

    def backward_pass(self):
        """
        Not sure about the signature as of now.
        @return:
        """
        pass

class crossentropyloss(object):

    def __init__(self):
        self.x = None
        self.y = None

    def compute_loss(self, x, y):
        pass

    def backward_pass(self):
        pass

class squarederrorloss(object):

    def __init__(self):
        self.x = None
        self.y = None

    def compute_loss(self, x, y):
        pass

    def backward_pass(self):
        pass

