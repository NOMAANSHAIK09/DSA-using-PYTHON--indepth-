def selectionsort(A):
    n =len(A)
    for i in range(n-1):
        position = i
        print("position",position)
        for j in range(i+1,n):
            if A[j] < A[position]:
                position = j
                print("position j=",position)
        A[i], A[position] = A[position], A[i]
    return A    
A = [64, 25, 12, 22, 11]
print(selectionsort(A))
"""first set n len of array , start a loop in array till n-1 from 0 index, and set the position as i after an another loop itterating in array from i+1 means index 1 it 
compare both the index , and swap into each other"""


