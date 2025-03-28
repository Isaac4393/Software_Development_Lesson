'''
All of these functions have at least one bug that causes them to not work according to the documentation.
Play around with print testing in the main function, and try to get them working without using higher-level Python functions like sum().
This will force you to think about possible edge cases.
'''



def divide(a, b):
    """Divides two numbers

    Args:
        a (float): The dividend
        b (float): The divisor

    Returns:
        The Quotient of a and b
    """
    return a//b




def swap_list_elements(list, first_index, second_index):
    '''Swaps two elements in a list and returns the new list without altering the original.

    Args:
        list (list): A list with the elements to be swapped.
        first_index (int): The index of the first element to be swapped.
        second_index (int): The index of the second element to be swapped.

    Returns:
        The updated list.
    '''
    list[first_index] = list[second_index]
    list[second_index] = list[first_index]




def find_list_average(list):
    """Returns the average of all numbers in a list and None if the list is empty.

    Args:
        list (list): A list containing numbers.

    Returns:
        Float: The average of all numbers in the list, None if the list is empty.
    """
    sum = 0
    for i in range(len(list) + 1):
        sum = sum + list[i]
    return sum // len(list)




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







#TEST FUNCTIONS HERE
def main():
    pass











#ignore
if (__name__ == "__main__"):
    main()