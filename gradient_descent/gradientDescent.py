import numpy as np
from icecream import ic
import time

# Gradient descent implementation from Real Python
def gradient_descent(gradient, start, learn_rate, n_iter=50, tolerance=1e-06):
    vector = start
    for _ in range(n_iter):
        diff = -learn_rate * gradient(vector)
        if np.all(np.abs(diff) <= tolerance):
            break
        vector += diff
    return vector

if __name__ == '__main__':
    start_time = time.perf_counter_ns()
    result = gradient_descent(gradient=lambda v: 2 * v, start=10.0, learn_rate=0.2)
    end_time = time.perf_counter_ns()
    ic(result)
    elapsed_time = end_time - start_time
    ic(elapsed_time)
