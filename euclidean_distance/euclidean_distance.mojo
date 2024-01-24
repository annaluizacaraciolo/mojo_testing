from math import sqrt
from math import pow
from time import now

fn euclidean_dist(x1: Int64, y1: Int64, x2: Int64, y2: Int64):
    let x = x2 - x1
    let y = y2 - y1
    let euclidean_distance = sqrt(pow(x, 2) + pow(y,2))
    print(euclidean_distance)

fn main():
    # time measured in nanoseconds
    let start_time = now()
    euclidean_dist(3, 12, 7, 19)
    let end_time = now()
    print(end_time - start_time)
    
   
    

   
    