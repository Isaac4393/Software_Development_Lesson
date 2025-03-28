import pytest
import math
import src.function_side_effects_solution as fs







def test_add_constant():
    list1 = [1, 2, 3, 4, 5]
    list2 = [9999, 1, 2, 9999, 3]

    fs.add_constant(list1, 1)
    assert(list1 == [2, 3, 4, 5, 6])
    fs.add_constant(list1, .5)
    assert(list1 == [2.5, 3.5, 4.5, 5.5, 6.5])

    fs.add_constant(list2, 1)
    assert(list2 == [9999, 2, 3, 9999, 4])


def test_multiply_constant():
    list1 = [1, 2, 3, 4, 5]
    list2 = [9999, 1, 2, 9999, 3]

    fs.multiply_by_constant(list1, 2)
    assert(list1 == [2, 4, 6, 8, 10])
    fs.multiply_by_constant(list1, .1)
    assert(list1 == [2*.1, 4*.1, 6*.1, 8*.1, 10*.1]) #Ccan't just write out [.2, .4, .6, .8, 1] because the floats will be slightly inacurate



def test_mask_element():
    list = [10, 20, 30, 40, 50]

    fs.mask_element(list, 2)
    assert(list == [10, 20, 9999, 40, 50])
    fs.mask_element(list, 0)
    fs.mask_element(list, 4)
    assert(list == [9999, 20, 9999, 40, 9999])