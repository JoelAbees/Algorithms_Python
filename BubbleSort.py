def bubbleSort(list):
    for i in range(len(list)-1,0,-1):
        print("Value of i = " + str(i))
        for j in range(i):
            print("Value of j = " + str(j))
            if list[j]>list[j+1]:
                list[j] , list[j+1] = list[j+1] , list [j]
            
            print(list)
    
    print("Final sorted list: ")
    print(list)    




listk = [2,7,3,5,4,1]      
bubbleSort(listk) 
print(listk)