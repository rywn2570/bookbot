import pytest
from stats import count_words, count_characters, sort_on, chars_dict_to_sorted_list


def test_count_words():
    assert count_words("hello there") == 2
    assert count_words("") == 0


    with pytest.raises(Exception):
        count_characters(0)

    with pytest.raises(Exception):
        count_characters({})

    with pytest.raises(Exception):
        count_characters([])
        


def test_count_characters():
    assert count_characters("HI") == {'h': 1, 'i': 1}

def test_sort_on():
    assert sort_on(["h", 1]) == 1

def test_chars_dict_to_sorted_list():
    assert chars_dict_to_sorted_list({'h': 1, 'i': 1}) == [('h', 1), ('i', 1)]