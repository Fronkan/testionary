import pytest

from testionary.tracking_dict import TrackingDict


@pytest.fixture
def tracking_dict():
    return TrackingDict({"a": 1, "b": 2})


def test_bracket_access_is_counted(tracking_dict):
    tracking_dict["a"]
    assert {"a"} == tracking_dict.accessed_keys


def test_get_access_is_counted(tracking_dict):
    tracking_dict["a"]
    assert {"a"} == tracking_dict.accessed_keys


def test_bracket_set_item_is_counted(tracking_dict):
    tracking_dict["a"] = 2
    assert tracking_dict["a"] == 2
    assert {"a"} == tracking_dict.modified_keys


def test_update_with_tuple_list_is_counted(tracking_dict):
    tracking_dict.update([("a", 2)])
    assert tracking_dict["a"] == 2
    assert {"a"} == tracking_dict.modified_keys


def test_update_with_dict_is_counted(tracking_dict):
    tracking_dict.update({"a": 2})
    assert tracking_dict["a"] == 2
    assert {"a"} == tracking_dict.modified_keys


def test_update_with_kwargs_is_counted(tracking_dict):
    tracking_dict.update(a=2)
    assert tracking_dict["a"] == 2
    assert {"a"} == tracking_dict.modified_keys


def test_union_assign_with_dict_is_counted(tracking_dict):
    tracking_dict |= {"a": 2}
    assert tracking_dict["a"] == 2
    assert {"a"} == tracking_dict.modified_keys


def test_union_assign_with_tuple_list_is_counted(tracking_dict):
    tracking_dict |= [("a", 2)]
    assert tracking_dict["a"] == 2
    assert {"a"} == tracking_dict.modified_keys


def test_iteration_tracking_false(tracking_dict):
    assert not tracking_dict.has_been_iterated


def test_iteration_tracking_for(tracking_dict):
    for k in tracking_dict:
        pass
    assert tracking_dict.has_been_iterated


@pytest.mark.parametrize(
    "method_name",
    ["keys", "values", "items"],
)
def test_iteration_dict_methods(tracking_dict, method_name):
    assert not tracking_dict.has_been_iterated
    method = getattr(tracking_dict, method_name)
    for a in method():
        pass
    assert tracking_dict.has_been_iterated


def test_iteration_with_in_operator(tracking_dict):
    "a" in tracking_dict
    assert tracking_dict.has_been_iterated


def test_iteration_with_in_operator_does_not_exist(tracking_dict):
    "a non-existing key" in tracking_dict
    assert tracking_dict.has_been_iterated
