'''
These are the "fixed" versions of the functions in basic_functions.py.
The comments describe the bugs that I intended to put in each function (there might be more I didn't notice!).
'''



# LOGIC ERROR - Uses floor division
def divide(a, b):
    """Divides two numbers

    Args:
        a (float): The dividend
        b (float): The divisor

    Returns:
        The Quotient of a and b
    """
    return a/b



# LOGIC ERROR - No temp variable when swapping
# LOGIC ERROR - Modifies the array in-place rather than copying it, modifying the copy, and returning the modified array
def swap_list_elements(list, first_index, second_index):
    '''Swaps two elements in a list and returns the new list without altering the original.

    Args:
        list (list): A list with the elements to be swapped.
        first_index (int): The index of the first element to be swapped.
        second_index (int): The index of the second element to be swapped.

    Returns:
        The updated list.
    '''
    new_list = list.copy()
    temp = new_list[first_index]
    new_list[first_index] = new_list[second_index]
    new_list[second_index] = temp
    return new_list



# RUNTIME ERROR - Iterates one element too far, causing it to access an index out of bounds
# LOGIC ERROR - Uses floor division
def find_list_average(list):
    """Returns the average of all numbers in a list and None if the list is empty.

    Args:
        list (list): A list containing numbers.

    Returns:
        Float: The average of all numbers in the list, None if the list is empty.
    """
    if (len(list) == 0):
        return None
    
    sum = 0
    for i in range(len(list)):
        sum = sum + list[i]
    return sum / len(list)



#RUNTIME ERROR - Compares the last element to the one after it, causing it to index out of bounds
#LOGIC ERROR - Returns false in the for loop, meaning it will return false if the first two elements are not equal
def has_equal_adjacent_elements(list):
    """Determines whether or not a list has at least two equal adjacent elements.

    Args:
        list (list): A list containing elements comparable for equality.

    Returns:
        bool: True if the list has equal adjacent elements. False otherwise.
    """
    for i in range(len(list) - 1):
        if (list[i+1] == list[i]):
            return True
    return False




#TEST FUNCTIONS HERE
def main():
    pass











#ignore
if (__name__ == "__main__"):
    main()