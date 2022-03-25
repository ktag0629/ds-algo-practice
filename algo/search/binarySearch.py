"""Binary Search tree implementation 

When to use: usually a dead give away to why you wanna use is if 
you have a sorted array.

# Why use:

If you have a sorted array, you can cut down your runtime to 
O(log n), 

# What makes it a `binary` search tree?

You essentially cut down on your search space by half every iteration

# How does it work? 

Say you have sorted array, if you're search for a particular element, 
You go to the half-way mark, if it's less than that mark go left, 
if greater, go right. Then go to the half-way mark again. 

"""

def bin_search(elems, l, r, x):
    """ implementation of binary search using recursion
    Args:
        elems: list of elements to find the element
        l: left index (window that we're searching within)
        r: right index (window that we're searching within)
        x: element we're looking for

    Returns:
        index of where to find element, -1 if element not in array

    Raises:
        None
    """
    if r >= l: # return if r and l are the same val
        mid = l + (r - 1) // 2

        if elems[mid] == x:
            return mid

        elif elems[mid] > x:
            return bin_search(elems, l, mid-1, x)
        else:
            return bin_search(elems, mid+1, r, x)
    else: 
        return -1

def main():

    elems = [1,2,3,4,5,6,7,8,9,10]
    ans = bin_search(elems, 0, len(elems)-1, 2)
    print(ans)
    
if __name__== "__main__":
    main()
