def binarySearch(arr,x,l,h):
    if l > h:
        return -1
    mid = (l + h)//2

    if (arr[mid] == x):
        return mid
    elif(arr[mid]>x):
        return binarySearch(arr,x,l,mid-1)
    else:
        return binarySearch(arr,x,mid+1,h)

print(binarySearch([1,2,3,4,5,6,8,9],6,0,8))                 