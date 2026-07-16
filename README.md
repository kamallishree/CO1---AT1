**QUESTION 1 ** 
Algorithm: Merge Sort
START
Input the array
Call MergeSort(array)
Function MergeSort(array)

    If size of array is less than or equal to 1
        Return array

    Find the middle index

    Divide the array into Left and Right halves

    Left = MergeSort(Left half)

    Right = MergeSort(Right half)

    Return Merge(Left, Right)

Function Merge(Left, Right)

    Create an empty Result array

    Compare the first elements of Left and Right

    Add the smaller element to Result

    Repeat until one array becomes empty

    Add the remaining elements of Left

    Add the remaining elements of Right

    Return Result

Display the sorted array
STOP


**QUESTION 2 **
Algorithm: Search Engine Index Builder
START
Input n
Function IndexBuilder(n)

    If n is less than or equal to 1
        Return 1

    Return IndexBuilder(n / 2) + 1

Call IndexBuilder(n)
Display the number of operations
STOP
