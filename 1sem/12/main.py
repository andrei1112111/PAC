import numpy as np


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def sigmoid_derivative(x):
    return x * (1 - x)


class Neuron:
    def __init__(self, inputs):
        self._weights = np.random.rand(inputs)
        self._bias = np.random.rand()
        self._output = None
        self._inputs = None
        self._delta = None

    def forward(self, inputs):
        self._inputs = np.array(inputs)
        self._output = sigmoid(np.dot(self._inputs, self._weights) + self._bias)
        return self._output

    def backward(self, error, learning_rate=0.1):
        self._delta = error * sigmoid_derivative(self._output)

        self._weights -= learning_rate * self._delta * self._inputs
        self._bias -= learning_rate * self._delta


class Model:
    def __init__(self):
        self.hidden = [Neuron(2) for _ in range(2)]
        self.output = Neuron(2)

    def forward(self, inputs):
        out_h = np.array([self.hidden[i].forward(inputs) for i in range(len(self.hidden))])
        out_o = self.output.forward(out_h)

        return out_o

    def backward(self, label):
        error = self.output._output - label
        self.output.backward(error)

        hidden_errors = self.output._delta * self.output._weights

        for i in range(len(self.hidden)):
            self.hidden[i].backward(hidden_errors[i])


test = [[[0.0, 0.0], 0.0], [[0.0, 1.0], 1.0], [[1.0, 0.0], 1.0], [[1.0, 1.0], 0.0]]
train = test

model = Model()

epoch = 10000

for _ in range(epoch):
    for X, label in train:
        y = model.forward(X)
        model.backward(label)

for X, label in test:
    y = model.forward(X)
    print(f"For {X} Predicted: {y} Label: {label}")
