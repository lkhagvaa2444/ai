import numpy as np
from tqdm import trange
import gzip
import struct
import os
import requests
from pathlib import Path
from macrograd.engine import Value
from macrograd.utils import fetch_mnist

def fetch(url):
    filename = url.split("/")[-1]
    folder = Path("data")
    path = folder / filename
    if not path.exists():
        folder.mkdir(parents=True, exist_ok=True)
        content = requests.get(url).content
        path.write_bytes(content)
    return path

def read_idx(filename):
    with gzip.open(filename, "rb") as f:
        zero, data_type, dims = struct.unpack(">HBB", f.read(4))
        shape = tuple(struct.unpack(">I", f.read(4))[0] for d in range(dims))
        return np.frombuffer(f.read(), dtype=np.uint8).reshape(shape)

def load_mnist():
    base_url = "http://yann.lecun.com/exdb/mnist/"
    files = ["train-images-idx3-ubyte.gz", "train-labels-idx1-ubyte.gz", 
             "t10k-images-idx3-ubyte.gz", "t10k-labels-idx1-ubyte.gz"]
    paths = [fetch(base_url + file) for file in files]
    return tuple(map(read_idx, paths))

def to_one_hot(labels, n):
    return np.eye(n)[labels]

def accuracy(y_true, y_pred):
    return np.mean(np.argmax(y_true, axis=-1) == np.argmax(y_pred, axis=-1))

class Model:
    def __init__(self):
        self.w = Value.randn((28*28, 10))
        self.b = Value.randn((10,))

    def parameters(self):
        return self.w, self.b

    def __call__(self, x):
        return x @ self.w + self.b

def cross_entropy_loss(y_true, y_pred):
    # Compute the softmax
    exps = np.exp(y_pred - np.max(y_pred, axis=-1, keepdims=True))
    softmax = exps / np.sum(exps, axis=-1, keepdims=True)

    # Compute the cross entropy loss
    ce_loss = -np.sum(y_true * np.log(softmax + 1e-9), axis=-1)

    return ce_loss.mean()

def train(model, x_train, y_train, epochs, batch_size, learning_rate):
    for epoch in range(epochs):
        permutation = np.random.permutation(len(x_train))
        x_train = x_train[permutation]
        y_train = y_train[permutation]
        for i in trange(0, len(x_train), batch_size):
            x_batch = x_train[i:i+batch_size]
            y_batch = y_train[i:i+batch_size]

            model.zero_grad()

            output = model(x_batch)
            loss = cross_entropy_loss(y_batch, output)

            loss.backward()

            for p in model.parameters():
                p.data -= learning_rate * p.grad

        print("Epoch {}, Loss: {:.4f}, Accuracy: {:.4f}".format(
            epoch+1, loss.item(), accuracy(y_batch, output)))

def test(model, x_test, y_test):
    output = model(x_test)
    loss = cross_entropy_loss(y_test, output)
    acc = accuracy(y_test, output)
    print("Test Loss: {:.4f}, Accuracy: {:.4f}".format(loss.item(), acc))

def main():
    x_train, y_train, x_test, y_test = load_mnist()
    x_train, x_test = x_train.reshape(-1, 28*28), x_test.reshape(-1, 28*28)
    y_train, y_test = to_one_hot(y_train, 10), to_one_hot(y_test, 10)

    model = Model()
    train(model, x_train, y_train, epochs=10, batch_size=64, learning_rate=0.1)
    test(model, x_test, y_test)

if __name__ == "__main__":
    main()
