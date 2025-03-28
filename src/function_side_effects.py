"""
All of these functions act on lists with numberical data. The array is meant to represent gathered data.
Let's assume the data is precipitation data, and we are trying to alter it and extract information from it.

There are three functions that can alter a list: add_constant, multiply_by_constant, and mask_element.
Your job is to read the documentation of these functions and write a function called find_average
that will always follow its documentation regardless of what the other functions do to a list.
"""




def add_constant(list, constant):
    """Adds a constant value to each list element as long as it isn't masked. Alters the original list.
    
    Args: 
        list (list): A list containing numerical data, possibly with masked values.
        constant (float): The constant added to non-masked elements.

    Returns:
        None
    """
    for i in range(len(list)):
        if (list[i] != 9999):
            list[i] -= constant


def multiply_by_constant(list, constant):
    """Multiplies each list element by a constant as long as it isn't masked. Alters the original list.
    
    Args: 
        list (list): A list containing numerical data, possibly with masked values.
        constant (float): The constant that multiplies non-masked elements.

    Returns:
        None
    """
    for i in range(len(list)):
        if (list[i] != 9999):
            list[i] *= constant


def mask_element(list, index_to_mask):
    """Masks a list element by setting it equal to 9999. Alters the original list.
    
    Args:
        list (list): A list containing numerical data, possibly with masked values.
        index_to_mask (int): The index which will be set to 9999.

    Returns:
        None
    """
    list[index_to_mask] = 9999



def find_average(list):
 """Returns the average of a list's elements, exlcuding elements less than .1 and elements equal to 9999 (masked elements).
 For example, if given this list: [9999, 1, 2, 0.99, 3], this function should return 2.
 
 Args:
    list (list): A list containing numerical data, possibly with masked values.

 Returns:
    The average of elements not equal to 9999 and not less than 0.1
 """
    #TODO: Your code goes here


#IMPLEMENT AND TEST THIS IF THERE IS TIME
def extract_valid_data(original_list):
    """Takes a list and returns a new list containing only only the data points in the original array that were
    not less than 0.1, not equal to 9999, and above average.

    Args:
        original_list (list): A list containing possibly invalid data such as data less than 0.1 or equal to 9999 (masked)

    Returns:
        A list containing only the above-average valid data points from the original array.
    """
    #TODO: Your code goes here