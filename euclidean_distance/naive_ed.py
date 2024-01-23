import math
from icecream import ic
import time

def main():
    x1, y1, x2, y2 = 3, 12, 7, 19
    start_time = time.perf_counter_ns()
    euclidean_distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)
    end_time = time.perf_counter_ns()
    ic(euclidean_distance)
    time_elapsed = end_time - start_time
    ic(time_elapsed)
    
if __name__ == '__main__':
    main()