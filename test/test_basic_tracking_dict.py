import pytest

from testionary.basic import BasicTrackingDict

@pytest.fixture
def basic_tracking_dict():
    return BasicTrackingDict({"a":1, "b":2})

def test_bracket_access_is_counted(basic_tracking_dict):
    basic_tracking_dict["a"]
    assert {"a"} == basic_tracking_dict.accessed_keys

def test_get_access_is_counted(basic_tracking_dict):
    basic_tracking_dict["a"]
    assert {"a"} == basic_tracking_dict.accessed_keys

def test_bracket_set_item_is_counted(basic_tracking_dict):
    basic_tracking_dict["a"] = 2
    assert basic_tracking_dict["a"] == 2
    assert {"a"} == basic_tracking_dict.modified_keys
    
def test_update_with_tuple_list_is_counted(basic_tracking_dict):
    basic_tracking_dict.update([("a",2)])
    assert basic_tracking_dict["a"] == 2
    assert {"a"} == basic_tracking_dict.modified_keys

def test_update_with_dict_is_counted(basic_tracking_dict):
    basic_tracking_dict.update({"a":2})
    assert basic_tracking_dict["a"] == 2
    assert {"a"} == basic_tracking_dict.modified_keys

def test_update_with_kwargs_is_counted(basic_tracking_dict):
    basic_tracking_dict.update(a=2)
    assert basic_tracking_dict["a"] == 2
    assert {"a"} == basic_tracking_dict.modified_keys


def test_union_assign_with_dict_is_counted(basic_tracking_dict):
    basic_tracking_dict |= {"a":2}
    assert basic_tracking_dict["a"] == 2
    assert {"a"} == basic_tracking_dict.modified_keys

def test_union_assign_with_tuple_list_is_counted(basic_tracking_dict):
    basic_tracking_dict |= [("a",2)]
    assert basic_tracking_dict["a"] == 2
    assert {"a"} == basic_tracking_dict.modified_keys
