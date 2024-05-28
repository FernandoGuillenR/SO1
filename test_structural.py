import pytest 
import example

def test_can_call_existing_endpoints_of_the_API():
    try:
        ret = example.get_coordinates("Lima,Peru")
        assert(ret is not None)
    except:
        False, "Exception raised wjem ca;;omg am existing function"


def test_cannot_call_non_existing_endpoints_of_the_API():
    try:
        ret = example.something_not_existent("blah blah")
        assert False, "Exception not raised"
    except:
        pass

def test_the_result_is_correct_for_simple_cases():
    detected = example.get_coordinates("Lima,Peru")
    expected = (-12.0621065,-77.0365256)
    assert detected == expected, "The result is not correct"

