def bubbleSort(arr):
    n = len(arr)

    for i in range(n):
        swapped = False
        # print("n :"+ str(n))
        # print("i :"+ str(i))
        # print("n-i-1 :"+ str(n-i-1))
        for j in range(0, n-i-1):
            # print("j :"+ str(j))
            # print("j :"+ str(arr[j]))
            # print("j+1 :"+ str(arr[j+1]))
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        
        
        if (swapped == False):
            break


if __name__ == "__main__":
    arr = [64, 34, 25, 25, 12, 22, 11, 90, 11]

    bubbleSort(arr)
    print("Sorted array: ")
    for i in range(len(arr)):
        print("%d" % arr[i], end= " ")