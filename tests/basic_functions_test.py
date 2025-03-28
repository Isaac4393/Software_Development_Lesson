import pytest
#import src.basic_functions as bf
import src.basic_functions_fixed as bf



def test_divide():
    assert bf.divide(6, 3) == 2 #test some normal ints
    assert bf.divide(0, 5) == 0 #test zero in numerator
    assert bf.divide(5, 2) == 2.5 #test a foating point result
    assert bf.divide(1, 3) == 1/3 #test a repeating fraction result
    with pytest.raises(ZeroDivisionError): #test that dividing by zero raises a ZeroDivisionError
        bf.divide(1, 0)




def test_swap_list_elements():
    list = [10, 20, 30, 40, 50]

    #call the swap function on the list and make sure the original list is not changed
    bf.swap_list_elements(list, 2, 3)
    assert list == [10, 20, 30, 40, 50]

    #test what the function returns for some basic swaps
    assert bf.swap_list_elements(list, 0, 1) == [20, 10, 30, 40, 50]
    assert bf.swap_list_elements(list, 3, 4) == [10, 20, 30, 50, 40]
    assert bf.swap_list_elements(list, 2, 4) == [10, 20, 50, 40, 30]

    #test swapping with a list holding various data types
    new_list = ['dog', 'cat', 20, 30, True, False]
    assert bf.swap_list_elements(new_list, 0, 3) == [30, 'cat', 20, 'dog', True, False]
    assert bf.swap_list_elements(new_list, 4, 5) == ['dog', 'cat', 20, 30, False, True]
    assert bf.swap_list_elements(new_list, 1, 4) == ['dog', True, 20, 30, 'cat', False]

    #test that passing an index outside the bounds of the list raises an IndexError
    with pytest.raises(IndexError):
        bf.swap_list_elements(new_list, 1, 200)




def test_find_list_average():
    #set up lists that test different cases
    list1 = [1, 2, 3, 4, 5]
    list2 = [1.5, 2.5, 3.3, 4.4]
    list3 = [0, 100000, 12345, 66654, 90908]
    list4 = [0, 0, 0]
    list5 = [-1, 3, 5]
    list6 = []

    #test the averages
    assert bf.find_list_average(list1) == 3
    assert bf.find_list_average(list2) == 2.925
    assert bf.find_list_average(list3) == 53981.4
    assert bf.find_list_average(list4) == 0
    assert bf.find_list_average(list5) == 7/3
    assert bf.find_list_average(list6) == None




def test_has_equal_adjacent_elements():
    #set up lists that test different cases
    list1 = [1, 2, 3, 4, 5]
    list2 = [1, 1, 2, 3, 4, 5]
    list3 = [1, 2, 3, 4, 5, 5]
    list4 = ['cat', 'dog', 'rainbow']
    list5 = [1, 2, False, False, True]
    list6 = [1, 2, 'hello', 'hello', 3]

    #test the results
    assert bf.has_equal_adjacent_elements(list1) == False
    assert bf.has_equal_adjacent_elements(list2) == True
    assert bf.has_equal_adjacent_elements(list3) == True
    assert bf.has_equal_adjacent_elements(list4) == False
    assert bf.has_equal_adjacent_elements(list5) == True
    assert bf.has_equal_adjacent_elements(list6) == True