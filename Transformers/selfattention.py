"""
This script has methods to implement self attention using pytorch
"""
import torch
from torch import nn
import torch.nn.functional as F
import math


class SelfAttention(nn.Module):
    def __init__(self, input_dimension, attention_heads):
        super().__init__()
        self.input_dimension = input_dimension
        self.attention_heads = attention_heads
        self.query_layer = nn.Linear(in_features=input_dimension, out_features=input_dimension)
        self.key_layer = nn.Linear(in_features=input_dimension, out_features=input_dimension)
        self.value_layer = nn.Linear(in_features=input_dimension, out_features=input_dimension)

    def compute_weight_matrices(self, X):
        """
        This function computes query, key and value matrices for each head.
        Then it computes weights for each output yj.
        X: Input data. This is of dimension batch * sequence_length * input_dimension
        @return:
        """
        batch_size, sequence_length, input_dimension = X.size()
        query_data = self.query_layer(X)
        key_data = self.key_layer(X)
        value_data = self.value_layer(X)
        W = torch.bmm(query_data, value_data.view(batch_size, input_dimension, sequence_length))
        # Dividing by square root of input dimension size. not completely clear why am i doing this ?
        W = W/math.sqrt(input_dimension)
        # Computing Softmax of W matrix
        W = F.softmax(W, dim=2)
        output = torch.bmm(W, value_data)
        return output

    def forward(self, X):
        """
        This function computes the output vectors using self attention.
        @param X: Input vector of dimension batch * sequence_length * input_dimension
        @return: Output vector of dimension batch * sequence_length * input_dimension
        """
        output = self.compute_weight_matrices(X)
        return output

if __name__ == '__main__':
    X = torch.rand((10, 20, 3))
    attention = SelfAttention(input_dimension=3, attention_heads=1)
    attention.forward(X)