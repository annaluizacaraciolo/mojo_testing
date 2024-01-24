from math import exp
from python import Python


fn sigmoid(x: Float64) -> Float64:
    return 1 / (1 + exp(-x))

fn main() raises:
    let time = Python.import_module('time')
    let start_time = time.perf_counter_ns()
    let result = sigmoid(1)
    let end_time = time.perf_counter_ns()
    let time_elapsed = end_time - start_time
    print(result)
    print(time_elapsed)

    