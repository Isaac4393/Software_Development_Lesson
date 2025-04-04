def add_constant(list, constant):
    """Adds a constant value to each list element as long as it isn't masked. Alters the original list.
    
    Args: 
        list (list): A list containing numerical data.
        constant (int): The constant added to non-masked elements.

    Returns:
        None
    """
    for i in range(len(list)):
        if (list[i] != 9999):
            list[i] += constant



def multiply_by_constant(list, constant):
    """Multiplies each list element by a constant as long as it isn't masked. Alters the original list.
    
    Args: 
        list (list): A list containing numerical data.
        constant (int): The constant that multiplies non-masked elements.

    Returns:
        None
    """
    for i in range(len(list)):
        if (list[i] != 9999):
            list[i] *= constant



def mask_element(list, index_to_mask):
    """Masks a list element by setting it equal to 9999. Alters the original list.
    
    Args:
        list (list): A list containing numerical data.
        index_to_mask (int): The index which will be set to 9999.

    Returns:
        None
    """
    list[index_to_mask] = 9999



#write a function that accurately finds the average of the data values while ignoring values less than 0.1 and masked values
def find_average(list):
    """Returns the average of a list's elements, exlcuding elements less than .1 and elements equal to 9999 (masked elements).
    For example, if given this list: [9999, 1, 2, 0, 3], this function should return 2.
 
    Args:
        list (list): A list containing numerical data, possibly with masked values.

    Returns:
        The average of elements not equal to 9999 and not less than 0.1
    """
    counted_elements = 0
    #test
    sum = 0
    for i in range(len(list)):
        element = list[i]
        if element != 9999 and element >= .1:
            sum += element
            counted_elements += 1
    return sum / counted_elements


#If there is time, write a function that makes a new list only containing the valid data points that are above average from the original list
def extract_valid_data(original_list):
    """Takes a list and returns a new list containing only the data points in the original array that were
    not less than 0.1, not equal to 9999, and above average.

    Args:
        original_list (list): A list containing possibly invalid data such as data less than 0.1 or equal to 9999 (masked)

    Returns:
        A list containing only the above-average valid data points from the original array.
    """
    original_list_average = find_average(original_list)
    new_list = []

    for i in range(len(original_list)):
        element = original_list[i]
        if element != 9999 and element >= .1 and element > original_list_average:
            new_list.append(element)
    return new_list