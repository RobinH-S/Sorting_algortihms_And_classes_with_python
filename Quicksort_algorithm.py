#quicksort function
#Takes a list of numbers as parameter
def quicksort(list):
    #list for the bigger numbers in the parameter list to be stored
    bigger = []
    #list for the lower numbers in the parameter list to be stored
    smaller = []

    #middle value of the parameter list. used to divide the smaller from bigger numbers
    mid = len(list)//2 - 1
    pivot = list[mid]
    print(pivot)

    #for loop to iterate through all numbers in parameter list
    for el in list:
        #checking if the number is smaller than the pivot int
        if el > pivot:
            bigger.append(el)
        #checking if the number is bigger than the pivot int
        if el < pivot:
            smaller.append(el)

    #sorting the lists
    smaller.sort()
    bigger.sort()

    pivot = [pivot]
    #putting all the lists together.
    total = smaller +pivot+  bigger
    #printing the new sorted list
    print (total)


#list to be sorted
arr = [2,6,7,8,9,0,2,1,3,4,5,6,7,9,9,0,1,2,34,7,8,9,6786,996,5,433,12]

#calling the quick_sort function on the arr list
quicksort(arr)
