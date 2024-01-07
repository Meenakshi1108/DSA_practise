# def lcis_recursive(arr1, arr2, i, j, prev):
#     if i == len(arr1) or j == len(arr2):
#         return 0
    
#     # If the current elements are equal
#     if arr1[i] == arr2[j] and arr1[i] >= prev:
#         return 1 + lcis_recursive(arr1, arr2, i+1, j+1, arr1[i])
    
#     # # If the current element in arr2 is less than the previous element in arr1
#     # if arr2[j] <= prev:
#     #     return lcis_recursive(arr1, arr2, i, j+1, prev)
    
#     # # If the current element in arr1 is less than the previous element in arr2
#     # if arr1[i] <= prev:
#     #     return lcis_recursive(arr1, arr2, i+1, j, prev)
    
#     # If none of the above conditions are met
#     return max(lcis_recursive(arr1, arr2, i+1, j, prev), lcis_recursive(arr1, arr2, i, j+1, prev))

# a1 = [1,2,0,2,1] 
# a2 = [1,0,1]

# result_recursive = lcis_recursive(a1, a2, 0, 0, float('-inf'))
# print("Length of LCIS (Recursive) is:", result_recursive)


def LCIS(arr1, n, arr2, m):
    # table[j] is going to store length of LCIS
    # ending with arr2[j]. We initialize it as 0.
    table = [0] * m
    for j in range(m):
        table[j] = 0

    # Traverse all elements of arr1[]
    for i in range(n):
        # Initialize the current length of LCIS
        current = 0

        # For each element of arr1[], 
        # traverse all elements of arr2[].
        for j in range(m):
            # If both arrays have the same elements.
            # Note that we don't break the loop here.
            if (arr1[i] == arr2[j]):
                if (current + 1 > table[j]):
                    table[j] = current + 1

            # Now seek the previous smaller common
            # element for the current element of arr1 
            if (arr1[i] > arr2[j]):
                if (table[j] > current):
                    current = table[j] #if any element before,inc from that index   

        # Print the DP table at each step
        print(f"DP Table after processing element {arr1[i]}:")
        print(table)

    # The maximum value in table[] 
    # is our result
    result = 0
    for i in range(m):
        if (table[i] > result):
            result = table[i]

    return result

# Driver Code
if __name__ == "__main__":
    arr1 = [3, 4, 9, 1]
    arr2 = [5, 3, 8, 9, 10, 2, 1]

    n = len(arr1)
    m = len(arr2)

    print("Length of LCIS is", 
          LCIS(arr1, n, arr2, m))

    