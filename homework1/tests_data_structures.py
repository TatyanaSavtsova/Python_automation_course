

def test_string_concatenation(function_fixture, module_fixture, session_fixture):

    """This test checks the concatenation of 2 strings."""

    string1 = "Harry "
    string2 = "Potter"
    assert string1 + string2 == "Harry Potter", "The result of concatenation is not Harry Potter."


def test_list_length(function_fixture, module_fixture, session_fixture):

    """This test checks the length of the list."""

    test_list = [i for i in range(1, 9)]
    assert len(test_list) == 8, "The length of the list test_list does not equal 8."


def test_list_append(function_fixture, module_fixture, session_fixture):

    """This test checks that the element exists in the list after appending."""

    test_list = ['This', 'is', 'the']
    x = 'end'
    test_list.append(x)
    assert 'end' in test_list, "The list test_list does not contain 'end'."


def test_tuple_slice(function_fixture, module_fixture, session_fixture):

    """This test checks the slice of tuple."""

    test_tuple = ('a', 'a', 'a', 'python', 'b', 'b')
    assert test_tuple[3:4] == ('python',), "The result of slicing is not 'python."


def test_tuple_length(function_fixture, module_fixture, session_fixture):

    """This test checks the length of tuple."""

    test_tuple = ('a', 'a', 'a', 'python', 'b', 'b')
    assert len(test_tuple) == 6, "The length of the tuple test_tuple is not 6."


def test_tuple_max(function_fixture, module_fixture, session_fixture):

    """This test checks the max value in tuple."""

    test_tuple = (1, 2, 3, 6, 4)
    assert max(test_tuple) == 6, "The max of tuple test_tuple is not 6."


def test_dict_get(function_fixture, module_fixture, session_fixture):

    """This test checks a value for the given key."""

    test_dict = {'name': 'Alice', 'surname': 'Perry'}
    assert test_dict.get('name') == 'Alice', "The value of key 'name' is not 'Alice'."


def test_set_intersection(function_fixture, module_fixture, session_fixture):

    """This test checks the intersection of 2 sets."""

    test_set1 = {1, 2, 3}
    test_set2 = {3, 4, 5}
    assert (test_set1 & test_set2) == {3}, "The intersection of test_set1 and test_set2 is not 3."


def test_numbers_exponent(function_fixture, module_fixture, session_fixture):

    """This test checks the result of raising first operand to the power of the second operand."""

    a = 2
    b = 8
    assert a ** b == 256, "The result of raising 2 to the power of 3 is not 256."


def test_numbers_modulus(function_fixture, module_fixture, session_fixture):

    """This test checks the remainder left when one operand is divided by a second operand."""

    a = 20
    b = 3
    assert a % b == 2, "The remainder of divided 20 to 3 is not 2."

