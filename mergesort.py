def merge(arr):
    n=len(arr)
    m=int(len(arr)/2)
    l=arr[:m]
    r=arr[m:]
    i=j=0
    k=0
    while i<len(l) and j<len(r):
        if l[i]<r[j]:
            arr[k]=l[i]
            i+=1
        else:
            arr[k]=r[j]
            j+=1
        k+=1

    while i<len(l):
        arr[k]=l[i]
        i=i+1
        k=k+1

    while j<len(r):
        arr[k]=r[j]
        j=j+1
        k=k+1

if __name__=="__main__":
    n=int(input("enter the size of array"))
    print("size of array is",n)
    arr=[]
    p=0

    for i in range(0,n):
        print("enter element",i+1,end="\t")
        p=int(input())
        arr.append(p)

    print("Array is",end="")
    for i in range (0,n):
        print(end="\t")
        print("%d" %arr[i],end="\t")
    print("\narray after sorting")
    merge(arr)
    for i in range(0,n):
        print("%d" %arr[i])
    
        
