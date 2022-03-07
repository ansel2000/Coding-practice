#Code for merge sort

from array import array


def mergeSort(arr):
    if len(arr)>1:
        mid = len(arr)//2
        L=arr[:mid]
        R = arr[mid:]

        mergeSort(L)
        mergeSort(R)

        i=j=k=0

        while i <len(L) and j<len(R):
            if L[i]<R[j]:
                arr[k]=L[i]
                k+=1
                i+=1
            else:
                arr[k]=R[j]
                j+=1
                k+=1
        
        if i>= len(L):
            while j<len(R):
                arr[k]=R[j]
                j+=1
                k+=1
        elif j>=len(R):
            while i<len(L):
                arr[k]=L[i]
                k+=1
                i+=1
        
        return arr
        
if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]
    print("Given array is", end="\n")
    print(arr)
    print("Sorted array is: ", end="\n")
    a=mergeSort(arr)
    print(a)