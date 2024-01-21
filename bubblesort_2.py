import time

def main():
    arr = [3,2,10,4,0,9]

    for i in range(len(arr)-1):
        for j in range(len(arr)-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]  
    #print(arr)  
                

if __name__ == "__main__":
    start_time_2 = time.process_time_ns()
    main()
    end_time_2 = time.process_time_ns()
    print("Time taken only by the process: {}".format(end_time_2 - start_time_2))