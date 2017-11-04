def __init__(self, input_nodes, hidden_nodes, output_nodes, learning_rate):
    # set number of nodes in each input, hidden, output layer
    self.input_nodes = input_nodes
    self.hidden_nodes = hidden_nodes
    self.output_nodes = output_nodes

    # learning rate
    self.learning_rate = learning_rate
    pass


input_nodes = 3
hidden_nodes = 3
output_nodes = 3
learning_rate = 0.3

n = neuralNetwork(input_nodes, hidden_nodes, output_nodes, learning_rate)
