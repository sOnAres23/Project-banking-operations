from src.processing import filter_by_state, sort_by_date


def test_filter_by_state(list_dict, list_filter_state):
    assert filter_by_state(list_dict) == list_filter_state


def test_sort_by_date(list_dict, list_sort_date):
    assert sort_by_date(list_dict) == list_sort_date
