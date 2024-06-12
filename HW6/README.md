# MacroGrad MNIST Classification

This repository contains code for training and testing a simple neural network model using MacroGrad on the MNIST dataset.

## Requirements

- Python 3.x
- NumPy
- tqdm
- requests

## Usage

1. Clone the repository:

    ```bash
    git clone https://github.com/newcodevelop/micrograd.git
    cd micrograd
    ```

2. Run the `mnist.py` script:

    ```bash
    python mnist.py
    ```

## Description

- `mnist.py`: This script contains the main implementation of the neural network model, training loop, and testing procedure. It loads the MNIST dataset, defines the model architecture, loss function (cross-entropy loss), and training/testing routines.
- `data/`: This folder stores the downloaded MNIST dataset files.
- `macrograd/`: This folder contains the MacroGrad library code.
- `macrograd/engine.py`: This file contains the implementation of the `Value` class used for automatic differentiation.
- `macrograd/utils.py`: This file contains utility functions for fetching and reading the MNIST dataset files.
- `requirements.txt`: This file lists the required Python packages.

## References

- [MacroGrad GitHub Repository](https://github.com/newcodevelop/micrograd/)
- [MacroGrad MNIST Example Notebook](https://github.com/newcodevelop/micrograd/blob/main/03b-MacroGrad/mnist.ipynb)
- [MacroGrad Engine Implementation](https://github.com/newcodevelop/micrograd/blob/main/03b-MacroGrad/macrograd/engine.py)
- [Softmax with Cross-Entropy Loss](https://mattpetersen.github.io/softmax-with-cross-entropy)
