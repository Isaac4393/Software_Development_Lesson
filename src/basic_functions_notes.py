import pytest




# LOGIC ERROR - floor division
def divide(a, b):
    """Divides two numbers

    Args:
        a (float): The dividend
        b (float): The divisor

    Returns:
        The Quotient of a and b
    """
    return a//b



# Logic error - no temp variable
def swap_two_list_elements(list, first_index, second_index):
    '''Swaps two elements in a list.

    Args:
        list (list): A list with the elements to be swapped.
        first_index (int): The index of the first element to be swapped.
        second_index (int): The index of the second element to be swapped.

    Returns:
        None
    '''
    list[first_index] = list[second_index]
    list[second_index] = list[first_index]



# LOGIC ERROR - incorrect indexing when finding sum
def find_list_average(list):
    """Returns the average of all numbers in a list, returns None if the list is empty.

    Args:
        list (list): A list containing numbers.

    Returns:
        Float: The average of all numbers in the list, None if the list is empty.
    """
    highest_index = len(list) - 1 #find the highest index in the list
    sum = 0

    for i in range(highest_index):
        sum = sum + list[i]
    return sum / len(list)



# Runtime error - checks index out of range if it gets to the last element without finding a pair
# Logic error - the else statement in the for loop is incorrect
def has_equal_adjacent_elements(list):
    """Determines whether or not a list has at least two equal adjacent elements.

    Args:
        list (list): A list containing elements comparable for equality.

    Returns:
        bool: True if the list has equal adjacent elements. False otherwise.
    """
    for i in range(len(list)):
        if (list[i+1] == list[i]):
            return True
        else:
            return False
    return False





def main():
    pass







if __name__ == "__main__":
    main()