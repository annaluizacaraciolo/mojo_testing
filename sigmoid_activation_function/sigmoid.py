import math
import time
from icecream import ic

def sigmoid(x):
    return 1 / (1 + math.exp(-x))

if __name__ == "__main__":
    start_time = time.perf_counter_ns()
    result = sigmoid(1)
    end_time = time.perf_counter_ns()
    time_elapsed = end_time - start_time
    ic(result)
    ic(time_elapsed)
