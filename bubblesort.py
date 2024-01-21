import time

def main():
    arr = [3,2,10,4,0,9]

    for i in range(len(arr)-1):
        for j in range(len(arr)-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]  
    #print(arr)  
        
if __name__ == "__main__":
    start_time = time.perf_counter_ns()
    main()
    end_time = time.perf_counter_ns()
    print("Real time Elapsed: {}".format(end_time - start_time))