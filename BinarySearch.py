def binarySearch(list,item):
    list = sorted(list)
    first = 0
    last = len(list)-1
    found=False
    while first <= last and not found:
        mid = (first+last)//2
        if list[mid] == item: 
            found=True
            print("This item is on position: " + str(mid+1))
        elif item < list[mid]: 
            last = mid-1
        else: first = mid+1
    return(list)


list = [2,6,22,41,50,53,67,76,34,87,9,34,23,98,12,56]
print(binarySearch(list, 53))